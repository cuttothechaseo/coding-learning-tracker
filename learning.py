import json

records = [
    {"id": 69, "title": "hi", "status": "present", "concepts": ["yea", "ok", "so"]}
]

# Print list
print(records)

# Print type of list
print(type(records))

# Print type of first item in list
first_item = records[0]
print(type(first_item))

# Print value of title in dict
print(records[0]["title"])

# open json file in write mode containing above records
with open("learning_data.json", "w") as file:
    json.dump(records, file, indent=4)

# open json file in read mode containing above records
with open("learning_data.json", "r") as file:
    loaded_records = json.load(file)

print(loaded_records)
print(type(loaded_records))
first_item_loaded_records = loaded_records[0]
print(type(first_item_loaded_records))
