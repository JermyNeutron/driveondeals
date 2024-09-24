import time
from datetime import datetime


# Standard current time retrieval
def get_now(test, hints_enabled) -> tuple[str, str, str, str, str]:
    """
    Automatically retrieves the current date and time.

    Args:
        test (boolean)
        hints_enabled (boolean)

    Returns:
        tuple: A tuple containing:
            0) current_time (str): The current time in format HH:MM:SS, e.g. "07:25:40".
            1) date_current_day (str): The current day (DD).
            2) date_dow (str): "Day of Week", e.g. Tuesday.
            3) date_current_month (str): The current month (MM).
            4) date_current_year (str): The current year (YYYY).
    """
    time_current = time.strftime("%H:%M:%S")
    date_current_day = time.strftime("%d")
    date_dow = datetime.now().strftime("%A")
    date_current_month = time.strftime("%m")
    date_current_year = time.strftime("%Y")
    if hints_enabled:
        print(f"HINT: {{time_current}}: {time_current}")
        print(f"HINT: {{date_current_day}}: {date_current_day}")
        print(f"HINT: {{date_dow}}: {date_dow}")
        print(f"HINT: {{date_current_month}}: {date_current_month}")
        print(f"HINT: {{date_current_year}}: {date_current_year}")
    return time_current, date_current_day, date_dow, date_current_month, date_current_year


# Suffix function only tested on Alamo website
def find_suffix_alamo(test: bool, hints_enabled: bool, date_day: str) -> str:
    """
    Determines proper suffix for day selected as required in Alamo's website.

    Args:
        test (boolean)
        hints_enabled (boolean)

    Returns:
        mod_day (str): e.g. "23rd"
    """
    mod_day = date_day
    if int(date_day) < 1 or int(date_day) > 31:
        print("invalid day entered.")
        pass # possible change return value
    else:
        if date_day[-1] == "1":
            mod_day += "st"
        elif date_day[-1] == "2":
            mod_day += "nd"
        elif date_day[-1] == "3":
            mod_day += "rd"
        else:
            mod_day += "th"
        hints_enabled and print(f"HINT: {find_suffix_alamo} {date_day} returned as {mod_day}")
        return mod_day


def minimum_date_selection(test, hints_enabled) -> str:
    date_current = time.strftime("")
    pass


# TESTS
def find_suffix(test, hints_enabled):
    day = input("enter a valid calendar day [0,31]: ")
    return_date = find_suffix_alamo(test, hints_enabled, day)

def test1():
    now = datetime.now().strftime("%A") # %A converts day into string
    print(now)

if __name__ == "__main__":
    test = True
    hints_enabled = True
    meta_date_today = get_now(test, hints_enabled) # important for meta to be collected upon initial program execution
    find_suffix_alamo(test, hints_enabled, meta_date_today[1])
    # test1()