from tkinter import Tk
from header import Header
from body import Body
from show_info import ShowInfo


class Main:
    def __init__(self):
        window = Tk()
        window.geometry("1116x582")
        window.configure(bg="#28283F")
        window.title("Money Manager")
        window.geometry("+150+40")

        self.body = Body(window)
        self.header = Header(window)
        self.footer=ShowInfo(window)

        window.resizable(False, False)
        window.mainloop()

if __name__ == "__main__":
    main = Main()
