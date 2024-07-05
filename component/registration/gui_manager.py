from tkinter import Tk, Canvas, Entry, Button, PhotoImage
from pathlib import Path
from login_manager import LoginManager

class GUI(LoginManager):
    def __init__(self):
        super().__init__()
        self.OUTPUT_PATH = Path(__file__).parent.parent.parent
        self.ASSETS_PATH = self.OUTPUT_PATH / Path("assets/reg")
        self.filename = self.OUTPUT_PATH / Path("data_store/user_rec.csv")
        self.window = Tk()
        self.window.iconbitmap(self.relative_to_assets("window_logo.ico"))
        self.window.title("Money Manager")
        self.window.geometry("1116x582")
        self.window.geometry("+150+40")
        self.window.configure(bg="#FFFFFF")
        self.canvas = Canvas(self.window,bg="#FFFFFF",height=582,width=1116,bd=0,highlightthickness=0)
        self.canvas.place(x=0, y=0)
        self.create_widgets()

    def create_widgets(self):
        self.image_image_1 = PhotoImage(file=self.relative_to_assets("image_1.png"))
        self.canvas.create_image(558.0,291.0,image=self.image_image_1)
        self.image_image_2 = PhotoImage(file=self.relative_to_assets("image_2.png"))
        self.canvas.create_image(772.0,290.0,image=self.image_image_2)
        self.canvas.create_text(613.0,92.0,anchor="nw",text="Create an Account",fill="#000000",font=("Arial", 20 * -1))
        self.entry_image_1 = PhotoImage(file=self.relative_to_assets("entry_1.png"))
        self.canvas.create_image(772.92,161.44,image=self.entry_image_1)
        self.entry_1 = Entry(bd=0,bg="#DAF3C6",fg="#000716",highlightthickness=0)
        self.entry_1.place(x=622.72,y=137.98,width=300.39,height=44.92)
        self.canvas.create_rectangle(624,129,690,143,fill="#FAFAFA",outline="")
        self.canvas.create_text(621,120,anchor="nw",text="Your Name",fill="#212121",font=("Arial", 12 * -1))
        self.entry_image_2 = PhotoImage(file=self.relative_to_assets("entry_1.png"))
        self.canvas.create_image(772.916,220.88,image=self.entry_image_2)
        self.entry_2 = Entry(bd=0,bg="#DAF3C6",fg="#000716",highlightthickness=0)
        self.entry_2.place(x=622.72,y=197.34,width=300.39,height=45.08)
        self.entry_image_3 = PhotoImage(file=self.relative_to_assets("entry_2.png"))
        self.canvas.create_image(772.92,284.78,image=self.entry_image_3)
        self.entry_3 = Entry(bd=0,bg="#DAF3C6",fg="#000716",highlightthickness=0,show="*")
        self.entry_3.place(x=622.72,y=261.24,width=300.39,height=45.08)
        self.canvas.create_rectangle(624.0,187.65,662.0,202.7,fill="#FAFAFA",outline="")
        self.canvas.create_text(620.0,180.62,anchor="nw",text="Email",fill="#212121",font=("Arial", 12 * -1))
        self.canvas.create_rectangle(621.0,247.85,686.0,265.92,fill="#FAFAFA",outline="")
        self.canvas.create_text(625.0,240.83,anchor="nw",text="Password",fill="#212121",font=("Arial", 12 * -1))
        self.button_image_1 = PhotoImage(file=self.relative_to_assets("button_1.png"))
        button_1 = Button(image=self.button_image_1,borderwidth=0,highlightthickness=0,command=self.get_data)
        button_1.place(x=614.72,y=321.77,width=316.39,height=47.08)
        self.canvas.create_text(613.0,33.0,anchor="nw",text="LET'S GET YOU STARTED",fill="#000000",font=("Arial", 12 * -1))
        self.canvas.create_text(633.0,415.0,anchor="nw",text="Already have an account?",fill="#212121",font=("Arial", 24 * -1))
        self.button_image_2 = PhotoImage(file=self.relative_to_assets("button_2.png"))
        button_2 = Button(image=self.button_image_2,borderwidth=0,highlightthickness=0,command=self.switch_login)
        button_2.place(x=660.0,y=457.0,width=220.0,height=44.0)
        self.image_image_4 = PhotoImage(file=self.relative_to_assets("image_4.png"))
        self.canvas.create_image(213.0,59.10955810546875,image=self.image_image_4)

    def run(self):
        self.window.resizable(False,False)
        self.window.mainloop()