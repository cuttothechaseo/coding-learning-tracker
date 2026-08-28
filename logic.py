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


def search_records_by_title(records, search_term):
    matches = []
    search_term = search_term.lower()

    for record in records:
        if search_term in record["title"].lower():
            matches.append(record)

    return matches


def filter_records_by_status(records, status):
    matches = []
    status = status.lower()

    for record in records:
        if status == record["status"].lower():
            matches.append(record)

    return matches
