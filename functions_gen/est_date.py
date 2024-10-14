import time
from datetime import datetime

import sys

sys.path.append(".")

from functions_gen import suffix


# Custom texts
checkmark = "\u2713"
xmark = "\u2715"


def main(test: bool, hints_enabled: bool, date_pointer: datetime) -> tuple[datetime, str]:
    """
    Returns datetime object with easy referencing.

    Args:
        test (bool)
        hints_enabled (bool)
        date_pointer (datetime)

    Returns:
        tuple: a tuple containing:
            0) date_pointer (datetime): Returning original datetime object.
            1) time_current (str): The current time in format HH:MM:SS, e.g. "07:25:40".
            2) date_current (str): The current date (YYYY-MM-DD).
            3) date_current_day (str): The current day (DD).
            4) date_current_day_sfx (str): (DD) with suffix, e.g. 27th.
            5) date_dow (str): "Day of Week", e.g. Tuesday.
            6) date_current_month_ind (str): The current month (MM).
            7) date_current_month_str (str): The current month, e.g. September.
            8) date_current_year (str): The current year (YYYY).
    """
    time_current = date_pointer.strftime("%H:%M:%S")
    date_current = date_pointer.strftime("%Y-%m-%d")
    date_current_day = date_pointer.strftime("%d")
    date_current_day_sfx = suffix.main(test, hints_enabled, str(int(date_current_day))) # (str)
    date_dow = date_pointer.strftime("%A")
    date_current_month_int = date_pointer.strftime("%m")
    date_current_month_str = date_pointer.strftime("%B")
    date_current_year = date_pointer.strftime("%Y")
    if hints_enabled:
        print(f"HINT {__name__}: Received and returning {{date_pointer}}: {date_pointer}")
        print(f"HINT {__name__}: {{time_current}}: {time_current}")
        print(f"HINT {__name__}: {{date_current}}: {date_current}")
        print(f"HINT {__name__}: {{date_current_day}}: {date_current_day}")
        print(f"HINT {__name__}: {{date_current_day_sfx}}: {date_current_day_sfx}")
        print(f"HINT {__name__}: {{date_dow}}: {date_dow}")
        print(f"HINT {__name__}: {{date_current_month_int}}: {date_current_month_int}")
        print(f"HINT {__name__}: {{date_current_month_str}}: {date_current_month_str}")
        print(f"HINT {__name__}: {{date_current_year}}: {date_current_year}")
    rtn_tuple = (date_pointer, time_current, date_current, date_current_day, date_current_day_sfx, date_dow, date_current_month_int, date_current_month_str, date_current_year)
    return rtn_tuple


def main_simp(test: bool, hints_enabled: bool, date_pointer: datetime) -> tuple[datetime, str]:
    """
    Returns datetime object with suffix ONLY.

    Args:
        test (bool)
        hints_enabled (bool)
        date_pointer (datetime)

    Returns:
        tuple: a tuple containing:
            0) date_pointer (datetime): Returning original datetime object.
            1) date_current_day_sfx (str): (DD) with suffix, e.g. 27th.
    """
    hints_enabled and print(f"HINT {__name__}: Datetime received: {date_pointer}")
    suffix_str = suffix.main(test, hints_enabled, str(int(date_pointer.strftime("%d"))))
    rtn_tuple = (date_pointer, suffix_str)
    hints_enabled and print(f"HINT {__name__}: Returning SIMPLE datetime tuple {checkmark}")
    return rtn_tuple


if __name__ == "__main__":
    test = True
    hints_enabled = True
    
    date_pointer = datetime.now()
    main(test, hints_enabled, date_pointer)