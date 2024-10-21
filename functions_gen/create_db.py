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

    connection = sqlite3.connect('rental_data.db')
    hints_enabled and print(f'HINT {__name__}: rental_data.db accessed.')
    cursor = connection.cursor()

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS rental_prices (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
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
        total REAL NOT NULL    
    )
    ''')

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS cheapest_prices(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
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
        total REAL NOT NULL 
    )
    ''')

    connection.commit()

    connection.close()
    hints_enabled and print(f'HINT {__name__}: rental_data.db closed.')


def db_update(test: bool, hints_enabled: bool, option_tuples_cleaned: list) -> None:
    connection = sqlite3.connect('rental_data.db')
    hints_enabled and print(f'HINT {__name__}: rental_data.db accessed.')
    cursor = connection.cursor()

    for option in option_tuples_cleaned:
        cursor.execute('''
            INSERT INTO rental_prices (service, type, model, pax, lug, data_dtm_track, date_scr_date, date_scr_int, date_rsv_date, date_rsv_int, adv_rsv, daily, total)
            Values (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?);
        ''', option)

    connection.commit()
    connection.close()


def db_export_rental_prices(test: bool, hints_enabled: bool, service: str) -> None:
    connection = sqlite3.connect('rental_data.db')
    cursor = connection.cursor()

    # specific folder
    cursor.execute('SELECT * FROM rental_prices')

    rows = cursor.fetchall()

    column_names = [description[0] for description in cursor.description]

    export_path = f'test/rental_prices_export_{service}.csv' if test else f'temp/rental_prices_export_{service}.csv'
    with open(export_path, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(column_names)
        writer.writerows(rows)

    connection.close()
    hints_enabled and print(f'HINT {__name__}: Data exported to {export_path}')


if __name__ == "__main__":
    test = True
    hints_enabled = True

    create_database(test, hints_enabled)
    # db_export_rental_prices(test, hints_enabled)


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