"""
Advanced Personal Expense Tracker
Author: Ekramul Hasan Rahat
Date: 2026-02-22
Description: Main program to manage personal expenses with categories, summaries, and charts.
"""

from utils import add_expense, view_expenses, total_expenses, category_summary, monthly_summary
from charts import plot_expenses_chart

def main():
    print("Welcome to Advanced Personal Expense Tracker")
    
    while True:
        print("\nSelect an option:")
        print("1. Add an expense")
        print("2. View all expenses")
        print("3. Show total expenses")
        print("4. Show expenses by category")
        print("5. Show monthly summary")
        print("6. Plot expenses chart")
        print("7. Exit")
        
        choice = input("Enter your choice (1-7): ")
        
        if choice == "1":
            add_expense()
        elif choice == "2":
            view_expenses()
        elif choice == "3":
            total_expenses()
        elif choice == "4":
            category_summary()
        elif choice == "5":
            monthly_summary()
        elif choice == "6":
            plot_expenses_chart()
        elif choice == "7":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()