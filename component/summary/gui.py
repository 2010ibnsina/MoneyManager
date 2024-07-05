from tkinter import Tk, Canvas, Button, Label, PhotoImage
from pathlib import Path
from DataManager import DataManager

OUTPUT_PATH = Path(__file__).parent.parent.parent
ASSETS_PATH = OUTPUT_PATH / Path("assets/summary")
filename = OUTPUT_PATH / Path("data_store/data.csv")

class MainWindow:
    def __init__(self, switch_manager, assets_path):
        self.window = Tk()
        self.switch_manager = switch_manager
        self.assets_path = assets_path
        self.setup_window()
        self.data_manager = DataManager(filename)
        self.get_data()
    def run(self): self.window.mainloop()
    
    def setup_window(self):
        self.window.iconbitmap(self.assets_path / "window_logo.ico")
        self.window.geometry("1116x582")
        self.window.title("Money Manager")
        self.window.geometry("+150+40")
        self.window.grid_columnconfigure(0, weight=1)
        self.canvas = Canvas(self.window, bg="#28283F", height=582, width=1116, highlightthickness=0)
        self.canvas.place(x=0, y=0)
        self.image_image_1 = PhotoImage(file=self.assets_path / "image_1.png")
        self.image_1 = self.canvas.create_image(134.0, 455.0, image=self.image_image_1)
        self.button_image_1 = PhotoImage(file=self.assets_path / "button_1.png")
        self.button_1 = Button(image=self.button_image_1, borderwidth=0,
                               command=lambda: self.switch_manager.dashboard(self.window))
        self.button_1.place(x=50.0, y=74.0, width=196.0, height=33.0)
        self.button_image_2 = PhotoImage(file=self.assets_path / "button_2.png")
        self.button_2 = Button(image=self.button_image_2, borderwidth=0,
                               command=lambda: self.switch_manager.income(self.window))
        self.button_2.place(x=51.0, y=107.0, width=189.0, height=26.0)
        self.button_image_3 = PhotoImage(file=self.assets_path / "button_3.png")
        self.button_3 = Button(image=self.button_image_3, borderwidth=0,
                               command=lambda: self.switch_manager.expense(self.window))
        self.button_3.place(x=45.0, y=139.0, width=192.0, height=24.0)
        self.button_image_4 = PhotoImage(file=self.assets_path / "button_4.png")
        self.button_4 = Button(image=self.button_image_4, borderwidth=0)
        self.button_4.place(x=44.0, y=172.0, width=193.0, height=32.0)
        self.button_image_5 = PhotoImage(file=self.assets_path / "button_5.png")
        self.button_5 = Button(image=self.button_image_5, borderwidth=0,
                               command=lambda: self.switch_manager.login(self.window))
        self.button_5.place(x=87.0, y=440.0, width=136.0, height=64.0)
        self.image_image_2 = PhotoImage(file=self.assets_path / "image_2.png")
        self.image_2 = self.canvas.create_image(1060.0, 550.0, image=self.image_image_2)
        self.window.resizable(False, False)
    def get_data(self):
        d_count,start,end = len(self.data_manager.get_data()), 1, 4
        for i, row in enumerate(self.data_manager.get_data(), start=1):
            for col in range(start, end):
                BG = '#0FFF52' if row[0] == '1' else '#E2B2FF' if row[0] == 'flag' else '#FF4545'
                if d_count <= 10:
                    label = Label(self.window, text=row[col], font='Arial', height=2, width=12, relief='ridge', bg=BG)
                else:
                    label = Label(self.window, text=row[col], font='Arial', height=1, width=12, relief='ridge', bg=BG)
                label.grid(row=i, column=col, ipadx='72')
