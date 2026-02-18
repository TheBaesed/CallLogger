# EPB Call Logger

A Python application built to replace handwritten call notes for EPB Fiber Optics tech support agents.

## What It Does

- Log customer support calls with caller info, issue, troubleshooting steps, and resolution
- View the 10 most recent calls
- Search calls by caller name, phone number, or issue keyword
- View full detail of any call by ID
- All data stored locally in a SQLite database

## Built With

- Python 3.12+
- SQLite3 (built into Python)
- Flask (coming soon)

## How To Run

1. Make sure Python is installed
2. Clone this repository
3. Navigate to the project folder
4. Run the following command:
```
python main.py
```

## Project Structure

- `main.py` - Entry point and menu navigation
- `database.py` - Database connection and table setup
- `calls.py` - All call logging, viewing, and search logic

## Author

Chris Lisi - EPB Fiber Optics Tech Support
