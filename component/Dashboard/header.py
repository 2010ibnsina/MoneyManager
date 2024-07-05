from datetime import datetime
from tkinter import Label, PhotoImage, TclError,Frame
from pathlib import Path


class Header:
    def __init__(self, window):
        self.window = window
        self.header = Frame(window, bg='#C07BB5')
        self.header.place(x=300, y=0, width=840, height=50)
        self.OUTPUT_PATH = Path(__file__).parent.parent.parent
        self.ASSETS_PATH = self.OUTPUT_PATH / Path("assets/dashboard")


        # Greeting text
        self.greeting_text = Label(self.header, text=self.get_greeting(), font=("Pacifico", 22, "bold"), fg='#FFC436',
                                   bg='#C07BB5')
        self.greeting_text.place(x=310, y=5)

        # Time text
        time_text = f'It\'s  {self.get_time()}'
        self.time_label = Label(self.header, text=time_text, font=("Pacifico", 17, "bold"), fg='#000000', bg='#C07BB5')
        self.time_label.place(x=680, y=10)


        # Profile
        profile_image_path = self.relative_to_assets("avatar.png")
        try:
            profile_photo = PhotoImage(file=profile_image_path)
        except TclError:
            profile_photo = None
            print(f"Profile image not found: {profile_image_path}")
        self.profile_label = Label(window, image=profile_photo, bg='#C07BB5')
        self.profile_label.image = profile_photo
        self.profile_label.place(x=315, y=8)

    def get_time(self):
        return datetime.now().strftime("%H:%M")

    def get_greeting(self):
        current_hour = datetime.now().hour

        greetings = {
            current_hour < 12: "Good Morning",
            12 <= current_hour < 18: "Good Afternoon",
            18 <= current_hour < 24: "Good Evening",
        }

        return greetings[True]

    def relative_to_assets(self, path: str) -> Path:
        return self.ASSETS_PATH / Path(path)
