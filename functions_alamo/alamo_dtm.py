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


# Test with ('Midsize SUV', 'Nissan Rogue or similar', '5', '4', 'IFAR', '70.00', '88.30')

def dtm_update(test: bool, hints_enabled: bool, query: list) -> None:
    """
    Compares and updates alamo_dtm.json with alamo classes.

    Args:
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
        if i[0] == "Premium":
            pass
        # everything else
        elif i[0] in dtm_import_list:
            test and print(dtm_import_list[i[0]])
            if i[1] != dtm_import_list[i[0]]["description"]:
                dtm_import_list[i[0]]["description"] = i[1]
                logging.info(f'HINT {__name__}: "{i[0]}" had their description assigned to "{i[1]}".')
                alt += 1
            if i[4] != dtm_import_list[i[0]]["dtm"]:
                dtm_import_list[i[0]]["dtm"] = i[4]
                logging.info(f'HINT {__name__}: "{i[0]}" had their dtm assigned to "{i[4]}".')
                alt += 1
        else:
            print('we found something new')
    
    if alt == 0:
        hints_enabled and print(f"HINT {__name__}: dtm's in alamo_dtm.json are up to date.")
    # write to json file
    else:
        with open("functions_alamo/alamo_dtm.json", "w") as f:
            json.dump(dtm_import_list, f, indent=4)        


if __name__ == "__main__":
    test = False
    hints_enabled = True
    myvar = example_tuples.example_tuples
    dtm_update(test, hints_enabled, myvar)
