from tkinter import Canvas, PhotoImage, Button, Entry
from tkcalendar import DateEntry
from pathlib import Path
from datetime import date
from Navigation import NavigationHandler

ASSETS_PATH = Path(__file__).parent.parent.parent / "assets" / "income"

class IncomeManagerGUI:
    def __init__(self, window):
        self.window = window
        self.canvas = Canvas(window, bg="#28283F", height=582, width=1116, bd=0, highlightthickness=0)
        self.canvas.place(x=0, y=0)
        self.nav = NavigationHandler(self.window)
        self.image_image_1 = PhotoImage(file=self.relative_to_assets("image_1.png"))
        self.image_1 = self.canvas.create_image(135.0, 298.0, image=self.image_image_1)
        self.button_image_1 = PhotoImage(file=self.relative_to_assets("button_1.png"))
        self.button_1 = Button(image=self.button_image_1, borderwidth=0, command=self.nav.switch_dashboard)
        self.button_1.place(x=50.0, y=74.0, width=196.0, height=33.0)
        self.button_image_2 = PhotoImage(file=self.relative_to_assets("button_2.png"))
        self.button_2 = Button(image=self.button_image_2, borderwidth=0)
        self.button_2.place(x=51.0, y=107.0, width=189.0, height=26.0)
        self.button_image_3 = PhotoImage(file=self.relative_to_assets("button_3.png"))
        self.button_3 = Button(image=self.button_image_3, borderwidth=0, command=self.nav.switch_expense)
        self.button_3.place(x=53.0, y=139.0, width=193.0, height=32.0)
        self.button_image_4 = PhotoImage(file=self.relative_to_assets("button_4.png"))
        self.button4 = Button(image=self.button_image_4, borderwidth=0, command=self.nav.switch_summary)
        self.button4.place(x=47.0, y=173.0, width=196.0, height=31.0)
        self.button_image_5 = PhotoImage(file=self.relative_to_assets("button_5.png"))
        self.button_5 = Button(image=self.button_image_5, borderwidth=0, command=self.nav.switch_login)
        self.button_5.place(x=87.0, y=440.0, width=136.0, height=64.0)
        self.canvas.create_rectangle(486.0, 46.0, 881.0, 539.0, fill="#28283F", outline="")
        self.image_image_2 = PhotoImage(file=self.relative_to_assets("image_2.png"))
        self.image_2 = self.canvas.create_image(684.0, 292.0, image=self.image_image_2)
        self.button_image_6 = PhotoImage(file=self.relative_to_assets("button_6.png"))
        self.canvas.create_rectangle(503.0, 107.0, 858.0, 191.0, fill="#454567", outline="")
        self.canvas.create_rectangle(503.0, 247.0, 858.0, 331.0, fill="#454567", outline="")
        self.entry_image_1 = PhotoImage(file=self.relative_to_assets("entry_1.png"))
        self.entry_bg_1 = self.canvas.create_image(680.5, 149.0, image=self.entry_image_1)
        self.entry_1 = Entry(bd=0, bg="#FFFFFF", fg="#000716", highlightthickness=0)
        self.entry_1.place(x=526.0, y=107.0, width=309.0, height=82.0)
        self.entry_image_2 = PhotoImage(file=self.relative_to_assets("entry_2.png"))
        self.entry_bg_2 = self.canvas.create_image(680.5, 289.0, image=self.entry_image_2)
        self.entry_2 = Entry(bd=0, bg="#FFFFFF", fg="#000716", highlightthickness=0)
        self.entry_2.place(x=526.0, y=247.0, width=309.0, height=82.0)
        self.canvas.create_text(600, 89, text="Enter Income Source", fill="#FEFAD9", font=("Arial", 12))
        self.canvas.create_text(600, 226, text="Enter Income Amount", fill="#FEFAD9", font=("Arial", 12))
        def submit_data():
            source, amount=self.entry_1.get().strip(), self.entry_2.get().strip()
            self.nav.submit_data(date.today().strftime("%b %d %Y"),source, amount)
            if amount.isnumeric() and not source == "":
                self.entry_1.delete(0, "end")
                self.entry_2.delete(0, 'end')
        self.button_6 = Button(image=self.button_image_6, borderwidth=0, command=submit_data)
        self.button_6.place(x=612.0, y=466.0, width=136.0, height=65.46)
    @staticmethod
    def relative_to_assets(path: str) -> Path:
        return ASSETS_PATH / Path(path)
