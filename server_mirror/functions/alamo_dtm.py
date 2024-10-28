# Server-Mirror

import sys
import json
import logging

import import_logging
from resources import alamo_example_tuples

import_logging.main("resources/alamo_dtm_logs.txt")

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
    with open("resources/alamo_dtm.json", "r") as file:
        dtm_import_list = json.load(file)

    # Was there a change?
    alt = 0
    # Compare dtms and descriptions
    for i in query:
        # if type Premium (since there are 2 of them)
        if i[2] == "Premium":
            pass
        # everything else
        elif i[2] in dtm_import_list:
            test and print(dtm_import_list[i[2]])
            if i[3] != dtm_import_list[i[2]]["description"]:
                dtm_import_list[i[2]]["description"] = i[3]
                logging.info(f'HINT {__name__}: "{i[2]}" had their description assigned to "{i[3]}".')
                alt += 1
            if i[6] != dtm_import_list[i[2]]["dtm"]:
                dtm_import_list[i[2]]["dtm"] = i[6]
                logging.info(f'HINT {__name__}: "{i[2]}" had their dtm assigned to "{i[6]}".')
                alt += 1
        else:
            print(f'we found something new: {i[2]}')
    
    if alt == 0:
        hints_enabled and print(f"HINT {__name__}: dtm's in alamo_dtm.json are up to date.")
    # write to json file
    else:
        with open("resources/alamo_dtm.json", "w") as f:
            json.dump(dtm_import_list, f, indent=4)        


if __name__ == "__main__":
    test = False
    hints_enabled = True
    myvar = alamo_example_tuples.example_tuples
    dtm_update(test, hints_enabled, myvar)
