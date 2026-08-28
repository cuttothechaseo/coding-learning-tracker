# Coding Learning Tracker Project

## Purpose

Build a terminal-based Python application for recording completed coding
projects and the lessons learned from them. The main learning goal is to
understand how data moves from terminal input, through program logic, into
structured Python data, then into JSON storage and back again on a later run.

The project should remain small and understandable. The record structure and
program organization should grow only when the current feature creates a clear
need.

## Version 1 Scope

A complete first version should support:

- Adding a learning record with a stable ID, title, status, and a small set of
  useful learning details
- Viewing all saved records
- Updating a record or marking it complete
- Deleting a record
- Searching records by title
- Filtering records by status or concept
- Saving records to JSON
- Loading saved records when the program starts

The exact record fields will be chosen before implementation and kept minimal.
Classes, a database, a graphical interface, user accounts, and extensive
reporting are outside Version 1.

## Concepts Reinforced

- Functions with clear responsibilities
- Parameters, arguments, local variables, and return values
- Lists and dictionaries, including mutation and data shape
- Loops, conditionals, and input validation
- Multiple helper functions coordinated by `main()`
- Reading tracebacks and debugging state changes

## New Concepts

- Reading from and writing to files
- JSON serialization and deserialization
- Persistent state across separate program runs
- CRUD operations: create, read, update, and delete
- Stable record IDs
- Searching and filtering collections of dictionaries
- Handling missing, empty, or malformed data files
- Separating storage, program logic, and terminal interaction when those
  boundaries become useful

## Development Progression

### 1. Choose One Record Shape

Agree on a small dictionary structure and create one example record in memory.
Be able to identify the type and purpose of every field.

### 2. Add and View Records in Memory

Store records in a collection, add a record through terminal input, and display
the records clearly. Trace each value from input to the stored dictionary.

### 3. Save and Load JSON

Write the record collection to a JSON file and load it when the program starts.
Confirm that the loaded Python data has the expected types and shape.

### 4. Identify and Change One Record

Assign stable IDs, then use an ID to update a record, mark it complete, or
delete it without depending on list position.

### 5. Search and Filter

Search records by title and filter them by one useful field such as status or
concept.

### 6. Refine the Program Structure

Add validation and basic file-error handling. Split storage or record logic
into separate modules only after the code has developed clear, repeated
responsibilities.

## Definition of Success

The project is successful when the learner can build and explain a coherent
terminal application that preserves records between runs and supports the
bounded Version 1 operations. In particular, the learner should be able to
trace one record from terminal input to a Python dictionary, through the
collection and JSON file, and back into the program with its identity and data
intact.
