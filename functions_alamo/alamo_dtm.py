import sys
import json
import logging
from collections import OrderedDict

sys.path.append(".")

from functions_alamo import example_tuples

from functions_gen import import_logging

import_logging.set_logging("functions_alamo/alamo_dtm_logs.txt")


dtm_list = {
    # Sedans
    "Compact": {"dtm": "CCAR", "description": None},
    "Compact Convertible": {"dtm": None, "description": None}, 
    "Compact Special": {"dtm": None, "description": None},
    "Economy": {"dtm": "ECAR", "description": None},
    "Full Size Hybrid": {"dtm": None, "description": None},
    "Full Size": {"dtm": "FCAR", "description": None},
    "Full Size Elite Electric": {"dtm": None, "description": None},
    "Full Size Elite": {"dtm": "GXAR", "description": None},
    "Intermediate Electric": {"dtm": None, "description": None},
    "Midsize": {"dtm": "ICAR", "description": None},
    "Midsize Convertible": {"dtm": None, "description": None},
    "Luxury": {"dtm": "LCAR", "description": None},
    "Luxury Sport": {"dtm": None, "description": None},
    "Luxury Convertible": {"dtm": None, "description": None},
    "Premium": {"dtm": "PCAR", "description": "Nissan Maxima or similar"},
    "Premium": {"dtm": "PDAR", "description": "Chrysler 300 or similar"},
    "American Muscle Car": {"dtm": None, "description": None}, 
    "Premium Special": {"dtm": "PXAR", "description": None},
    "Standard Elite": {"dtm": "RXAR", "description": None},
    "Standard Hybrid": {"dtm": None, "description": None},
    "Standard": {"dtm": "SCAR", "description": None},
    "Sporty Car": {"dtm": None, "description": None},
    "Convertible": {"dtm": "STAR", "description": None},
    "Corvette": {"dtm": None, "description": None}, 
    "Midsize Luxury Sedan": {"dtm": None, "description": None}, 
    "Midsize Sport Luxury Sedan": {"dtm": None, "description": None}, 
    "Electric Luxury Sedan": {"dtm": None, "description": None}, 
    "Full Size Luxury Sedan": {"dtm": None, "description": None}, 
    "Performance Sport": {"dtm": None, "description": None}, 
    "Luxury Performance Sport": {"dtm": None, "description": None}, 
    "Premium Luxury Sedan": {"dtm": None, "description": None}, 
    "Ultra Performance Sport": {"dtm": None, "description": None}, 
    "Elite Performance Sport": {"dtm": None, "description": None}, 
    "Ultra Luxury Sedan": {"dtm": None, "description": None},

    # SUVs
    "Compact Electric SUV": {"dtm": None, "description": None},
    "Compact SUV": {"dtm": "CFAR", "description": None},
    "Compact SUV AWD": {"dtm": None, "description": None},
    "Full Size SUV":  {"dtm": "FFAR", "description": "Chevrolet Tahoe, Ford Expedition, Nissan Armada or similar"}, # Chevrolet Taho, Ford Expedition, Nissan Armada or similar
    "Full Size SUV AWD": {"dtm": None, "description": None},
    "Jeep Wrangler 4 door": {"dtm": "FJAR", "description": None},
    "Full Size SUV": {"dtm": None, "description": "Chevrolet Tahoe or similar"}, # Chevrolet Tahoe or similar
    "Midsize SUV": {"dtm": "IFAR", "description": None},
    "Midsize SUV AWD": {"dtm": None, "description": None},
    "Jeep": {"dtm": "IJAR", "description": None},
    "Luxury SUV": {"dtm": "LFAR", "description": None},
    "Luxury SUV AWD": {"dtm": None, "description": None},
    "Extended Luxury SUV": {"dtm": None, "description": None},
    "Premium SUV": {"dtm": "PFAR", "description": None},
    "Premium SUV AWD": {"dtm": None, "description": None},
    "Premium Crossover": {"dtm": "PGAR", "description": None},
    "Premium Crossover AWD": {"dtm": None, "description": None},
    "Premium All-Terrain": {"dtm": None, "description": None},
    "Standard Elite SUV": {"dtm": "RFAR", "description": None},
    "Standard SUV": {"dtm": "SFAR", "description": None},
    "Standard SUV AWD": {"dtm": None, "description": None},
    "Standard Crossover": {"dtm": None, "description": None},
    "Standard Crossover AWD": {"dtm": None, "description": None},
    "Midsize Luxury SUV": {"dtm": "UDAR", "description": None},
    "Premium Elite SUV": {"dtm": "UFAR", "description": None},
    "Midsize Elite Luxury SUV": {"dtm": "WDAR", "description": None},
    "Electric Luxury SUV": {"dtm": None, "description": None},
    "Full Size Luxury SUV": {"dtm": None, "description": None},
    "Special SUV": {"dtm": None, "description": None},
    "Premium Luxury SUV": {"dtm": None, "description": None},
    "Ultra Luxury SUV": {"dtm": None, "description": None},
    "Medium Hybrid SUV": {"dtm": None, "description": None},

    # Trucks
    "Full Size Electric Pickup": {"dtm": None, "description": None},
    "Pickup": {"dtm": "PPAR", "description": None},
    "Full Size Diesel Pickup": {"dtm": None, "description": None},
    "Full Size Electric Pickup 4WD": {"dtm": None, "description": None},
    "Premium Pickup 4WD": {"dtm": None, "description": None},
    "Standard Pickup": {"dtm": "SPAR", "description": None},
    "Standard Pickup 4WD": {"dtm": None, "description": None},

    # Vans
    "15 Passenger Van": {"dtm": None, "description": None},
    "10 Passenger Van": {"dtm": None, "description": None},
    "7 Passenger Minivan": {"dtm": "MVAR", "description": None},
    "12 Passenger Van Med/High Roof": {"dtm": None, "description": None},
    "Heavy Duty Cargo Van 4WD": {"dtm": None, "description": None},
    "12 Passenger Van": {"dtm": None, "description": None},
    "Cargo Van": {"dtm": None, "description": None},
    "Cargo Van 4WD": {"dtm": None, "description": None},
    "8 Passenger Minivan": {"dtm": "SVAR", "description": None},
    "Heavy Duty High Roof Cargo Van 4WD": {"dtm": None, "description": None},
    "15 Passenger Van Med/High Roof": {"dtm": None, "description": None},
    "Limo Van": {"dtm": None, "description": None},

    # Special
    "You Click We Pick": {"dtm": "XXAR", "description": "Vehicle determined upon pick-up, Compact or Large"},
    "Drive Happy Default": {"dtm": None, "description": None},
}


