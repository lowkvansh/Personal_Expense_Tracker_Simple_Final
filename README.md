# Personal Expense Tracker

Personal Expense Tracker is a simple command-line Python application for keeping track of daily expenses.

The program allows users to create an account, log in, and manage their personal expense records. Users can add, view, search, update, and delete expenses. The application also provides basic summaries such as total spending, average expense, spending by category, and spending by month.

The project is designed to be simple and easy to use through the terminal.

## Features

- Create a new user account
- Login using a username and password
- Add a new expense
- View all saved expenses
- Search expenses by category or date
- Update an existing expense
- Delete an expense
- Calculate total expenses
- Calculate average expense
- View spending by category
- View spending by month
- Logout from the account
- Store information locally using text files

## How the Program Works

When the program starts, the user is shown a main menu. The user can choose to register a new account, log in to an existing account, or exit the program.

After logging in, the user gets access to the expense menu. From this menu, the user can add and manage expenses.

Each expense contains information such as the date, category, amount, and description. The program saves this information in text files so that the records remain available when the application is opened again.

## Expense Information

Each expense contains:

- Date
- Category
- Amount
- Description

For example:

Date: 25-09-2026  
Category: Food  
Amount: 250  
Description: Lunch

## Project Structure

Personal_Expense_Tracker/
│
├── main.py
├── README.md
├── requirements.txt
├── statement.md
├── report.md
├── report.pdf
│
├── data/
│   ├── users.txt
│   └── expenses.txt
│
├── tests/
│   └── test_main.py
│
└── docs/
    └── diagrams.md
    
The main application is contained in `main.py`.

The `data` folder stores user and expense information.

The `tests` folder contains basic tests for checking some of the calculations used by the application.

## Requirements

The project requires:

- Python 3
- A terminal or command prompt

No additional Python packages are required.

## How to Run

Open a terminal in the project folder and run:

python main.py

The application will then display the main menu.

## Example

## PERSONAL EXPENSE TRACKER

1. Register
2. Login
3. Exit

Enter your choice:

After logging in, the expense menu is displayed:

## EXPENSE MENU

1. Add Expense
2. View Expenses
3. Search Expenses
4. Update Expense
5. Delete Expense
6. Show Summary
7. Logout

Enter your choice:

## Data Storage

The application uses simple text files to store information locally.

User information is stored in:

data/users.txt

Expense information is stored in text files inside the `data` folder.

This keeps the project lightweight and means that no database setup is required.

## Testing

Basic tests are included in the `tests` folder.

To run the tests, use:

python -m unittest discover -s tests -v

The tests check basic expense calculations such as total and average spending.

## Limitations

This is a simple command-line application intended for learning and personal use.

The application does not use a database or an online account system. User data is stored locally in text files.

Passwords are stored as plain text, so this project should not be used as a real authentication system for sensitive information.

## Future Improvements

Some possible improvements for the future include:

- Add a graphical user interface
- Add charts for spending patterns
- Add budget limits
- Add export options
- Use a database for storing information
- Improve password security
- Add more detailed financial reports

## Author

A Python-based command-line application for managing everyday expenses
