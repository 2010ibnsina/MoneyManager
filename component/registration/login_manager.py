from user_manager import UserManager
import csv
from pathlib import Path
from  tkinter import messagebox

OUTPUT_PATH = Path(__file__).parent.parent.parent
filename=OUTPUT_PATH/Path("data_store/user_rec.csv")

def popmsg():
    messagebox.showinfo("Already Registered","User Already Exist\nPlease Log in")

class LoginManager(UserManager):
    def __init__(self):
        super().__init__()



    def check_user_list(self,field,reader):
        for line in reader:
            if field[1]==line[1]:
                popmsg()
                self.switch_login()
                return True
            

    def new_user(self,field):
        with open(filename,'r+',newline="") as file:
            self.field=field
            reader=csv.reader(file)
            if not self.check_user_list(self.field,reader):
                csv.writer(file).writerow(self.field)
                messagebox.showinfo("Success","New User Registration is Successful.\n"+
                                    "Now Log Into The System")
                file.close()
                self.switch_login()

    def get_data(self):
        name=self.entry_1.get()
        if name == "":
            self.input_err("name")
        email = self.entry_2.get()
        if email == "":
            self.input_err("Email")
        password = self.entry_3.get()
        if password == "":
            self.input_err("Password")

        if name != "" and email != "" and password != "" :
            # self.check_user(email, password)
            self.field=[name,email,password]
            self.new_user(self.field)
