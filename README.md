# Coding Learning Tracker

A terminal-based Python application for recording coding projects, what was
learned from them, and what to practice next. Records are saved to JSON and
loaded again on later runs.

## Features

- Add and view learning records
- Assign stable numeric IDs
- Mark records complete
- Delete records by ID
- Search titles with case-insensitive partial matching
- Filter records by status
- Save changes to `records.json`
- Handle missing, empty, or malformed data files without crashing

Each record contains an ID, title, status, concepts list, biggest lesson, and
next learning step.

## Project Structure

- `main.py` handles the menu, terminal input, output, and orchestration.
- `logic.py` contains record lookup, mutation, search, filtering, and ID logic.
- `storage.py` loads and saves JSON data.
- `records.json` stores the persistent records.
- `learning.py` contains the small file and JSON exercise completed before the
  main project.

## Run the Program

The project uses Python's standard library and has no third-party dependencies.

```bash
python3 main.py
```

## Learning Focus

This project practices the complete data flow:

```text
terminal input → Python data → program logic → JSON storage → loaded Python data
```

It also reinforces CRUD operations, lists of dictionaries, mutation, return
values, validation, stable IDs, searching, filtering, and separating a program
into modules when clear responsibilities emerge.
