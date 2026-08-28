import json


def load_records():
    try:
        with open("records.json", "r") as file:
            loaded_records = json.load(file)
    except FileNotFoundError:
        return []

    return loaded_records


def save_records(records):
    with open("records.json", "w") as file:
        json.dump(records, file, indent=4)
