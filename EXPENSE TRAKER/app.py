import csv
import os
from collections import defaultdict
import matplotlib.pyplot as plt

CSV_FILE = "expenses.csv"

# Create CSV file if it doesn't exist
if not os.path.exists(CSV_FILE):
    with open(CSV_FILE, "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["Date", "Type", "Category", "Amount"])


def menu():
    print("\n===== Expense Tracker CLI =====")
    print("1. Add Transaction")
    print("2. View Transactions")
    print("3. Monthly Summary")
    print("4. Export Report")
    print("5. Generate Expense Chart")
    print("6. Exit")


def add_transaction():
    date = input("Enter Date (YYYY-MM-DD): ")
    ttype = input("Enter Type (Income/Expense): ").strip().title()
    category = input("Enter Category: ").strip().title()

    try:
        amount = float(input("Enter Amount: "))
    except ValueError:
        print("❌ Invalid Amount!")
        return

    with open(CSV_FILE, "a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([date, ttype, category, amount])

    print("✅ Transaction Added Successfully!")


def view_transactions():
    print("\n----- Transactions -----")

    with open(CSV_FILE, "r", newline="") as file:
        reader = csv.reader(file)

        for row in reader:
            print(row)


def monthly_summary():
    income = 0
    expense = 0

    with open(CSV_FILE, "r", newline="") as file:
        reader = csv.DictReader(file)

        for row in reader:
            try:
                amount = float(row["Amount"])
            except:
                continue

            if row["Type"].lower() == "income":
                income += amount
            elif row["Type"].lower() == "expense":
                expense += amount

    balance = income - expense

    print("\n----- Monthly Summary -----")
    print(f"Total Income : ₹{income:.2f}")
    print(f"Total Expense: ₹{expense:.2f}")
    print(f"Balance      : ₹{balance:.2f}")


def export_report():
    income = 0
    expense = 0

    with open(CSV_FILE, "r", newline="") as file:
        reader = csv.DictReader(file)

        for row in reader:
            try:
                amount = float(row["Amount"])
            except:
                continue

            if row["Type"].lower() == "income":
                income += amount
            elif row["Type"].lower() == "expense":
                expense += amount

    balance = income - expense

    with open("monthly_report.csv", "w", newline="") as file:
        writer = csv.writer(file)

        writer.writerow(["Metric", "Amount"])
        writer.writerow(["Total Income", income])
        writer.writerow(["Total Expense", expense])
        writer.writerow(["Balance", balance])

    print("✅ Report exported as monthly_report.csv")


def generate_chart():
    categories = defaultdict(float)

    with open(CSV_FILE, "r", newline="") as file:
        reader = csv.DictReader(file)

        for row in reader:
            try:
                amount = float(row["Amount"])
            except:
                continue

            if row["Type"].lower() == "expense":
                category = row["Category"].strip().title()
                categories[category] += amount

    if not categories:
        print("❌ No expense data available.")
        return

    plt.figure(figsize=(6, 6))
    plt.pie(
        categories.values(),
        labels=categories.keys(),
        autopct="%1.1f%%"
    )

    plt.title("Expense Distribution")
    plt.savefig("expense_chart.png")
    plt.show()

    print("✅ Chart saved as expense_chart.png")


while True:
    menu()

    choice = input("Enter your choice: ")

    if choice == "1":
        add_transaction()

    elif choice == "2":
        view_transactions()

    elif choice == "3":
        monthly_summary()

    elif choice == "4":
        export_report()

    elif choice == "5":
        generate_chart()

    elif choice == "6":
        print("👋 Thank You for using Expense Tracker!")
        break

    else:
        print("❌ Invalid Choice")