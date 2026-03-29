import pandas as pd
import os
from datetime import datetime
import matplotlib.pyplot as plt

# Configuration
FILE_NAME = "expenses.csv"

def initialize_df():
    """Ensures a CSV exists with the correct columns."""
    if os.path.exists(FILE_NAME):
        return pd.read_csv(FILE_NAME)
    else:
        # Define the structure of our tracker
        columns = ["Date", "Category", "Description", "Amount"]
        df = pd.DataFrame(columns=columns)
        df.to_csv(FILE_NAME, index=False)
        return df

def add_expense(category, description, amount):
    """Appends a new expense to the CSV."""
    df = pd.read_csv(FILE_NAME)

    new_entry = {
        "Date": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "Category": category,
        "Description": description,
        "Amount": float(amount)
    }

    # Append the new row and save
    df = pd.concat([df, pd.DataFrame([new_entry])], ignore_index=True)
    df.to_csv(FILE_NAME, index=False)
    print("\n✅ Expense added successfully!")

def delete_expense():
    df = pd.read_csv(FILE_NAME)
    print(df)
    loc = int(input("Enter index to delete:"))
    df = df.drop(index=loc)
    df.to_csv(FILE_NAME,index=False)
    view_summary()

def save_expenses(df):
    df = df.sort_values(by='Amount')
    df.to_csv(FILE_NAME,index=False)

def view_summary():
    """Displays data and basic stats using Pandas."""
    df = pd.read_csv(FILE_NAME)

    if df.empty:
        print("\n📭 No expenses recorded yet.")
        return

    print("\n--- Current Expenses ---")
    print(df)

    # Use Pandas magic for a quick summary
    total = df["Amount"].sum()
    print(f"\n💰 Total Spent: ${total:.2f}")

    print("\n--- Spending by Category ---")
    print(df.groupby("Category")["Amount"].sum())

def edit_expense(location):
    df = pd.read_csv(FILE_NAME)
    location = int(location) - 1
    if location < 0 or location >= len(df):
        print("Invalid expense number.")
        return
    print("\nCurrent values:")
    print(df.iloc[location])
    new_cat = input("New Category (leave blank to keep same): ")
    new_desc = input("New Description (leave blank to keep same): ")
    new_amt = input("New Amount (leave blank to keep same): ")
    if new_cat:
        df.at[location, "Category"] = new_cat
    if new_desc:
        df.at[location, "Description"] = new_desc
    if new_amt:
        df.at[location, "Amount"] = float(new_amt)
    df.to_csv(FILE_NAME, index=False)
    print("Expense updated successfully!")

def plot_expenses():
    df = pd.read_csv(FILE_NAME)
    category_totals = df.groupby('Category')['Amount'].sum()
    plt.figure(figsize=(8,8)) # 8x8 inches
    plt.pie(category_totals, labels=category_totals.index, autopct='%1.1f%%')
    plt.title('Total Expense by Category')
    plt.axis('equal')
    plt.show()

def main():
    initialize_df()

    while True:
        print("\n--- 📈 Expense Tracker CLI ---")
        print("1. Add Expense")
        print("2. View Summary")
        print("3. Delete Expense")
        print("4. Edit Expense")
        print("5. Plot")
        print("6. Exit")

        choice = input("Select an option: ")

        if choice == "1":
            cat = input("Enter Category (e.g., Food, Rent, Fun): ")
            desc = input("Short Description: ")
            amt = input("Amount: ")
            add_expense(cat, desc, amt)
        elif choice == "2":
            view_summary()
        elif choice == "3":
            delete_expense()
        elif choice == "4":
            location = input("Enter expense number:")
            edit_expense(int(location))
        elif choice == "5":
            plot_expenses()
        elif choice == "6":
            print("Goodbye!")
            break
        else:
            print("Invalid choice, try again.")


if __name__ == "__main__":
    main()