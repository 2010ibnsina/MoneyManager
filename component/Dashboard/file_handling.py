import os
from pathlib import Path
import csv

class FileHandling:
    def __init__(self):
        self.OUTPUT_PATH = Path(__file__).parent.parent.parent
        self.filename = self.OUTPUT_PATH / Path("data_store/data.csv")

    def calculate_income_expenses(self):
        income_data = {}
        expenses_data = {}

        with open(self.filename, newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                flag = int(row['flag'])
                source = row['Source']
                amount = float(row['Amount'])

                if flag == 0:  # Expense
                    expenses_data[source] = amount
                elif flag == 1:  # Income
                    income_data[source] = amount

        # Sort the dictionaries by value in descending order
        sorted_income_data = dict(sorted(income_data.items(), key=lambda item: item[1], reverse=True))
        sorted_expenses_data = dict(sorted(expenses_data.items(), key=lambda item: item[1], reverse=True))

        # Keep the top 4 categories for expenses and sum the rest for "Others"
        top_expenses = dict(list(sorted_expenses_data.items())[:4])
        other_expenses = sum(list(sorted_expenses_data.values())[4:])
        top_expenses['Others'] = other_expenses

        # Keep the top 4 categories for income and sum the rest for "Others"
        top_income = dict(list(sorted_income_data.items())[:4])
        other_income = sum(list(sorted_income_data.values())[4:])
        top_income['Others'] = other_income

        return top_income, top_expenses
