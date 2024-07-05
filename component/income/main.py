from tkinter import Tk
from pathlib import Path
from Navigation import NavigationHandler
from GUI import IncomeManagerGUI
from Feedback import Feedback

OUTPUT_PATH = Path(__file__).parent.parent.parent
filename = OUTPUT_PATH / Path("data_store/data.csv")


class IncomeManager:
    def __init__(self):
        self.window = Tk()
        self.window.iconbitmap(IncomeManagerGUI.relative_to_assets("window_logo.ico"))
        self.window.title("Money Manager")
        self.window.geometry("1116x582")
        self.window.geometry("+150+40")
        self.window.configure(bg="#28283F")
        self.window.resizable(False, False)

        self.gui = IncomeManagerGUI(self.window)
        self.navigation = NavigationHandler(self.window)
        self.feed = Feedback(self.window)

    def run(self):
        self.window.mainloop()


if __name__ == "__main__":
    app = IncomeManager()
    app.run()
