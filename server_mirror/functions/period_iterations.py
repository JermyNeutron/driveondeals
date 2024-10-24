from datetime import datetime, date, timedelta

# Custom texts
checkmark = "\u2713"
xmark = "\u2715"


def dx1rtn(test: bool, hints_enabled: bool, date_pointer: datetime) -> datetime:
    return_datetime = date_pointer + timedelta(days=1)
    return return_datetime


def dx3rtn(test: bool, hints_enabled: bool, date_pointer: datetime) -> tuple:

    
    def find_start(test: bool, hints_enabled: bool, date_pointer: datetime) -> datetime:
        date_start = date_pointer
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


def dx7rtn(test: bool, hints_enabled: bool, date_pointer: datetime) -> datetime:
    return_date = date_pointer + timedelta(days=7)
    return return_date


def dx14rtn(test: bool, hints_enabled: bool, date_pointer: datetime) -> datetime:
    return_date = date_pointer + timedelta(days=14)
    return return_date


def dx30rtn(test: bool, hints_enabled: bool, date_pointer: datetime) -> datetime:
    return_date = date_pointer + timedelta(days=30)
    return return_date


if __name__ == "__main__":
    test = True
    hints_enabled = True

    dx3rtn(test, hints_enabled, datetime.now())