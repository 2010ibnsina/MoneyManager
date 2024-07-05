from file_handling import FileHandling
from tkinter import *

class ShowInfo:
    def __init__(self, window):
        self.data = FileHandling()
        self.window = window
        self.frame2 = Frame(window, bg='#008DDA')
        self.frame2.place(x=300, y=430, width=210, height=148)
        self.frame3 = Frame(window, bg='#BFEA7C')
        self.frame3.place(x=574, y=430, width=239, height=148)
        self.frame4 = Frame(window, bg='#FF8911')
        self.frame4.place(x=870, y=430, width=239, height=148)
        income_data, expenses_data = self.data.calculate_income_expenses()
        total_income = sum(income_data.values())
        total_expenses = sum(expenses_data.values())
        total_balance = total_income - total_expenses
        total_balance_label = Label(self.frame2, font=("", 14, "bold"), bg='#008DDA')
        total_balance_label.place(x=36, y=20)
        total_balance_label.config(text='Total Balance\n\n', fg='#FBA834')
        balance_text = f'{total_balance}'
        balance_label = Label(self.frame2, text=balance_text, font=("", 28, "bold"), fg='#9CFF2E', bg='#008DDA')
        balance_label.place(x=33, y=60)
        most_income_source = max(income_data, key=income_data.get)
        most_income_amount = income_data[most_income_source]
        most_income_label_text = "Most Income Source"
        most_income_source_text = most_income_source
        most_income_amount_text = f"Amount: {most_income_amount}"
        most_income_label_text_label = Label(self.frame3, text=most_income_label_text, font=("Arial", 14, "bold"),
                                             fg='black', bg='#BFEA7C')
        most_income_source_text_label = Label(self.frame3, text=most_income_source_text, font=("Arial", 22, "bold"),
                                              fg='#FF407D', bg='#BFEA7C')
        most_income_amount_text_label = Label(self.frame3, text=most_income_amount_text, font=("Arial", 19, "bold"),
                                              fg='#0F1035', bg='#BFEA7C')
        most_income_label_text_label.place(x=20, y=20)
        most_income_source_text_label.place(x=35, y=55)
        most_income_amount_text_label.place(x=20, y=100)
        most_expense_source = max(expenses_data, key=expenses_data.get)
        most_expense_amount = expenses_data[most_expense_source]
        most_expense_label_1 = Label(self.frame4, text="Most Expense Source", font=("Arial", 14, "bold"), fg='white',
                                     bg='#FF8911')
        most_expense_label_2 = Label(self.frame4, text=most_expense_source, font=("Arial", 19, "bold"), fg='#000000',
                                     bg='#FF8911')
        most_expense_label_3 = Label(self.frame4, text=f"Amount: {most_expense_amount}", font=("Arial", 19, "bold"),
                                     fg='#35155D', bg='#FF8911')
        most_expense_label_1.place(x=20, y=20)
        most_expense_label_2.place(x=90, y=55)
        most_expense_label_3.place(x=29, y=100)
    def update_balance_labels(self):
        income_data, expenses_data = self.data.calculate_income_expenses()
        total_income = sum(income_data.values())
        total_expenses = sum(expenses_data.values())
        self.total_balance = total_income - total_expenses
    def display_balance_labels(self):
        total_balance_label = Label(self.frame2, font=("", 14, "bold"), bg='#008DDA')
        total_balance_label.place(x=36, y=20)
        total_balance_label.config(text='Total Balance\n\n', fg='#FBA834')
        balance_text = f'{self.total_balance}'
        balance_label = Label(self.frame2, text=balance_text, font=("", 28, "bold"), fg='#9CFF2E', bg='#008DDA')
        balance_label.place(x=33, y=60)
