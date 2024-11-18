import csv
import sqlite3

def create_database(test: bool, hints_enabled: bool) -> None:
    """
    Creates and establishes database connection

    Args:
        test (bool)
        hints_enabled (bool)

    Returns:
        None
    """
    data_path = 'rental_data.db' if not test else 'test_data.db'
    connection = sqlite3.connect(data_path)
    hints_enabled and print(f'HINT {__name__}: {data_path} accessed.')
    cursor = connection.cursor()

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS rental_prices (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        epoch_ident INT NOT NULL,
        location TEXT NOT NULL,
        service TEXT NOT NULL,
        type TEXT NOT NULL,
        model TEXT NOT NULL,
        pax INTEGER,
        lug INTEGER,
        data_dtm_track TEXT NOT NULL,
        date_scr_date TEXT NOT NULL,
        date_scr_int INTEGER NOT NULL,
        date_rsv_date TEXT NOT NULL,
        date_rsv_int INTEGER NOT NULL,
        adv_rsv INTEGER NOT NULL,
        span_rsv INTEGER NOT NULL,
        daily REAL NOT NUll,
        total REAL NOT NULL,
        unlimited INTEGER NOT NULL
    )
    ''')

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS cheapest_prices(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        epoch_ident INT NOT NULL,
        location TEXT NOT NULL,
        service TEXT NOT NULL,
        type TEXT NOT NULL,
        model TEXT NOT NULL,
        pax INTEGER,
        lug INTEGER,
        data_dtm_track TEXT NOT NULL,
        date_scr_date TEXT NOT NULL,
        date_scr_int INTEGER NOT NULL,
        date_rsv_date TEXT NOT NULL,
        date_rsv_int INTEGER NOT NULL,
        adv_rsv INTEGER NOT NULL,
        span_rsv INTEGER NOT NULL,
        daily REAL NOT NUll,
        total REAL NOT NULL,
        unlimited INTEGER NOT NULL
    )
    ''')

    connection.commit()

    connection.close()
    hints_enabled and print(f'HINT {__name__}: {data_path} closed.')


def db_update(test: bool, hints_enabled: bool, option_tuples_cleaned: list) -> None:
    data_path = 'rental_data.db' if not test else 'test_data.db'
    connection = sqlite3.connect(data_path)
    hints_enabled and print(f'HINT {__name__}: {data_path} accessed.')
    cursor = connection.cursor()

    for option in option_tuples_cleaned:
        option = (*option[:-1], int(option[-1])) # rebuilds tuple with converted boolean into integer

        cursor.execute('''
        INSERT INTO rental_prices (epoch_ident, location, service, type, model, pax, lug, data_dtm_track, date_scr_date, date_scr_int, date_rsv_date, date_rsv_int, adv_rsv, span_rsv, daily, total, unlimited)
        Values (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?);
        ''', option)

    connection.commit()
    connection.close()


