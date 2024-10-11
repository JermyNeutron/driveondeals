# Determine Upcoming Weekend Dates

from datetime import datetime, date
import est_date

# TEST
meta_date = est_date.get_now(True, True)

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
    year = int(current_date[0:4])
    month = 12 # int(current_date[5:7])
    day = 28 # int(current_date[8:10])
    # print(f"REMOVABLE {main}, {year}")
    # print(f"REMOVABLE {main}, {month}")
    # print(f"REMOVABLE {main}, {day}")
    

# currently needs rework as it doesn't lapse into the new year
    current_day_str = date(year, month, day).strftime("%A")
    print(date(year, month, day))
    current_day_no = day
    end_day: str
    if current_day_str != "Friday":
        date_point = current_day_str
        while date_point != "Friday":
            try:
                current_day_no += 1
                current_temp_str = date(year, month, current_day_no).strftime("%A")
                print(f"current_temp_str: {current_temp_str}, {current_day_no}")
                date_point = current_temp_str
            except ValueError as e:
                if (month + 1) % 13:
                    month += 1
                    day = 0
                else:
                    year += 1
                    month = 1
                    day = 0
        dx3wknd_start = date(year, month, current_day_no)
        dx3wknd_end = date(year, month, current_day_no + 3)
        print(f"Starting Friday: {dx3wknd_start}")
        print(f"Ending Monday: {dx3wknd_end}")


if __name__ == "__main__":
    test = True
    hints_enabled = True
    main(True, True, meta_date[1])