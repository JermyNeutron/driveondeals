from datetime import datetime
import sqlite3

# find referencing


def get_epochs(db_path: str):
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    cursor.execute("""
        SELECT DISTINCT epoch_ident
        FROM rental_prices;        
    """)
    results = cursor.fetchall()
    conn.close()

    unique_epoch_idents = [row[0] for row in results]
    return unique_epoch_idents


def get_avg(db_path, ident):
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    cursor.execute("""
    SELECT epoch_ident, AVG(daily) AS avg_daily, COUNT(daily) as entry_count
    FROM rental_prices
    WHERE type in ()
    AND epoch_ident = ?
    GROUP BY epoch_ident;
    """, (ident,))

    result = cursor.fetchone()
    conn.close()
    print(f"Returning {datetime.fromtimestamp(result[0]).strftime('%Y-%m-%d')}, {result[1]:.3f}, {result[2]}")


def main():
    db_path = "rental_data.db"
    epoch_idents = get_epochs(db_path)
    for i in epoch_idents:
        get_avg(db_path, i)


if __name__ == '__main__':
    main()