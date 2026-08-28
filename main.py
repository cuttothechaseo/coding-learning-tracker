import json


def load_records():
    try:
        with open("records.json", "r") as file:
            loaded_records = json.load(file)
    except FileNotFoundError:
        return []

    return loaded_records


def create_record(record_id):
    project_input = input("Input Project:")
    biggest_lesson = input("What was the biggest lesson?")
    next_learning_step = input("What is the next learning step?")
    concept_input = input("What concepts did you learn?")
    result_dict = {
        "id": record_id,
        "title": project_input,
        "status": "in progress",
        "concepts": [concept_input],
        "biggest_lesson": biggest_lesson,
        "next_step": next_learning_step,
    }

    return result_dict


def view_records(records):
    if records == []:
        print("No records found.")

    for record in records:
        print(record["id"], record["title"], record["status"])


def find_record_by_id(records, record_id):
    for record in records:
        if record["id"] == record_id:
            return record

    return None


def mark_record_complete(records, record_id):
    record = find_record_by_id(records, record_id)

    if record is None:
        return False
    else:
        record["status"] = "complete"
        return True


def get_next_id(records):
    highest_id = 0
    for record in records:
        highest_id = max(highest_id, record["id"])

    return highest_id + 1


def save_records(records):
    with open("records.json", "w") as file:
        json.dump(records, file, indent=4)


def main():
    records = load_records()
    while True:
        print("-- Main Menu --")
        print("1: Add a record")
        print("2: View records")
        print("3: Quit")
        choice = input("Enter your choice: (1-3)")

        if choice == "1":
            next_id = get_next_id(records)
            record = create_record(next_id)
            records.append(record)
            save_records(records)
            print("Record added successfully.")
        elif choice == "2":
            view_records(records)
        elif choice == "3":
            break
        else:
            print("Invalid choice. Please enter 1, 2, or 3.")


if __name__ == "__main__":
    main()
