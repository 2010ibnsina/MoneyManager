from user_manager import UserManager
import csv

class LoginManager(UserManager):
    def __init__(self):
        super().__init__()

    def check_user(self, email, password):
        with open(self.filename, 'r') as file:
            readar = csv.reader(file)
            next(readar)  # Skip the field names
            flag = 0
            for line in readar:
                if email == line[1] and password == line[2]:
                    self.popmsg(line[0])
                    flag = 1
                    break
            if flag == 0:
                self.pop_reg_msg()

    def get_data(self):
        email = self.entry_1.get()
        if email == "":
            self.input_err("Email")
        password = self.entry_2.get()
        if password == "":
            self.input_err("Password")

        self.check_user(email, password)
