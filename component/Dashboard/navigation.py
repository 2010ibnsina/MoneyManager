from pathlib import Path
import os


class Navigation:
    def __init__(self,window):
        self.window=window

    def execute_python_file(self,file_path):
        try:
            os.system(f'python {file_path}')
        except FileNotFoundError:
            print(f"Error: The file '{file_path}' does not exist.")

    def switch_login(self,path):
        self.window.destroy()
        self.execute_python_file(path / Path("login/main.py"))

    def switch_income(self,path):
        self.window.destroy()
        self.execute_python_file(path/ Path("income/main.py"))

    def switch_expense(self,path):
        self.window.destroy()
        self.execute_python_file(path / Path("expense/main.py"))

    def switch_summary(self,path):
        self.window.destroy()
        self.execute_python_file(path / Path("summary/main.py"))
