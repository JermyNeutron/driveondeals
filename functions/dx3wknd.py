# Determine Upcoming Weekend Dates

import sys
sys.path.append(".")

from datetime import datetime, date, timedelta
from functions import est_date


# TEST
def test_meta_dt(test: bool, hints_enabled: bool) -> datetime:
    # return datetime.now()
    return datetime.fromisoformat("2024-12-28")



def test_meta_tup(test: bool, hints_enabled: bool) -> tuple:
    return est_date.get_now(test, hints_enabled)


# test time difference between calling other function and calling datetime.now() internally
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


    # find starting Friday
    def find_start(test: bool, hints_enabled: bool, date_pointer: timedelta) -> tuple:
        hints_enabled and print(date_pointer.strftime("%A"))
        if date_pointer.strftime("%A") != "Friday":
            tgt_date = date_pointer
            while tgt_date.strftime("%A") != "Friday":
                tgt_date += timedelta(days=1)
            date_pointer = tgt_date
        print(f"HINT {__name__}: The nearest Friday is: {date_pointer}")


    dx3wknd_start = find_start(test, hints_enabled, date_pointer)


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
    rtn_tuple = []


    def find_start(test: bool, hints_enabled: bool, date_pointer: timedelta) -> datetime:
        date_start = date_pointer
        if date_start.strftime("%A") != "Friday":
            tgt_date = date_start
            while tgt_date.strftime("%A") != "Friday":
                tgt_date += timedelta(days=1)
            date_start = tgt_date
        print(f"HINT {__name__}: The nearest Friday is: {date_start}")
        return date_start


    dx3wknd_start_datetime = find_start(test, hints_enabled, date_pointer)
    dx3wknd_start = est_date.main_simp(test, hints_enabled, dx3wknd_start_datetime)
    rtn_tuple.append(dx3wknd_start)


    def find_end(test: bool, hints_enabled: bool, dx3wknd_start_datetime: timedelta) -> datetime:
        date_return = dx3wknd_start_datetime + timedelta(days=3)
        return date_return

        
    dx3wknd_end_datetime = find_end(test, hints_enabled, dx3wknd_start_datetime)
    dx3wknd_end = est_date.main_simp(test, hints_enabled, dx3wknd_end_datetime)
    rtn_tuple.append(dx3wknd_end)

    print(rtn_tuple)
    return tuple(rtn_tuple)


if __name__ == "__main__":
    test = True
    hints_enabled = True
    meta_date = datetime.now()

    main_simp(test, hints_enabled, meta_date)