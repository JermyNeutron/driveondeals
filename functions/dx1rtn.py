# Calculates next day return tuple
import sys
sys.path.append(".")

from datetime import datetime, date, timedelta

from functions import suffix


# Custom texts
checkmark = "\u2713"
xmark = "\u2715"


def main(test: bool, hints_enabled: bool, date_pointer: datetime = "DEFAULT") -> datetime:
    """
    Determines immediate next calendar day and returns datetime object with easy referencing.

    Args:
        test (bool)
        hints_enabled (bool)
        meta_krono (datetime)

    Returns:
        tuple: a tuple containing:
            0) date_pointer (datetime): Returning original datetime object.
            1) current_time (str): The current time in format HH:MM:SS, e.g. "07:25:40".
            2) date_current (str): The current date (YYYY-MM-DD).
            3) date_current_day (str): The current day (DD).
            4) date_current_day_sfx (str): (DD) with suffix, e.g. 27th.
            5) date_dow (str): "Day of Week", e.g. Tuesday.
            6) date_current_month_ind (str): The current month (MM).
            7) date_current_month_str (str): The current month, e.g. September.
            8) date_current_year (str): The current year (YYYY).
    """
    if date_pointer == "DEFAULT":
        date_pointer = datetime.fromisoformat("2024-10-12 19:18:16.708059")
        hints_enabled and print(f"HINT {__name__}: Function defaulted to ambiguous datetime object!!!", end="")
    hints_enabled and print(f"HINT {__name__}: Receiving date_pointer as {date_pointer}")
    
    rtn_tuple = []
    next_day_datetime = date_pointer + timedelta(days=1)
    rtn_tuple.append(next_day_datetime)
    time_current = next_day_datetime.strftime("%H:%M:%S")
    rtn_tuple.append(time_current)
    date_current = next_day_datetime.strftime("%Y-%m-%d")
    rtn_tuple.append(date_current)
    date_current_day = next_day_datetime.strftime("%d")
    rtn_tuple.append(date_current_day)
    date_current_day_sfx = suffix.main(test, hints_enabled, date_current_day)
    rtn_tuple.append(date_current_day_sfx)
    date_dow = next_day_datetime.strftime("%A")
    rtn_tuple.append(date_dow)
    date_current_mont_int = next_day_datetime.strftime("%m")
    rtn_tuple.append(date_current_mont_int)
    date_current_mont_str = next_day_datetime.strftime("%B")
    rtn_tuple.append(date_current_mont_str)
    date_current_year = next_day_datetime.strftime("%Y")
    rtn_tuple.append(date_current_year)

    hints_enabled and print(f"HINT {__name__}: Returning newly created DEFAULT datetime tuple for NEXT day: {next_day_datetime} {checkmark}")
    return tuple(rtn_tuple)


def main_simp(test: bool, hints_enabled: bool, date_pointer: datetime = "DEFAULT") -> tuple[datetime, str]:
    """
    Determines immediate next calendar day and returns datetime object with suffix ONLY.

    Args:
        test (bool)
        hints_enabled (bool)
        date_pointer (datetime)

    Returns:
        tuple: a tuple containing:
            0) date_pointer (datetime): Returning original datetime object.
            1) date_current_day_sfx (str): (DD) with suffix, e.g. 27th.
    """
    if date_pointer == "DEFAULT":
        date_pointer = datetime.fromisoformat("2024-10-12 19:18:16.708059")
        hints_enabled and print(f"HINT {__name__}: Function defaulted to ambiguous datetime object!!!")
    rtn_tuple = []
    next_day_datetime = date_pointer + timedelta(days=1)
    rtn_tuple.append(next_day_datetime)
    next_day_suffix = suffix.main(test, hints_enabled, next_day_datetime.strftime("%d"))
    rtn_tuple.append(next_day_suffix)
    
    hints_enabled and print(f"HINT {__name__}: Returning newly created SIMPLE datetime tuple for NEXT day: {next_day_datetime} {checkmark}")
    return tuple(rtn_tuple)


if __name__ == "__main__":
    test = True
    hints_enabled = True
    
    main(test, hints_enabled)