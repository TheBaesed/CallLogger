import sqlite3

def get_connection():
    connection = sqlite3.connect("calls.db")
    return connection

def create_table():
    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS calls (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        date TEXT,
        time TEXT,
        caller_name TEXT,
        caller_phone TEXT,
        caller_address TEXT,
        issue TEXT,
        troubleshooting TEXT,
        resolution TEXT,
        agent_name TEXT
        )
    """)

    connection.commit()
    connection.close()
    print("Database ready.")

create_table()