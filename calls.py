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


