# Calculates next day return tuple

from datetime import datetime, date

def main(test: bool, hints_enabled: bool, meta_krono: datetime = "DEFAULT") -> datetime:
    """
    Calculates next day return.

    Args:
        test (bool)
        hints_enabled (bool)
        meta_krono (datetime)

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
    if meta_krono == "DEFAULT":
        meta_krono = datetime.fromisoformat("2024-10-12 19:18:16.708059")
        hints_enabled and print(f"\nHINT {__name__}: Function defaulted to ambiguous datetime object!!!", flush=True)
    hints_enabled and print(f"\nHINT {__name__}: Receiving meta_krono as {type(meta_krono)}", flush=True)
    
    temp_year = int(meta_krono.strftime("%Y"))
    temp_month = int(meta_krono.strftime("%m"))
    temp_day = int(meta_krono.strftime("%d"))

    # Attempt to add one calendar day
    while True:
        try:
            temp_day += 1
            next_day_date = date(temp_year, temp_month, temp_day)
            break
        except ValueError as e:
            if (temp_month + 1) % 13:
                temp_year += 1
                temp_month = 1
                temp_day = 0
            else:
                temp_month += 1
                temp_day = 0

    hints_enabled and print(f"HINT {__name__}: Returning newly created datetime object for {next_day_date} \u2713\n", flush=True)
    return datetime.fromisoformat(f"{next_day_date} {meta_krono.strftime('%H:%M:%S.%f')}")


if __name__ == "__main__":
    test = True
    hints_enabled = True
    
    main(test, hints_enabled)