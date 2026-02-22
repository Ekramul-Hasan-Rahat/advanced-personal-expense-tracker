"""
Utilities for Advanced Personal Expense Tracker
Author: Ekramul Hasan Rahat
Date: 2026-02-22
Description: Functions to add, view, and summarize expenses.
"""

import csv
from datetime import datetime
from collections import defaultdict

FILE_NAME = "expenses.csv"
CATEGORIES = ["Food", "Transport", "Bills", "Entertainment", "Other"]

def add_expense():
    item = input("Enter expense name: ")
    amount = input("Enter amount: ")
    print("Select category:")
    for i, cat in enumerate(CATEGORIES, 1):
        print(f"{i}. {cat}")
    category_choice = int(input("Enter number: "))
    category = CATEGORIES[category_choice-1] if 1 <= category_choice <= len(CATEGORIES) else "Other"
    date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    with open(FILE_NAME, mode="a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([date, item, amount, category])
    
    print(f"Expense '{item}' of {amount} added under '{category}' category!")

def view_expenses():
    print("\nAll Expenses:")
    print("{:<20} {:<20} {:<10} {:<15}".format("Date", "Item", "Amount", "Category"))
    print("-" * 70)
    
    try:
        with open(FILE_NAME, mode="r") as file:
            reader = csv.reader(file)
            for row in reader:
                print("{:<20} {:<20} {:<10} {:<15}".format(*row))
    except FileNotFoundError:
        print("No expenses found. Add your first expense!")

def total_expenses():
    total = 0
    try:
        with open(FILE_NAME, mode="r") as file:
            reader = csv.reader(file)
            for row in reader:
                total += float(row[2])
    except FileNotFoundError:
        print("No expenses found.")
        return
    print(f"\nTotal expenses: {total}")

def category_summary():
    summary = defaultdict(float)
    try:
        with open(FILE_NAME, mode="r") as file:
            reader = csv.reader(file)
            for row in reader:
                summary[row[3]] += float(row[2])
    except FileNotFoundError:
        print("No expenses found.")
        return
    
    print("\nExpenses by Category:")
    for cat, amount in summary.items():
        print(f"{cat}: {amount}")

def monthly_summary():
    summary = defaultdict(float)
    try:
        with open(FILE_NAME, mode="r") as file:
            reader = csv.reader(file)
            for row in reader:
                month = row[0][:7]  # YYYY-MM
                summary[month] += float(row[2])
    except FileNotFoundError:
        print("No expenses found.")
        return
    
    print("\nMonthly Expense Summary:")
    for month, amount in summary.items():
        print(f"{month}: {amount}")