import csv
from datetime import datetime

def add_expense():
    date = input("Enter the date (YYYY-MM-DD): ")
    category = input("Enter the category: ")
    amount = float(input("Enter the amount: "))
    notes = input("Enter any notes (optional): ")

    with open("expenses.csv", "a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([date, category, amount, notes])

    print("Expense added successfully!")


def view_expenses():
    print("\nAll Expenses:")
    with open("expenses.csv", "r") as file:
        reader = csv.reader(file)
        print("{:<15} {:<15} {:<10} {:<20}".format("Date", "Category", "Amount", "Notes"))
        print("-" * 60)
        for row in reader:
            print("{:<15} {:<15} {:<10} {:<20}".format(row[0], row[1], row[2], row[3]))


def view_summary():
    category_totals = {}
    with open("expenses.csv", "r") as file:
        reader = csv.reader(file)
        next(reader) #skip the header row

        for row in reader:
            if len(row) <3:
                print(f"Skipping invalid row: {row}")
                continue

            category = row[1]            
            try:
                amount = float(row[2])
                category_totals[category] = category_totals.get(category, 0) + amount

            except ValueError:
                print(f"Invalid row skipped: {row}")
                continue

    print("\nSummary by Category: ")
    for category, total in category_totals.items():
        print(f"{category}: Rs.{total:.2f}")


def view_monthly_expenses():
    month = input("Enter the month (YYYY-MM): ")
    total = 0

    print("\nExpenses for", month)
    with open("expenses.csv", "r") as file:
        reader = csv.reader(file)
        for row in reader:
            if row[0].startswith(month):
                total += float(row[2])
                print(f"{row[0]} - {row[1]}: ${row[2]} ({row[3]})")
    print(f"Total for {month}: ${total:.2f}")


def menu():
    while True:
        print("\nExpense Tracker")
        print("1. Add Expense")
        print("2. View All Expenses")
        print("3. View Summary by Category")
        print("4. View Monthly Expenses")
        print("5. Quit")

        choice = input("Enter your choice: ")
        
        if choice == "1":
            add_expense()
        elif choice == "2":
            view_expenses()
        elif choice == "3":
            view_summary()
        elif choice == "4":
            view_monthly_expenses()
        elif choice == "5":
            print("Exiting.. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

import os

def intialize_csv():
    if not os.path.exists("expenses.csv"):
        with open("expenses.csv", "w", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(["Date", "Category", "Amount", "Notes"])

if __name__ == "__main__":
    intialize_csv()
    menu()