# Determines suffix for day given.

def main(test: bool, hints_enabled: bool, date_day: str) -> str:
    """
    Determines proper suffix for day argued.

    Args:
        test (bool)
        hints_enabled (bool)
        date_day (str)

    Returns:
        mod_day (str): e.g. "23rd"
    """
    mod_day = date_day
    if int(date_day) < 1 or int(date_day) > 31:
        hints_enabled and print(f"HINT {__name__}: invalid day entered.")
        pass # possible change return value
    else:
        if date_day in ("11", "12", "13"):
            mod_day += "th"
        elif date_day[-1] == "1":
            mod_day += "st"
        elif date_day[-1] == "2":
            mod_day += "nd"
        elif date_day[-1] == "3":
            mod_day += "rd"
        else:
            mod_day += "th"
        hints_enabled and print(f"HINT {__name__}: {date_day} returned as {mod_day}\n")
        return mod_day
        
if __name__ == "__main__":
    test = True
    hints_enabled = True
    date_day = "31"
    
    main(test, hints_enabled, date_day)