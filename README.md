# Personal Expense Tracker

Personal Expense Tracker is a simple command-line Python application used to record day-to-day expenses

This program enables the user to create a new account, log in, and manage their own expense data. In addition, it allows searching, viewing, adding, updating and deleting expenses, and calculating total expenses, average expenses, and expenses by category and month

The project is designed to be simple and easy to use through the terminal

## Features

- Creating a new user account

- Login using a username and password

- Adding a new expense

- Viewing all saved expenses

- Search expenses by category or date

- Updating an existing expense

- Deleting an expense

- Total expenses calculation

- Average expense calculation

- Show spending by category

- Show spending by month

- Store data locally using text files
  
- Logout 

## How the Program Works

The program opens a menu in the terminal where the user can choose between registering a new account, logging in, or exiting the application

After logging in, the user receives an expense menu and from this menu, the user can add and manage expenses.

Every expense contains information such as the date, category, amount, and description. The program saves this information in text files so that the records remain available when the application is opened again.

## Expense Information

Each expense contains:

- Date

- Category

- Amount of money

- Description


For example:

Date: 25-09-2026  

Category: Food  

Amount: 250  

Description: Lunch


## Project Structure

```

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

```

The application code is mainly written in the `main.py` file


The data folder is where user information is stored


The tests folder contains a few basic tests for checking if some calculations work properly or not

## Requirements

The project requires:

```
- Python 3
- A terminal or command prompt
```

No additional python packages are required 

## How to Run

Open a terminal in the project folder and run:
```
python main.py
```
The application will then display the main menu

## Example

## PERSONAL EXPENSE TRACKER

1. Register

2. Login

3. Exit

Enter your choice:

After logging in, the user receives an expense menu:

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

The program stores data with the help of local text files.

The user data is stored in:
```
data/users.txt
```
While the expense data is stored in text files which are in the data folder, it is a simple project and means that no database system is required

## Testing

The project contains a few tests for checking if all calculations work properly

To run the tests, use:

```
python -m unittest discover -s tests -v
```

It will execute all the tests and show the results such as total and average spending. 

## Limitations

This is a simple command-line application created for learning and educational purposes

It is not suitable for production because the user data is not protected, and the program does not have a database

Also, passwords are stored in plain text meaning that it is insecure and not suitable for real authentication system or personal information

## Future Improvements

Some possible improvements for the future include:

- adding a graphical user interface

- adding charts for expenses

- adding budget limits

- adding export options

- using database for storing information

- improve password security

- adding more detailed financial reports

## Author
Personal Expense Tracker
