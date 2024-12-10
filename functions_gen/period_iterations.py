from datetime import datetime, date, timedelta

# Custom texts
checkmark = "\u2713"
xmark = "\u2715"


# # # DEPRECATED!
def dx1rtn(
    test: bool,
    hints_enabled: bool,
    date_pointer: datetime,
) -> datetime:
    return_datetime = date_pointer + timedelta(days=1)
    return return_datetime
# # #


def dx3rtn(
    test: bool,
    hints_enabled: bool,
    date_pointer: datetime,
) -> tuple:
    

    def find_start(
            test: bool,
            hints_enabled: bool,
            date_pointer: datetime,
    ) -> datetime:
        date_start = date_pointer + timedelta(days=1)
        if date_start.strftime("%A") != "Friday":
            tgt_date = date_start
            while tgt_date.strftime("%A") != "Friday":
                tgt_date += timedelta(days=1)
            date_start = tgt_date
        return date_start


    rtn_tuple = []
    dx3wknd_start_datetime = find_start(test, hints_enabled, date_pointer)
    dx3wknd_end_datetime = dx3wknd_start_datetime + timedelta(days=3)
    rtn_tuple.append(dx3wknd_start_datetime) 
    rtn_tuple.append(dx3wknd_end_datetime) 
    if test:
        hints_enabled and print(f"{__name__}: dx3rtn returns: {rtn_tuple}")
    return tuple(rtn_tuple)


def sameday(
    test: bool,
    hints_enabled: bool,
    date_pointer: datetime,
) -> tuple[
    datetime,
    datetime,
    int,
    int,
    str,
]:
    pu_date = date_pointer
    do_date = pu_date + timedelta(days=1)
    if hints_enabled:
        print(
            f'HINT: {__name__}: Searching rentals for '
            f'{pu_date.strftime("%m-%d-%Y")} - '
            f'{do_date.strftime("%m-%d-%Y")}.')
    return pu_date, do_date, 0, 1, "sameday"


def nextday(
    test: bool,
    hints_enabled: bool,
    date_pointer: datetime,
) -> tuple[
    datetime,
    datetime,
    int,
    int,
    str,
]:
    pu_date = date_pointer + timedelta(days=1)
    do_date = pu_date + timedelta(days=1)
    if hints_enabled:
        print(
            f'HINT: {__name__}: Searching rentals for '
            f'{pu_date.strftime("%m-%d-%Y")} - {do_date.strftime("%m-%d-%Y")}'
        )
    return pu_date, do_date, 1, 1, "nextday"


def p7rtn1(
    test: bool,
    hints_enabled: bool,
    date_pointer: datetime,
) -> tuple[
    datetime,
    datetime,
    int,
    int,
    str,
]:
    pu_date = date_pointer + timedelta(days=7)
    do_date = pu_date + timedelta(days=1)
    if hints_enabled:
        print(
            f'HINT: {__name__}: Searching rentals for '
            f'{pu_date.strftime("%m-%d-%Y")} - {do_date.strftime("%m-%d-%Y")}'
        )
    return pu_date, do_date, 7, 1, "p7rtn1"


def p14rtn1(
    test: bool,
    hints_enabled: bool,
    date_pointer: datetime
) -> tuple[
    datetime,
    datetime,
    int,
    int,
    str,
]:
    pu_date = date_pointer + timedelta(days=14)
    do_date = pu_date + timedelta(days=1)
    if hints_enabled:
        print(
            f'HINT: {__name__}: Searching rentals for '
            f'{pu_date.strftime("%m-%d-%Y")} - {do_date.strftime("%m-%d-%Y")}'
        )
    return pu_date, do_date, 14, 1, "p14rtn1"


def p30rtn1(
    test: bool,
    hints_enabled: bool,
    date_pointer: datetime,
) -> tuple[
    datetime,
    datetime,
    int,
    int,
    str,
]:
    pu_date = date_pointer + timedelta(days=30)
    do_date = pu_date + timedelta(days=1)
    if hints_enabled:
        print(
            f'HINT: {__name__}: Searching rentals for '
            f'{pu_date.strftime("%m-%d-%Y")} - {do_date.strftime("%m-%d-%Y")}'
        )
    return pu_date, do_date, 30, 1, "p30rtn1"


def main(
    test: bool,
    hints_enabled: bool,
    instance_timestamp: datetime,
) -> tuple[
    tuple[datetime, datetime, int, int, str],
    tuple[datetime, datetime, int, int, str],
    tuple[datetime, datetime, int, int, str],
    tuple[datetime, datetime, int, int, str],
    tuple[datetime, datetime, int, int, str],
]:
    """
    Calculates reservation windows from instance_timestamp and returns
    a tuple of nested tuples. If `test = True`, returning values are
    encased in a list instead of a tuple.

    Parameters:
        test (bool):
        hints_enabled (bool):
        instance_timestamp (datetime):

    Returns:
        tuple: (pu_date dt, do_date dt, adv_rsv, span_rsv, itr_type):
            0) sameday,
            1) nextday,
            2) 7 day advance, 1 day reservation,
            3) 14 day advance, 1 day reservation,
            4) 30 day advance, 1 day reservation,
    """
    rsv_windows = []
    # Same Day
    sameday_tup = sameday(test, hints_enabled, instance_timestamp)
    rsv_windows.append(sameday_tup)
    # Next Day
    nextday_tup = nextday(test, hints_enabled, instance_timestamp)
    rsv_windows.append(nextday_tup)
    # 7 Day Advance
    p7rtn1_tup = p7rtn1(test, hints_enabled, instance_timestamp)
    rsv_windows.append(p7rtn1_tup)
    # 14 Day Advance
    p14rtn1_tup = p14rtn1(test, hints_enabled, instance_timestamp)
    rsv_windows.append(p14rtn1_tup)
    # 30 Day Advance
    p30rtn1_tup = p30rtn1(test, hints_enabled, instance_timestamp)
    rsv_windows.append(p30rtn1_tup)

    if not test:
        return tuple(rsv_windows)
    else:
        return rsv_windows


if __name__ == "__main__":
    test = True
    hints_enabled = False

    instance_timestamp = datetime.now()

    results = main(test, hints_enabled, instance_timestamp)

    for i in results:
        print(i)

    rsv_window = [results.pop(3)]
    
    aria_label_pu = (
    f"Choose {rsv_window[0][1].strftime('%A')}, "
    f"{rsv_window[0][1].strftime('%B')} "
    f"{rsv_window[0][1].strftime('%d')}, "
    f"{rsv_window[0][1].strftime('%Y')}"
    )

    print(aria_label_pu)