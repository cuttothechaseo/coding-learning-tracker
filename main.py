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


def delete_record(records, record_id):
    record = find_record_by_id(records, record_id)
    if record is None:
        return False
    else:
        records.remove(record)
        return True


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


def search_records_by_title(records, search_term):
    matches = []
    search_term = search_term.lower()

    for record in records:
        if search_term in record["title"].lower():
            matches.append(record)

    return matches


def main():
    records = load_records()
    while True:
        print("-- Main Menu --")
        print("1: Add a record")
        print("2: View records")
        print("3: Mark a record complete")
        print("4: Delete a record")
        print("5: Search records by title")
        print("6: Quit")
        choice = input("Enter your choice: (1-6)")

        if choice == "1":
            next_id = get_next_id(records)
            record = create_record(next_id)
            records.append(record)
            save_records(records)
            print("Record added successfully.")
        elif choice == "2":
            view_records(records)
        elif choice == "3":
            try:
                record_id = int(input("Input record ID you want to change:"))
                result = mark_record_complete(records, record_id)
                if result == True:
                    save_records(records)
                    print("Status updated successfully.")
                elif result == False:
                    print("ID was not found.")
            except ValueError:
                print("Input a valid number")
                continue
        elif choice == "4":
            try:
                record_id = int(input("Input record ID you want to delete:"))
                result = delete_record(records, record_id)
                if result == True:
                    save_records(records)
                    print("Record deleted successfully.")
                elif result == False:
                    print("ID was not found.")
            except ValueError:
                print("Input a valid number")
                continue
        elif choice == "5":
            search_term = input("Input a search term:")
            matching_records = search_records_by_title(records, search_term)
            view_records(matching_records)
        elif choice == "6":
            break
        else:
            print("Invalid choice. Please enter 1, 2, 3, 4, 5, or 6.")


if __name__ == "__main__":
    main()
