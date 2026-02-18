import sqlite3
from datetime import datetime
from database import get_connection

def get_required_input(prompt):
    while True:
        value = input(prompt)
        if value.strip() != "":
            return value
        else:
            print("This field is required. Please enter a value.")

def log_call():
    print("\n--- Log New Call ---")

    caller_name = get_required_input("Caller name: ")
    caller_phone = get_required_input("Caller phone number: ")
    caller_address = get_required_input("Caller address: ")
    issue = get_required_input("Issue: ")
    troubleshooting = get_required_input("Troubleshooting steps taken: ")
    resolution = get_required_input("Resolution: ")
    agent_name = get_required_input("Agent name: ")

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

def search_calls():
    print("\n--- Search Calls ---")
    print("1. Search by caller name")
    print("2. Search by phone number")
    print("3. Search by issue")

    choice = input("\nSearch by: ")

    if choice == "1":
        term = input("Enter caller name: ")
        column = "caller_name"
    elif choice == "2":
        term = input("Enter phone number: ")
        column = "caller_phone"
    elif choice == "3":
        term = input("Enter issue keyword: ")
        column = "issue"
    else:
        print("Invalid Choice.")
        return

    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute(f"""
        SELECT id, date, time, caller_name, issue, resolution
        FROM calls
        WHERE {column} LIKE ?
        ORDER BY id DESC
    """, (f"%{term}%",))

    rows = cursor.fetchall()
    connection.close()

    if len(rows) == 0:
        print("No matching calls found.")
    else:
        for row in rows:
            print(f"\nID: {row[0]} | {row[1]} {row[2]}")
            print(f"Caller: {row[3]}")
            print(f"Issue: {row[4]}")
            print(f"Resolution: {row[5]}")
            print("---")

def view_call_detail():
    print("\n--- View Call Detail ---")
    call_id = input("Enter call ID: ")

    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute("""
        SELECT * FROM calls WHERE id = ?
    """, (call_id,))
    
    row = cursor.fetchone()
    connection.close()

    if row is None:
        print("No call found with that ID.")
    else:
        print(f"\n--- Call Id: {row[0]} ---")
        print(f"Date: {row[1]}")
        print(f"Time: {row[2]}")
        print(f"Caller Name: {row[3]}")
        print(f"Phone: {row[4]}")
        print(f"Address: {row[5]}")
        print(f"Issue: {row[6]}")
        print(f"Troubleshooting: {row[7]}")
        print(f"Resolution: {row[8]}")
        print(f"Agent: {row[9]}")

def log_call_db(caller_name, caller_phone, caller_address, issue, troubleshooting, resolution, agent_name):
    from datetime import datetime
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
    
def get_recent_calls():
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
    return rows

def get_call_by_id(call_id):
    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute("SELECT * FROM calls WHERE id = ?", (call_id,))

    row = cursor.fetchone()
    connection.close()
    return row

def search_calls_db(column, term):
    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute(f"""
        SELECT id, date, time, caller_name, issue, resolution
        FROM calls
        WHERE {column} LIKE ?
        ORDER BY id DESC
    """, (f"%{term}%",))

    rows = cursor.fetchall()
    connection.close()
    return rows




