from pathlib import Path
from tkinter import Label
from DataHandler import DataHandler


class Feedback:
    def __init__(self, window):
        self.OUTPUT_PATH = Path(__file__).parent.parent.parent
        self.filename = self.OUTPUT_PATH / "data_store/data.csv"
        self.expense_source = None
        self.expense_amount = None
        self.window = window
        self.warning_label = Label(window, bg="#28283F", fg="red", font=("Poppins", 12))

    def show_submit_label(self):
        self.warning_label.place(x=515.0, y=430.0)
        self.warning_label.config(text="Successfully Submitted!!", fg="white")
        self.window.after(900, lambda: self.warning_label.place_forget())

    def show_no_source_label(self):
        self.warning_label.place(x=515.0, y=430.0)
        self.warning_label.config(text="Please Enter Expense Reason", fg="red")

    def show_no_amount_label(self):
        self.warning_label.place(x=515.0, y=430.0)
        self.warning_label.config(text="Please Enter Expense Amount", fg="red")

    def show_no_data_label(self):
        self.warning_label.place(x=515.0, y=430.0)
        self.warning_label.config(text="Please provide data in both field.",
                                  fg="red", font=("Poppins", 10))

    def show_input_error_label(self):
        self.warning_label.place(x=515.0, y=430.0)
        self.warning_label.config(text="Expense Amount Can Be Only Positive Numbers", fg="red")

    def submit_data(self, e_date, expense_source, expense_amount):
        expense_flag=0
        if expense_source and expense_amount.isnumeric():
            data = DataHandler(self.filename)
            data.data_write([expense_flag, e_date, expense_source, expense_amount])
            self.show_submit_label()

        elif expense_amount and not expense_source:
            self.show_no_source_label()

        elif not expense_amount and expense_source:
            self.show_no_amount_label()

        elif not expense_source and not expense_amount:
            self.show_no_data_label()

        elif not expense_amount.isnumeric():
            self.show_input_error_label()
