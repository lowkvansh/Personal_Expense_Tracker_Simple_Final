# Personal Expense Tracker

Simple student-style CLI project for the VITyarthi Python Essentials evaluated project.

## Course modules used
- Module 2 - Python Fundamentals
- Module 3 - Python Operators
- Module 4 - Input and Output operations in Python
- Module 6 - Type Conversion in Python
- Module 7 - Core Data Structures in Python
- Module 8 - Control Flow Statements in Python
- Module 9 - Functions in Python

## Features
Register, Login, Exit, Logout, Add/View/Search/Update/Delete expenses, total, average, category summary, monthly summary and text-file storage.

## Run
`python main.py`

## Test
`python -m unittest discover -s tests -v`

## Main code
Most/all application logic is intentionally in `main.py` for easy student-level understanding and evaluation.

## Storage
Basic `.txt` files are used with `open()`, `read()` and `write()`. No CSV, database or third-party package is used.

## Educational note
Passwords are stored as plain text only for this beginner educational project. This is not a production authentication design.
