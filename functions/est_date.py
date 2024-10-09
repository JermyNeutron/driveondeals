import time
from datetime import datetime


months_poplist = {
    "01": "January",
    "02": "February",
    "03": "March",
    "04": "April",
    "05": "May",
    "06": "June",
    "07": "July",
    "08": "August",
    "09": "September",
    "10": "October",
    "11": "November",
    "12": "December",
}


# Standard current time retrieval
def get_now(test: bool, hints_enabled: bool) -> tuple[str, str, str, str, str]:
    """
    Automatically retrieves the current date and time.

    Args:
        test (bool)
        hints_enabled (bool)

    Returns:
        tuple: a tuple containing:
            0) current_time (str): The current time in format HH:MM:SS, e.g. "07:25:40".
            1) date_current_day (str): The current day (DD).
            2) date_current_day_sfx (str): (DD) with suffix, e.g. 27th.
            3) date_dow (str): "Day of Week", e.g. Tuesday.
            4) date_current_month_ind (str): The current month (MM).
            5) date_current_month_str (str): The current month, e.g. September.
            6) date_current_year (str): The current year (YYYY).
    """


    # Suffix function only tested on Alamo website
    def find_suffix(test: bool, hints_enabled: bool, date_day: str) -> str:
        """
        Determines proper suffix for day selected as required in Alamo's website.

        Args:
            test (bool)
            hints_enabled (bool)
            date_day (str)

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
            hints_enabled and print(f"HINT {find_suffix}: {date_day} returned as {mod_day}")
            return mod_day
        

    def minimum_date_selection(test: bool, hints_enabled: bool) -> str:
        date_current = time.strftime("")
        # possible function to restrict backward reseverations
        pass


    def month_int2str(test: bool, hints_enabled: bool, month_int: str):
        for month_ind, month_str in months_poplist.items():
            if month_ind == month_int:
                month_return = month_str
                hints_enabled and print(f"HINT {month_int2str}: {month_int} returning as {month_return}")
                return month_return
    

    time_current = time.strftime("%H:%M:%S")
    date_current_day = str(int(time.strftime("%d"))) # (str)
    date_current_day_sfx = find_suffix(test, hints_enabled, date_current_day) # (str)
    date_dow = datetime.now().strftime("%A")
    date_current_month_ind = time.strftime("%m")
    date_current_month_str = month_int2str(test, hints_enabled, date_current_month_ind)
    date_current_year = time.strftime("%Y")
    if hints_enabled:
        print(f"\nHINT {get_now}: {{time_current}}: {time_current}")
        print(f"HINT {get_now}: {{date_current_day}}: {date_current_day}")
        print(f"HINT {get_now}: {{date_current_day_sfx}}: {date_current_day_sfx}")
        print(f"HINT {get_now}: {{date_dow}}: {date_dow}")
        print(f"HINT {get_now}: {{date_current_month_ind}}: {date_current_month_ind}")
        print(f"HINT {get_now}: {{date_current_month_str}}: {date_current_month_str}")
        print(f"HINT {get_now}: {{date_current_year}}: {date_current_year}\n")
    return time_current, date_current_day, date_current_day_sfx, date_dow, date_current_month_ind, date_current_month_str, date_current_year


# TESTS


def test_get_now(test: bool, hints_enabled: bool):
    """
    Test function to print return tuple.

    "Automatically retrieves the current date and time."

    Args:
        test (bool)
        hints_enabled (bool)

    Returns:
        tuple: a tuple containing:
            0) current_time (str): The current time in format HH:MM:SS, e.g. "07:25:40".
            1) date_current_day (str): The current day (DD).
            2) date_current_day_sfx (str): (DD) with suffix, e.g. 27th.
            3) date_dow (str): "Day of Week", e.g. Tuesday.
            4) date_current_month_ind (str): The current month (MM).
            5) date_current_month_str (str): The current month, e.g. September.
            6) date_current_year (str): The current year (YYYY).
    """
    meta_date_today = get_now(test, hints_enabled)
    for i, value in enumerate(meta_date_today, start=0):
        print(f"HINT {test_get_now}:", i, value)


if __name__ == "__main__":
    test = True
    hints_enabled = True
    # meta_date_today = get_now(test, hints_enabled) # important for meta to be collected upon initial program execution
    test_get_now(test, hints_enabled)