def db_export_rental_prices(test: bool, hints_enabled: bool, service: str) -> None:
    data_path = 'rental_data.db' if not test else 'test_data.db'
    connection = sqlite3.connect(data_path)
    cursor = connection.cursor()

    # specific folder
    cursor.execute('SELECT * FROM rental_prices')

    rows = cursor.fetchall()

    column_names = [description[0] for description in cursor.description]

    export_path = f'test/{data_path[:-3]}_export_{service}.csv'
    with open(export_path, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(column_names)
        writer.writerows(rows)

    connection.close()
    hints_enabled and print(f'HINT {__name__}: Data exported to {export_path}')


# Local function only, deletes and updates local database copy
def dl_from_downloaded(test: bool, hints_enabled: bool):
    local_conn = sqlite3.connect("rental_data.db")
    local_cursor = local_conn.cursor()

    downloaded_conn = sqlite3.connect("downloaded_data.db")
    downloaded_cursor = downloaded_conn.cursor()

    tgt_table = "rental_prices"

    local_cursor.execute(f"DROP TABLE IF EXISTS {tgt_table}")

    local_cursor.execute(f'''
    CREATE TABLE IF NOT EXISTS {tgt_table} (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        epoch_ident INT NOT NULL,
        location TEXT NOT NULL,
        service TEXT NOT NULL,
        type TEXT NOT NULL,
        model TEXT NOT NULL,
        pax INTEGER,
        lug INTEGER,
        data_dtm_track TEXT NOT NULL,
        date_scr_date TEXT NOT NULL,
        date_scr_int INTEGER NOT NULL,
        date_rsv_date TEXT NOT NULL,
        date_rsv_int INTEGER NOT NULL,
        adv_rsv INTEGER NOT NULL, 
        daily REAL NOT NUll,
        total REAL NOT NULL,
        unlimited INTEGER NOT NULL
    )
    ''')
    local_conn.commit()

    downloaded_cursor.execute(f"SELECT * FROM {tgt_table}")
    rows = downloaded_cursor.fetchall()

    for row in rows:
        local_cursor.execute(f'''
        INSERT INTO {tgt_table} (id, epoch_ident, service, type, model, pax, lug, data_dtm_track, date_scr_date, date_scr_int, date_rsv_date, date_rsv_int, adv_rsv, span_rsv, daily, total, unlimited)
        Values (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?);
        ''', row)

    local_conn.commit()
    local_conn.close()
    downloaded_conn.close()

    db_export_rental_prices(False, hints_enabled, "Alamo")


def add_location():
    db_path = 'rental_data.db'
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    print("adding column at [2]")
    # cursor.execute("ALTER TABLE rental_prices RENAME TO old_prices;")

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS rental_prices (
            id INTEGER NOT NULL,
            epoch_ident INT NOT NULL,
            location TEXT NOT NULL,
            service TEXT NOT NULL,
            type TEXT NOT NULL,
            model TEXT NOT NULL,
            pax INTEGER,
            lug INTEGER,
            data_dtm_track TEXT NOT NULL,
            date_scr_date TEXT NOT NULL,
            date_scr_int INTEGER NOT NULL,
            date_rsv_date TEXT NOT NULL,
            date_rsv_int INTEGER NOT NULL,
            adv_rsv INTEGER NOT NULL,
            daily REAL NOT NUll,
            total REAL NOT NULL,
            unlimited INTEGER NOT NULL
        );
    """)

    cursor.execute("""
        INSERT INTO rental_prices (id, epoch_ident, location, service, type, model, pax, lug, data_dtm_track, date_scr_date, date_scr_int, date_rsv_date, date_rsv_int, adv_rsv, daily, total, unlimited)
        SELECT id, epoch_ident, "SNA", service, type, model, pax, lug, data_dtm_track, date_scr_date, date_scr_int, date_rsv_date, date_rsv_int, adv_rsv, daily, total, unlimited
        FROM old_prices;
    """)

    cursor.execute("DROP TABLE old_prices;")

    conn.commit()
    conn.close()
    print('location added')

    db_export_rental_prices(False, hints_enabled, "Alamo")


# forceupdate
def forceupdate():
    # db_path = 'rental_data.db'
    # conn = sqlite3.connect(db_path)
    # cursor = conn.cursor()

    # print('changing adv_rsv to 0s...')

    # cursor.execute('UPDATE rental_prices SET adv_rsv = 0;')

    # conn.commit()
    # conn.close()
    # print('adv changed!')

    # db_export_rental_prices(False, hints_enabled, "Alamo")

    db_path = 'rental_data.db'
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    print("span_rsv")

    cursor.execute("ALTER TABLE rental_prices RENAME TO old_prices;")

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS rental_prices (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            epoch_ident INT NOT NULL,
            location TEXT NOT NULL,
            service TEXT NOT NULL,
            type TEXT NOT NULL,
            model TEXT NOT NULL,
            pax INTEGER,
            lug INTEGER,
            data_dtm_track TEXT NOT NULL,
            date_scr_date TEXT NOT NULL,
            date_scr_int INTEGER NOT NULL,
            date_rsv_date TEXT NOT NULL,
            date_rsv_int INTEGER NOT NULL,
            adv_rsv INTEGER NOT NULL,
            span_rsv INTEGER NOT NULL,
            daily REAL NOT NUll,
            total REAL NOT NULL,
            unlimited INTEGER NOT NULL
        );
    """)

    cursor.execute("""
        INSERT INTO rental_prices (id, epoch_ident, location, service, type, model, pax, lug, data_dtm_track, date_scr_date, date_scr_int, date_rsv_date, date_rsv_int, adv_rsv, span_rsv, daily, total, unlimited)
        SELECT id, epoch_ident, location, service, type, model, pax, lug, data_dtm_track, date_scr_date, date_scr_int, date_rsv_date, date_rsv_int, adv_rsv, 1, daily, total, unlimited
        FROM old_prices;
    """)

    # cursor.execute("DROP TABLE old_prices;")

    conn.commit()
    conn.close()
    print('column added')

    db_export_rental_prices(False, hints_enabled, "Alamo")


if __name__ == "__main__":
    test = False
    hints_enabled = True
    service = "Alamo"

    while True:
        choice = input("1) Create database\n2) Export rental_prices table\n3) Update local database\nEnter Choice: ")
        if choice == "1":
            create_database(test, hints_enabled)
            break
        elif choice == "2":
            db_export_rental_prices(test, hints_enabled, service)
            break
        elif choice == "3":
            dl_from_downloaded(test, hints_enabled)
            break
        elif choice == "location":
            add_location()
            break
        elif choice == "forceupdate":
            forceupdate()
        else:
            print(f'{choice} was an invalid choice. Enter again.')


"""
Things I want to know:
- how far in advance generally gets you the cheapest rental cost for single day
- how far in advance generally gets you the cheapest rental cost for 3 day weekend
- how many times does a 3 day weekend cost change throughout the week
- which day on average was the chepeast 1 day rental
- which weekend had the cheapest rental
- each service's cheapest rental for each type
- 

# example of how to iterate each of objects to place into the database
# Insert each tuple into the database
for rental_data in rental_data_array:
    cursor.execute('''
    INSERT INTO rental_records (rental_service, rental_type, price, rental_date)
    VALUES (?, ?, ?, ?);
    ''', rental_data)  # Pass each tuple as parameters
"""