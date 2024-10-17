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


if __name__ == "__main__":
    test = True
    hints_enabled = True

    create_database(test, hints_enabled)


"""
Things I want to know:
- how far in advance generally gets you the cheapest rental cost for single day
- how far in advance generally gets you the cheapest rental cost for 3 day weekend
- how many times does a 3 day weekend cost change throughout the week
- 
"""