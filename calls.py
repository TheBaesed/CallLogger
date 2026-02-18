import sqlite3
from datetime import datetime
from database import get_connection

def log_call():
    print("\n--- Log New Call ---")

    caller_name = input("Caller name: ")
    caller_phone = input("Caller phone number: ")
    caller_address = input("Caller address: ")
    issue = input("Issue: ")
    troubleshooting = input("Troubleshooting steps taken: ")
    resolution = input("Resolution: ")
    agent_name = input("Agent name: ")

    now = datetime.now()
    date = now.strftime("%Y-%m-%d")
    time = now.strftime("%H:%M:%S")

    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute("""
        INSERT INTO calls (date, time, caller_name, caller_phone, caller_address, issue, troubleshooting, resolution, agent_name)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
    """, (date, time, caller_name, caller_phone, caller_address, issue, troubleshooting, resolution, agent_name))
        
    connection.commit()
    connection.close()

def view_recent_calls():
    print("\n--- Recent Calls ---")

    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute("""
        SELECT id, date, time, caller_name, issue
        FROM calls
        ORDER BY id DESC
        LIMIT 10
        """)
        
    rows = cursor.fetchall()
    connection.close()
        
    if len(rows) == 0:
        print("No calls logged yet.")
    else:
        for row in rows:
            print(f"\nID: {row[0]} | {row[1]} {row[2]}")
            print(f"Caller: {row[3]}")
            print(f"Issue: {row[4]}")
            print("---")


