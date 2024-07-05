from pathlib import Path
from tkinter import Label
from DataHandler import DataHandler


class Feedback:
    def __init__(self, window):
        self.OUTPUT_PATH = Path(__file__).parent.parent.parent
        self.filename = self.OUTPUT_PATH / "data_store/data.csv"
        self.income_source = None
        self.income_amount = None
        self.window = window
        font_size = 12
        self.warning_label = Label(window, bg="#28283F", fg="red", font=("Poppins", font_size))

    def show_submit_label(self):
        self.warning_label.place(x=515.0, y=380.0)
        self.warning_label.config(text="Successfully Submitted!!", fg="white")
        self.window.after(900, lambda: self.warning_label.place_forget())

    def show_no_source_label(self):
        self.warning_label.place(x=515.0, y=380.0)
        self.warning_label.config(text="Please Enter Income Source", fg="red")

    def show_no_amount_label(self):
        self.warning_label.place(x=515.0, y=380.0)
        self.warning_label.config(text="Please Enter Income Amount", fg="red")

    def show_no_data_label(self):
        self.warning_label.place(x=515.0, y=380.0)
        self.warning_label.config(text="Please provide data in both field.",
                                  fg="red")

    def show_input_error_label(self):
        self.warning_label.place(x=515.0, y=380.0)
        self.warning_label.config(text="Income Amount Can Be Only Positive Numbers", fg="red")

    def submit_data(self, date,income_source, income_amount):
        income_flag=1
        if income_source and income_amount.isnumeric():
            data = DataHandler(self.filename)
            data.data_write([income_flag, date, income_source, income_amount])
            self.show_submit_label()

        elif income_amount and not income_source:
            self.show_no_source_label()

        elif not income_amount and income_source:
            self.show_no_amount_label()

        elif not income_source and not income_amount:
            self.show_no_data_label()

        elif not income_amount.isnumeric():
            self.show_input_error_label()
