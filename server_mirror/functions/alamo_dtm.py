 # Server-Mirror

import json

from functions import import_logging

dtm_logger = import_logging.main("resources/alamo_dtm_logs.txt", "dtm_logger")


def dtm_update(test: bool, hints_enabled: bool, query: list) -> None:
    """
    Compares and updates alamo_dtm.json with alamo classes.

    Parameters:
        test (bool): No application yet.
        hints_enabled (bool):
        query (list): [(1731243736,SNA,Alamo,Midsize SUV,Nissan Rogue or similar,5,4,IFAR,2024-11-10,0,2024-11-11,1,1,91.2,114.43,True), ...,]

    Returns:
        None:
    """

    # Load alamo dtm's
    with open("resources/alamo_dtm.json", "r") as file:
        dtm_import_list = json.load(file)

    # Counter for any changes made for json file.
    alt = 0
    # Compare dtms and descriptions
    for i in query:
        # if type Premium (since there are 2 of them)
        if i[3] == "Premium":
            pass
        else:
            for category, vehtype in dtm_import_list.items():
                if i[3] in vehtype:
                    # everything else
                    if i[4] != vehtype[i[3]]["description"]:
                        vehtype[i[3]]["description"] = i[4]
                        dtm_logger.info(f'HINT {__name__}: "{i[3]}" had their description assigned to "{i[4]}".')
                        alt += 1
                    if i[7] != vehtype[i[3]]["dtm"]:
                        vehtype[i[3]]["dtm"] = i[7]
                        dtm_logger.info(f'HINT {__name__}: "{i[3]}" had their dtm assigned to "{i[7]}".')
                        alt += 1
                    break
            else:
                hints_enabled and print(f'we found something new: {i[3]}')
                dtm_logger.warning(f'{__name__}: we found something new: {i[3]}')

    if alt == 0:
        hints_enabled and print(f"HINT {__name__}: dtm's in alamo_dtm.json are up to date.")
        dtm_logger.info("dtm's in alamo_dtm.json are up to date.")
    # write to json file
    else:
        with open("resources/alamo_dtm.json", "w") as f:
            json.dump(dtm_import_list, f, indent=4)
        dtm_logger.info(f"{__name__}: Changes were saved.")


def logging_test() -> None:
    """Tests logging output to '../resources/alamo_dtm_logs.txt'"""
    dtm_logger.info(f"{__name__}: dtm_logger made from alamo_dtm")


if __name__ == "__main__":
    test = False
    hints_enabled = True

    logging_test()

    # myvar = None
    # dtm_update(test, hints_enabled, myvar)