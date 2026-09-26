import json
from pathlib import Path

DATA_FILE = Path(__file__).parent / "expenses.json"


def save_data(expenses):
    with open(DATA_FILE, "w") as file:
        json.dump(expenses, file, indent=4)
    print("Data saved successfully!")

def load_data():
    try:
        with open(DATA_FILE, "r") as file:
            data = json.load(file)
            return data
    except FileNotFoundError:
        print("No saved expenses found. Starting with an empty list.")
        return []
    except json.JSONDecodeError:
        print("Saved data is corrupted. Starting with an empty list.")
        return []