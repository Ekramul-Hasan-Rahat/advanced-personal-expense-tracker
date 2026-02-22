"""
Charts for Advanced Personal Expense Tracker
Author: Ekramul Hasan Rahat
Date: 2026-02-22
Description: Functions to visualize expenses by category using matplotlib.
"""

import csv
from collections import defaultdict
import matplotlib.pyplot as plt

FILE_NAME = "expenses.csv"

def plot_expenses_chart():
    summary = defaultdict(float)
    
    try:
        with open(FILE_NAME, mode="r") as file:
            reader = csv.reader(file)
            for row in reader:
                summary[row[3]] += float(row[2])
    except FileNotFoundError:
        print("No expenses found.")
        return
    
    categories = list(summary.keys())
    amounts = list(summary.values())
    
    plt.figure(figsize=(8,5))
    plt.bar(categories, amounts, color="skyblue")
    plt.title("Expenses by Category")
    plt.xlabel("Category")
    plt.ylabel("Amount")
    plt.show()