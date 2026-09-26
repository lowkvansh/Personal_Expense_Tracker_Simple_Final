# Personal Expense Tracker - Python Essentials Project
# Modules: 2 Fundamentals, 3 Operators, 4 Input/Output,
# 6 Type Conversion, 7 Data Structures, 8 Control Flow, 9 Functions

def create_file(filename):
    file = open(filename, "a")
    file.close()

def save_users(users):
    file = open("data/users.txt", "w")
    for username, password in users.items():
        file.write(username + "|" + password + "\n")
    file.close()

def load_users():
    users = {}
    create_file("data/users.txt")
    file = open("data/users.txt", "r")
    for line in file:
        line = line.strip()
        if line != "":
            parts = line.split("|")
            if len(parts) == 2:
                users[parts[0]] = parts[1]
    file.close()
    return users

def save_expenses(username, expenses):
    filename = "data/" + username + "_expenses.txt"
    file = open(filename, "w")
    for expense in expenses:
        file.write(
            expense["date"] + "|" + expense["category"] + "|" +
            str(expense["amount"]) + "|" + expense["description"] + "\n"
        )
    file.close()

def load_expenses(username):
    filename = "data/" + username + "_expenses.txt"
    create_file(filename)
    expenses = []
    file = open(filename, "r")
    for line in file:
        line = line.strip()
        if line != "":
            parts = line.split("|")
            if len(parts) == 4:
                try:
                    expenses.append({
                        "date": parts[0],
                        "category": parts[1],
                        "amount": float(parts[2]),
                        "description": parts[3]
                    })
                except ValueError:
                    pass
    file.close()
    return expenses

def register(users):
    print("\n--- REGISTER ---")
    username = input("Create username: ").strip()
    password = input("Create password: ")
    if username == "" or password == "":
        print("Username and password cannot be empty.")
    elif "|" in username or "|" in password:
        print("The | symbol cannot be used.")
    elif username in users:
        print("Username already exists.")
    else:
        users[username] = password
        save_users(users)
        print("Registration successful.")

def login(users):
    print("\n--- LOGIN ---")
    username = input("Username: ").strip()
    password = input("Password: ")
    if username in users and users[username] == password:
        print("Login successful.")
        return username
    print("Invalid username or password.")
    return ""

def get_amount():
    while True:
        value = input("Amount: ")
        try:
            amount = float(value)
            if amount > 0:
                return amount
            print("Amount must be greater than 0.")
        except ValueError:
            print("Please enter a valid number.")

def get_category():
    categories = ("Food", "Travel", "Bills", "Shopping", "Education", "Health", "Other")
    print("\nCategories:")
    for number in range(len(categories)):
        print(str(number + 1) + ". " + categories[number])
    while True:
        choice = input("Choose category: ")
        if choice.isdigit():
            number = int(choice)
            if 1 <= number <= len(categories):
                return categories[number - 1]
        print("Please choose a valid category number.")

def add_expense(expenses):
    print("\n--- ADD EXPENSE ---")
    expense = {
        "date": input("Date (YYYY-MM-DD): ").strip(),
        "category": get_category(),
        "amount": get_amount(),
        "description": input("Description: ").strip()
    }
    expenses.append(expense)
    print("Expense added successfully.")

def display_expenses(expenses):
    print("\n--- EXPENSES ---")
    if len(expenses) == 0:
        print("No expenses found.")
        return
    print("No.  Date        Category      Amount       Description")
    print("-" * 65)
    for number in range(len(expenses)):
        expense = expenses[number]
        print(str(number + 1) + "    " + expense["date"] + "   " +
              expense["category"] + "      " +
              format(expense["amount"], ".2f") + "       " +
              expense["description"])

def search_expenses(expenses):
    keyword = input("Enter search keyword: ").lower()
    results = []
    for expense in expenses:
        text = (expense["date"] + " " + expense["category"] + " " +
                expense["description"]).lower()
        if keyword in text:
            results.append(expense)
    display_expenses(results)

