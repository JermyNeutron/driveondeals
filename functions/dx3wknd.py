# Determine Upcoming Weekend Dates

import sys
sys.path.append(".")

from datetime import datetime, date, timedelta
from functions import est_date


# Custom texts
checkmark = "\u2713"
xmark = "\u2715"


# TEST: creates datetime object
def test_meta_dt(test: bool, hints_enabled: bool) -> datetime:
    choice = int(input("Create datetime object for (1) Now | (2) End of December: "))
    if choice == 1:
        return datetime.now()
    elif choice == 2:
        return datetime.fromisoformat("2024-12-28")
    else:
        return None

# TEST: 
def test_meta_tup(test: bool, hints_enabled: bool) -> tuple:
    meta_date = datetime.now()
    return est_date.main(test, hints_enabled, meta_date)


# Returns DEFAULT datetime tuples
def main(test: bool, hints_enabled: bool, date_pointer: datetime) -> tuple[tuple, tuple]:
    """
    Calculates upcomining Friday and returns weekends' DEFAULT datetime tuples.

    Args:
        test (bool)
        hints_enabled (bool)
        date_pointer (timedelta)

    Returns:
        dx3wknd_start DEFAULT (tuple)
        dx3wknd_start DEFAULT (tuple)
    """


    def find_start(test: bool, hints_enabled: bool, date_pointer: datetime) -> datetime:
        date_start = date_pointer
        if date_start.strftime("%A") != "Friday":
            tgt_date = date_start
            while tgt_date.strftime("%A") != "Friday":
                tgt_date += timedelta(days=1)
            date_start = tgt_date
        hints_enabled and print(f"HINT {__name__}: The nearest Friday is: {date_start}")
        return date_start


    rtn_tuple = []
    dx3wknd_start_datetime = find_start(test, hints_enabled, date_pointer)
    dx3wknd_start = est_date.main(test, hints_enabled, dx3wknd_start_datetime)
    rtn_tuple.append(dx3wknd_start)


    def find_end(test: bool, hints_enabled: bool, dx3wknd_start_datetime: datetime) -> datetime:
        date_return = dx3wknd_start_datetime + timedelta(days=3)
        return date_return

        
    dx3wknd_end_datetime = find_end(test, hints_enabled, dx3wknd_start_datetime)
    dx3wknd_end = est_date.main(test, hints_enabled, dx3wknd_end_datetime)
    rtn_tuple.append(dx3wknd_end)

    hints_enabled and print(f"HINT {__name__}: Returning 3 Day Weekend rental DEFAULT tuple.")
    return tuple(rtn_tuple)


# Returns SIMPLE datetime tuples
def main_simp(test: bool, hints_enabled: bool, date_pointer: datetime) -> tuple[tuple, tuple]:
    """
    Calculates upcomining Friday and returns weekends' SIMPLE datetime tuples.

    Args:
        test (bool)
        hints_enabled (bool)
        date_pointer (timedelta)

    Returns:
        dx3wknd_start SIMPLE (tuple)
        dx3wknd_start SIMPLE (tuple)
    """


    def find_start(test: bool, hints_enabled: bool, date_pointer: datetime) -> datetime:
        date_start = date_pointer
        if date_start.strftime("%A") != "Friday":
            tgt_date = date_start
            while tgt_date.strftime("%A") != "Friday":
                tgt_date += timedelta(days=1)
            date_start = tgt_date
        hints_enabled and print(f"HINT {__name__}: The nearest Friday is: {date_start}")
        return date_start


    rtn_tuple = []
    dx3wknd_start_datetime = find_start(test, hints_enabled, date_pointer)
    dx3wknd_start = est_date.main_simp(test, hints_enabled, dx3wknd_start_datetime)
    rtn_tuple.append(dx3wknd_start)


    def find_end(test: bool, hints_enabled: bool, dx3wknd_start_datetime: datetime) -> datetime:
        date_return = dx3wknd_start_datetime + timedelta(days=3)
        return date_return

        
    dx3wknd_end_datetime = find_end(test, hints_enabled, dx3wknd_start_datetime)
    dx3wknd_end = est_date.main_simp(test, hints_enabled, dx3wknd_end_datetime)
    rtn_tuple.append(dx3wknd_end)

    hints_enabled and print(f"HINT {__name__}: Returning 3 Day Weekend rental SIMPLE tuple.")
    return tuple(rtn_tuple)


if __name__ == "__main__":
    test = True
    hints_enabled = True
    choice_time = int(input("Select choice of timedeltas: (1) test_meta_dt | (2) test_meta_tup: "))
    if choice_time == 1:
        selected_time = test_meta_dt(test, hints_enabled)
    elif choice_time == 2:
        selected_time = test_meta_tup(test, hints_enabled)
    else:
        choice_time = None
        print("invalid choice")
    
    if choice_time == None:
        pass
    else:
        choice_process = int(input("Select choice of execution: (1) Main/DEFAULT | (2) Main_simp/SIMPLE: "))
        if choice_process == 1:
            main(test, hints_enabled, selected_time)
        elif choice_process == 2:
            main_simp(test, hints_enabled, selected_time)
        else:
            print("invalid choice")