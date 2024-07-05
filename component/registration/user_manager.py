import os
import csv
from pathlib import Path
from tkinter import messagebox

class UserManager:
    def __init__(self):
        self.OUTPUT_PATH = Path(__file__).parent
        self.ASSETS_PATH = self.OUTPUT_PATH / "assets" / "login"
        self.filename = self.OUTPUT_PATH / "user_rec.csv"

    def relative_to_assets(self, path: str) -> Path:
        return self.ASSETS_PATH / Path(path)

    def execute_python_file(self, file_path):
        try:
            os.system(f'python {file_path}')
        except FileNotFoundError:
            print(f"Error: The file '{file_path}' does not exist.")

    def switch_login(self):
        self.window.destroy()
        self.execute_python_file(self.OUTPUT_PATH / "component/login/main.py")

    def popmsg(self, name):
        messagebox.showinfo("Greetings", f"{name} Welcome Back")
        self.window.destroy()
        self.execute_python_file(self.OUTPUT_PATH / "component/login/main.py")

    def pop_reg_msg(self):
        messagebox.showinfo("Existing Email",
                            "Email Already Exist \n" +
                            "please enter Your Email and Password correctly\n\n" +
                            "If Already have an accont, please Login")

    def input_err(self, field):
        field = f"{field} has no value"
        messagebox.showerror("No Input", field)