def update_expense(expenses):
    display_expenses(expenses)
    if len(expenses) == 0:
        return
    choice = input("Enter expense number to update: ")
    if not choice.isdigit():
        print("Invalid number.")
        return
    number = int(choice)
    if number < 1 or number > len(expenses):
        print("Expense not found.")
        return
    index = number - 1
    expenses[index]["date"] = input("Date (YYYY-MM-DD): ").strip()
    expenses[index]["category"] = get_category()
    expenses[index]["amount"] = get_amount()
    expenses[index]["description"] = input("Description: ").strip()
    print("Expense updated successfully.")

def delete_expense(expenses):
    display_expenses(expenses)
    if len(expenses) == 0:
        return
    choice = input("Enter expense number to delete: ")
    if not choice.isdigit():
        print("Invalid number.")
        return
    number = int(choice)
    if 1 <= number <= len(expenses):
        del expenses[number - 1]
        print("Expense deleted successfully.")
    else:
        print("Expense not found.")

def calculate_total(expenses):
    total = 0
    for expense in expenses:
        total = total + expense["amount"]
    return total

def calculate_average(expenses):
    if len(expenses) == 0:
        return 0
    return calculate_total(expenses) / len(expenses)

def category_summary(expenses):
    totals = {}
    for expense in expenses:
        category = expense["category"]
        if category not in totals:
            totals[category] = 0
        totals[category] = totals[category] + expense["amount"]
    print("\n--- CATEGORY SUMMARY ---")
    if len(totals) == 0:
        print("No expenses found.")
    else:
        for category in totals:
            print(category + ": " + format(totals[category], ".2f"))

def monthly_summary(expenses):
    month = input("Enter month (YYYY-MM): ").strip()
    total = 0
    for expense in expenses:
        if expense["date"].startswith(month):
            total = total + expense["amount"]
    print("Spending in " + month + ": " + format(total, ".2f"))

def show_summary(expenses):
    print("\n--- SUMMARY ---")
    print("Total spending: " + format(calculate_total(expenses), ".2f"))
    print("Average expense: " + format(calculate_average(expenses), ".2f"))
    category_summary(expenses)

def expense_menu(username):
    expenses = load_expenses(username)
    while True:
        print("\n" + "=" * 45)
        print("PERSONAL EXPENSE TRACKER")
        print("Logged in as: " + username)
        print("=" * 45)
        print("1. Add expense")
        print("2. View expenses")
        print("3. Search expenses")
        print("4. Update expense")
        print("5. Delete expense")
        print("6. Show summary")
        print("7. Monthly summary")
        print("8. Save expenses")
        print("9. Logout")
        choice = input("Enter choice: ")
        if choice == "1":
            add_expense(expenses)
            save_expenses(username, expenses)
        elif choice == "2":
            display_expenses(expenses)
        elif choice == "3":
            search_expenses(expenses)
        elif choice == "4":
            update_expense(expenses)
            save_expenses(username, expenses)
        elif choice == "5":
            delete_expense(expenses)
            save_expenses(username, expenses)
        elif choice == "6":
            show_summary(expenses)
        elif choice == "7":
            monthly_summary(expenses)
        elif choice == "8":
            save_expenses(username, expenses)
            print("Expenses saved.")
        elif choice == "9":
            save_expenses(username, expenses)
            print("Logged out successfully.")
            break
        else:
            print("Invalid choice.")

def main():
    users = load_users()
    while True:
        print("\n" + "=" * 45)
        print("PERSONAL EXPENSE TRACKER")
        print("=" * 45)
        print("1. Register")
        print("2. Login")
        print("3. Exit")
        choice = input("Enter choice: ")
        if choice == "1":
            register(users)
        elif choice == "2":
            username = login(users)
            if username != "":
                expense_menu(username)
        elif choice == "3":
            print("Thank you for using Personal Expense Tracker.")
            break
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()
