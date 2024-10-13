import time
from datetime import datetime

import sys

sys.path.append(".")

from functions import suffix


# Standard current time retrieval
def get_now(test: bool, hints_enabled: bool) -> tuple[str, str, str, str, str, str, str]:
    """
    Automatically retrieves the current date and time.

    Args:
        test (bool)
        hints_enabled (bool)

    Returns:
        tuple: a tuple containing:
            0) meta_krono (tup): Everything retrieved from datetime.now()
            1) current_time (str): The current time in format HH:MM:SS, e.g. "07:25:40".
            2) date_current (str): The current date (YYYY-MM-DD).
            3) date_current_day (str): The current day (DD).
            4) date_current_day_sfx (str): (DD) with suffix, e.g. 27th.
            5) date_dow (str): "Day of Week", e.g. Tuesday.
            6) date_current_month_ind (str): The current month (MM).
            7) date_current_month_str (str): The current month, e.g. September.
            8) date_current_year (str): The current year (YYYY).
    """
        

    def minimum_date_selection(test: bool, hints_enabled: bool) -> str:
        date_current = time.strftime("")
        # possible function to restrict backward reseverations
        pass
    
    # POSSIBLE condense .strftime()'s to minimize tuple
    meta_krono = datetime.now()
    time_current = meta_krono.strftime("%H:%M:%S")
    date_current = meta_krono.strftime("%Y-%m-%d")
    date_current_day = meta_krono.strftime("%d")
    date_current_day_sfx = suffix.main(test, hints_enabled, date_current_day) # (str)
    date_dow = meta_krono.strftime("%A")
    date_current_month_int = meta_krono.strftime("%m")
    date_current_month_str = meta_krono.strftime("%B")
    date_current_year = meta_krono.strftime("%Y")
    if hints_enabled:
        print(f"\nHINT {__name__}: {{meta_krono}}: {meta_krono}")
        print(f"HINT {__name__}: {{time_current}}: {time_current}")
        print(f"HINT {__name__}: {{date_current}}: {date_current}")
        print(f"HINT {__name__}: {{date_current_day}}: {date_current_day}")
        print(f"HINT {__name__}: {{date_current_day_sfx}}: {date_current_day_sfx}")
        print(f"HINT {__name__}: {{date_dow}}: {date_dow}")
        print(f"HINT {__name__}: {{date_current_month_int}}: {date_current_month_int}")
        print(f"HINT {__name__}: {{date_current_month_str}}: {date_current_month_str}")
        print(f"HINT {__name__}: {{date_current_year}}: {date_current_year}\n")
    return meta_krono, time_current, date_current, date_current_day, date_current_day_sfx, date_dow, date_current_month_int, date_current_month_str, date_current_year


# TESTS
def test_get_now(test: bool, hints_enabled: bool):
    """
    Test function to print return tuple.

    Automatically retrieves the current date and time.

    Args:
        test (bool)
        hints_enabled (bool)

    Returns:
        tuple: a tuple containing:
            0) current_time (str): The current time in format HH:MM:SS, e.g. "07:25:40".
            1) date_current (str): The current date (YYYY-MM-DD).
            2) date_current_day (str): The current day (DD).
            3) date_current_day_sfx (str): (DD) with suffix, e.g. 27th.
            4) date_dow (str): "Day of Week", e.g. Tuesday.
            5) date_current_month_ind (str): The current month (MM).
            6) date_current_month_str (str): The current month, e.g. September.
            7) date_current_year (str): The current year (YYYY).
    """
    meta_date_today = get_now(test, hints_enabled)
    for i, value in enumerate(meta_date_today, start=0):
        print(f"HINT {test_get_now}:", i, value)


if __name__ == "__main__":
    test = True
    hints_enabled = True
    
    get_now(test, hints_enabled)