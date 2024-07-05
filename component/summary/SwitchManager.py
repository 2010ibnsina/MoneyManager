import os

class SwitchManager:
    def __init__(self, output_path):
        self.output_path = output_path

    def dashboard(self,window):
        window.destroy()
        self.execute_python_file("dashboard/main.py")

    def login(self,window):
        window.destroy()
        self.execute_python_file("login/main.py")

    def expense(self,window):
        window.destroy()
        self.execute_python_file("expense/main.py")

    def income(self,window):
        window.destroy()
        self.execute_python_file("income/main.py")


    def execute_python_file(self, file_path):
        try:
            os.system(f'python {self.output_path / file_path}')
        except FileNotFoundError:
            print(f"Error: The file '{file_path}' does not exist.")
