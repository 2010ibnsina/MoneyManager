import os
from pathlib import Path
from FeedBack import Feedback


class NavigationHandler:
    OUTPUT_PATH = Path(__file__).parent.parent.parent
    OUTPUT_PATH = OUTPUT_PATH / Path(r"component")

    def __init__(self, window):
        self.window = window
        self.feed=Feedback(self.window)

    @staticmethod
    def execute_python_file(file_path):
        try:
            os.system(f'python {file_path}')
        except FileNotFoundError:
            print(f"Error: The file '{file_path}' does not exist.")

    def switch_login(self):
        self.window.destroy()
        self.execute_python_file(self.OUTPUT_PATH / Path("login/main.py"))

    def switch_dashboard(self):
        self.window.destroy()
        self.execute_python_file(self.OUTPUT_PATH / Path("dashboard/main.py"))

    def switch_income(self):
        self.window.destroy()
        self.execute_python_file(self.OUTPUT_PATH / Path("income/main.py"))

    def switch_summary(self):
        self.window.destroy()
        self.execute_python_file(self.OUTPUT_PATH / Path("summary/main.py"))

    def submit_data(self,expense_date,expense_sorce,expense_amount):
        self.feed.submit_data(expense_date,expense_sorce,expense_amount)
