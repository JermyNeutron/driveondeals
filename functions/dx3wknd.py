# Determine Upcoming Weekend Dates

import sys
sys.path.append(".")

from datetime import datetime, date
from functions import est_date


# TEST
def test_meta(test, hints_enabled):
    return est_date.get_now(test, hints_enabled)


# test time difference between calling other function and calling datetime.now() internally
def main(test: bool, hints_enabled: bool, current_date: str) -> tuple[str, str]:
    """
    Automatically determines upcoming 3 day weekend dates (YYYY-MM-DD).

    Args:
        test (bool)
        hints_enabled (bool)
        current_date (str)

    Returns:
        tuple: a tuple containing:
            0) start date (YYYY-MM-DD)
            1) end date (YYYY-MM-DD)

    Indices:
        0-3: YEAR
        5-6: MONTH
        8-9: DAY
    """
    print(current_date)
    year = int(current_date[0:4])
    month = int(current_date[5:7])
    day = int(current_date[8:10])
    

    current_day_str = date(year, month, day).strftime("%A")
    hints_enabled and print(date(year, month, day))
    current_day_no = day
    if current_day_str != "Friday":
        date_point = current_day_str
        temp_year = year
        while date_point != "Friday":
            try:
                hints_enabled and print(temp_year, month, current_day_no)
                current_day_no += 1
                current_temp_str = date(temp_year, month, current_day_no).strftime("%A")
                hints_enabled and print(f"current_temp_str: {current_temp_str}, {current_day_no}")
                date_point = current_temp_str
            except ValueError as e:
                if (month + 1) % 13:
                    hints_enabled and print(f"HINT: Month advanced. Error handled for: {e}")
                    month += 1
                    current_day_no = 0
                else:
                    hints_enabled and print(f"HINT: Year advanced. Error handled for: {e}")
                    temp_year += 1
                    month = 1
                    current_day_no = 0
        dx3wknd_start = date(temp_year, month, current_day_no)
        dx3wknd_end = date(temp_year, month, current_day_no + 3)
        if hints_enabled:
            print(f"Starting Friday: {dx3wknd_start}")
            print(f"Ending Monday: {dx3wknd_end}")
        return dx3wknd_start, dx3wknd_end

def main_b(test: bool, hints_enabled: bool) -> tuple[str, str]:
    """
    Redudant function to test time delta when referencing vs. calling datetime.

    Automatically determines upcoming 3 day weekend dates (YYYY-MM-DD).

    Args:
        test (bool)
        hints_enabled (bool)

    Returns:
        tuple: a tuple containing:
            0) start date (YYYY-MM-DD)
            1) end date (YYYY-MM-DD)

    Indices:
        0-3: YEAR
        5-6: MONTH
        8-9: DAY
    """
    current_date = est_date.get_now(test, hints_enabled)
    year = int(current_date[1][0:4])
    month = 12 # int(current_date[5:7])
    day = 28 # int(current_date[8:10])
    

# currently needs rework as it doesn't lapse into the new year
    current_day_str = date(year, month, day).strftime("%A")
    hints_enabled and print(date(year, month, day))
    current_day_no = day
    if current_day_str != "Friday":
        date_point = current_day_str
        temp_year = year
        while date_point != "Friday":
            try:
                hints_enabled and print(temp_year, month, current_day_no)
                current_day_no += 1
                current_temp_str = date(temp_year, month, current_day_no).strftime("%A")
                hints_enabled and print(f"current_temp_str: {current_temp_str}, {current_day_no}")
                date_point = current_temp_str
            except ValueError as e:
                if (month + 1) % 13:
                    hints_enabled and print(f"HINT: Month advanced. Error handled for: {e}")
                    month += 1
                    current_day_no = 0
                else:
                    hints_enabled and print(f"HINT: Year advanced. Error handled for: {e}")
                    temp_year += 1
                    month = 1
                    current_day_no = 0
        dx3wknd_start = date(temp_year, month, current_day_no)
        dx3wknd_end = date(temp_year, month, current_day_no + 3)
        if hints_enabled:
            print(f"Starting Friday: {dx3wknd_start}")
            print(f"Ending Monday: {dx3wknd_end}")
        return dx3wknd_start, dx3wknd_end


if __name__ == "__main__":
    test = True
    hints_enabled = True
    meta_date = test_meta(test, hints_enabled)

    main(True, True, meta_date[2])