# Test with [(1731192271, 'Alamo', 'Midsize SUV', 'Nissan Rogue or similar', '5', '4', 'IFAR', '2024-11-09', 6, '2024-11-10', 0, 1, '70.00', '88.30', True),]

def dtm_update(test: bool, hints_enabled: bool, query: list) -> None:
    """
    Compares and updates alamo_dtm.json with alamo classes.

    Parameters:
        test (bool)
        hints_enabled (bool)
        query (list)

    Returns:
        None
    """
    # Load alamo dtm's
    with open("functions_alamo/alamo_dtm.json", "r") as file:
        dtm_import_list = json.load(file)

    # Was there a change?
    alt = 0
    # Compare dtms and descriptions
    for i in query:
            # if type Premium (since there are 2 of them)
        if i[2] == "Premium":
            print("Premium was passed")
            pass
        else:
            for category, vehtype in dtm_import_list.items():
                if i[2] in vehtype:
                    # everything else
                    test and print(vehtype[i[2]])
                    if i[3] != vehtype[i[2]]["description"]:
                        vehtype[i[2]]["description"] = i[3]
                        logging.info(f'HINT {__name__}: "{i[2]}" had their description assigned to "{i[3]}".')
                        alt += 1
                    if i[6] != vehtype[i[2]]["dtm"]:
                        vehtype[i[2]]["dtm"] = i[6]
                        logging.info(f'HINT {__name__}: "{i[2]}" had their dtm assigned to "{i[6]}".')
                        alt += 1
                    break
            else:
                print(f'we found something new: {i[2]}')
    
    if alt == 0:
        hints_enabled and print(f"HINT {__name__}: dtm's in alamo_dtm.json are up to date.")
    # write to json file
    else:
        print('something changed in the file')
        # with open("functions_alamo/alamo_dtm.json", "w") as f:
        #     json.dump(dtm_import_list, f, indent=4)        


