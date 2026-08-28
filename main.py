from logic import (
    delete_record,
    filter_records_by_status,
    get_next_id,
    mark_record_complete,
    search_records_by_title,
)
from storage import load_records, save_records


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


def handle_mark_complete(records):
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
        return


def main():
    records = load_records()
    while True:
        print("-- Main Menu --")
        print("1: Add a record")
        print("2: View records")
        print("3: Mark a record complete")
        print("4: Delete a record")
        print("5: Search records by title")
        print("6: Filter records by status")
        print("7: Quit")
        choice = input("Enter your choice: (1-7)")

        if choice == "1":
            next_id = get_next_id(records)
            record = create_record(next_id)
            records.append(record)
            save_records(records)
            print("Record added successfully.")
        elif choice == "2":
            view_records(records)
        elif choice == "3":
            handle_mark_complete(records)
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
            status = input("Search for a status:")
            matching_records = filter_records_by_status(records, status)
            view_records(matching_records)
        elif choice == "7":
            break
        else:
            print("Invalid choice. Please enter 1, 2, 3, 4, 5, 6, or 7.")


if __name__ == "__main__":
    main()