def createarr():
    queries = [(1731192271, 'Alamo', 'Midsize SUV', 'Nissan Rogue or similar', '5', '4', 'IFAR', '2024-11-09', 6, '2024-11-10', 0, 1, '70.00', '88.30', True),
(1731192271, 'Alamo', 'Compact SUV', 'Hyundai Kona or similar', '5', '3', 'CFAR', '2024-11-09', 6, '2024-11-10', 0, 1, '64.00', '80.38', True),
(1731192271, 'Alamo', 'Economy', 'Mitsubishi Mirage or similar', '4', '2', 'ECAR', '2024-11-09', 6, '2024-11-10', 0, 1, '70.42', '87.81', True),
(1731192271, 'Alamo', 'Full Size', 'Toyota Camry or Chevrolet Malibu or similar', '5', '4', 'FCAR', '2024-11-09', 6, '2024-11-10', 0, 1, '70.24', '88.93', True),
(1731192271, 'Alamo', 'Standard Pickup', 'Toyota Tacoma or similar', '4', '3', 'SPAR', '2024-11-09', 6, '2024-11-10', 0, 1, '70.00', '89.58', True),
(1731192271, 'Alamo', 'Midsize', 'Toyota Corolla or similar', '5', '3', 'ICAR', '2024-11-09', 6, '2024-11-10', 0, 1, '72.64', '91.05', True),
(1731192271, 'Alamo', 'Standard', 'VW Jetta or similar', '5', '3', 'SCAR', '2024-11-09', 6, '2024-11-10', 0, 1, '73.62', '92.22', True),
(1731192271, 'Alamo', 'Pickup', 'Ford F150 or similar', '4', '4', 'PPAR', '2024-11-09', 6, '2024-11-10', 0, 1, '72.78', '93.38', True),
(1731192271, 'Alamo', 'Compact', 'Nissan Versa or similar', '5', '2', 'CCAR', '2024-11-09', 6, '2024-11-10', 0, 1, '74.97', '93.51', True),
(1731192271, 'Alamo', 'Premium', 'Nissan Maxima or similar', '5', '4', 'PCAR', '2024-11-09', 6, '2024-11-10', 0, 1, '74.30', '93.63', True),
(1731192271, 'Alamo', 'Standard SUV', 'Chevrolet Equinox or similar', '5', '5', 'SFAR', '2024-11-09', 6, '2024-11-10', 0, 1, '75.00', '94.79', True),
(1731192271, 'Alamo', 'Full Size Elite', 'Audi A5 Sportback or similar', '5', '3', 'GXAR', '2024-11-09', 6, '2024-11-10', 0, 1, '75.94', '96.43', True),
(1731192271, 'Alamo', 'Standard Elite', 'BMW 228i Gran Coupe or similar', '5', '2', 'RXAR', '2024-11-09', 6, '2024-11-10', 0, 1, '78.00', '98.30', True),
(1731192271, 'Alamo', 'Premium Special', 'Audi A3 or BMW 2 Series Gran Coupe or similar', '5', '3', 'PXAR', '2024-11-09', 6, '2024-11-10', 0, 1, '78.32', '98.31', True),
(1731192271, 'Alamo', 'Standard Elite SUV', 'Audi Q3, Cadillac XT4 or similar', '5', '3', 'RFAR', '2024-11-09', 6, '2024-11-10', 0, 1, '77.97', '98.31', True),
(1731192271, 'Alamo', 'Luxury', 'Audi A4 or BMW 3 Series or similar', '5', '4', 'LCAR', '2024-11-09', 6, '2024-11-10', 0, 1, '83.96', '105.64', True),
(1731192271, 'Alamo', 'Premium Crossover', 'Dodge Durango or similar', '7', '3', 'PGAR', '2024-11-09', 6, '2024-11-10', 0, 1, '84.00', '106.07', True),
(1731192271, 'Alamo', 'Jeep', 'Jeep Wrangler 2 Door or similar', '4', '3', 'IJAR', '2024-11-09', 6, '2024-11-10', 0, 1, '104.59', '131.06', True),
(1731192271, 'Alamo', '7 Passenger Minivan', 'Chrysler Pacifica or similar', '7', '5', 'MVAR', '2024-11-09', 6, '2024-11-10', 0, 1, '107.98', '135.33', True),
(1731192271, 'Alamo', 'Jeep Wrangler 4 door', 'Jeep Wrangler Unlimited or similar', '5', '5', 'FJAR', '2024-11-09', 6, '2024-11-10', 0, 1, '109.87', '137.96', True),
(1731192271, 'Alamo', 'You Click We Pick', 'Vehicle determined upon pick-up, Compact or Larger', None, None, 'XXAR', '2024-11-09', 6, '2024-11-10', 0, 1, '117.99', '147.58', True),
(1731192271, 'Alamo', 'Premium SUV', 'Ford Expedition Max, Jeep Wagoneer L or similar', '8', '7', 'PFAR', '2024-11-09', 6, '2024-11-10', 0, 1, '119.00', '149.79', True),
(1731192271, 'Alamo', 'Premium', 'Chrysler 300 or similar', '5', '4', 'PDAR', '2024-11-09', 6, '2024-11-10', 0, 1, '259.98', '322.15', True),
(1731192271, 'Alamo', 'Midsize Luxury SUV', 'Mercedes GLE, BMW X5 or similar', '5', '4', 'UDAR', '2024-11-09', 6, '2024-11-10', 0, 1, '299.00', '371.87', True),
]
    return queries

if __name__ == "__main__":
    test = False
    hints_enabled = True
    # myvar = example_tuples.example_tuples
    # dtm_update(test, hints_enabled, myvar)
    testarr = createarr()
    dtm_update(test, hints_enabled, testarr)