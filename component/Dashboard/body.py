from tkinter import *
from file_handling import FileHandling
from navigation import Navigation
from pathlib import Path

assets_path = Path(__file__).parent.parent.parent / Path(r"assets/dashboard")
path = Path(__file__).parent.parent

class Body:
    def __init__(self, window):
        self.file_handler = FileHandling()
        self.window = window
        self.nav=Navigation(self.window)
        self.canvas = Canvas(self.window, bg='#28283F', width=1116, height=582, bd=0, highlightthickness=0)
        self.canvas.place(x=0, y=0)
        self.image_image_1 = PhotoImage(file=assets_path / "image_1.png")
        self.canvas.create_image(134.0, 291.0, image=self.image_image_1,)
        self.frame1 = Frame(window, bg='#7CCEC9')
        self.frame1.place(x=300, y=70, width=840, height=350)
        self.canvas = Canvas(self.frame1, bg='#7CCEC9', width=800, height=350, bd=0, highlightthickness=0)
        self.canvas.pack()
        self.draw_pie_charts()
        self.button_image_1 = PhotoImage(file=assets_path / "button_1.png")
        self.button_1 = Button(image=self.button_image_1, borderwidth=0, highlightthickness=0)
        self.button_1.place(x=51.0, y=72.0, width=193.0, height=32.0)
        self.button_image_2 = PhotoImage(file=assets_path / "button_2.png")
        self.button_2 = Button(image=self.button_image_2, borderwidth=0, highlightthickness=0,
                               command=lambda: self.nav.switch_income(path), relief="flat")
        self.button_2.place(x=47.0, y=108.0, width=193.0, height=28.0)
        self.button_image_3 = PhotoImage(file=assets_path / "button_3.png")
        self.button_3 = Button(image=self.button_image_3, borderwidth=0, highlightthickness=0,
                               command=lambda: self.nav.switch_expense(path), relief="flat")
        self.button_3.place(x=45.0, y=139.0, width=192.0, height=33.0)
        self.button_image_4 = PhotoImage(file=assets_path / "button_4.png")
        self.button_4 = Button(image=self.button_image_4, borderwidth=0, highlightthickness=0,
                               command=lambda: self.nav.switch_summary(path), relief="flat")
        self.button_4.place(x=45.0, y=169.0, width=208.0, height=33.0)
        self.button_image_5 = PhotoImage(file=assets_path / "button_5.png")
        self.button_5 = Button(image=self.button_image_5, borderwidth=0, highlightthickness=0,
                               command=lambda: self.nav.switch_login(path), relief="flat")
        self.button_5.place(x=87.0, y=440.0, width=136.0, height=64.0)
    def draw_pie_charts(self):
        income_data, expenses_data = self.file_handler.calculate_income_expenses()
        Icolors = ['#FF9999', '#66B2FF', '#99FF99', '#FFCC99', '#FFD700']
        Ecolors = ['#FFCC99', '#FFD700', '#FF9999', '#99FF99', '#66B2FF']
        self.draw_pie_chart(self.canvas, income_data, "Income Details", x=120, y=175, radius=120, colors=Icolors)
        self.draw_pie_chart(self.canvas, expenses_data, "Expenses Details", x=502, y=175, radius=120, colors=Ecolors)
    def draw_pie_chart(self, canvas, data, title, x, y, radius, colors):
        total = sum(data.values())
        start_angle = 0
        for category, value, color in zip(data.keys(), data.values(), colors):
            angle = 360 * value / total
            canvas.create_arc(x - radius, y - radius, x + radius, y + radius, start=start_angle, extent=angle, fill=color)
            start_angle += angle

        radius_extend, x_axis_extend, x_axis_extend2, y_axis_extend = 5, 20, 25, 10
        legend_x, legend_y = x + radius + radius_extend, y - radius
        for category, value, color in zip(data.keys(), data.values(), colors):
            canvas.create_rectangle(legend_x, legend_y, legend_x + x_axis_extend, legend_y + x_axis_extend, fill=color)
            canvas.create_text(legend_x + x_axis_extend2, legend_y + y_axis_extend, text=f"{category} ({value})",
                               anchor='w')
            legend_y += x_axis_extend2
        canvas.create_text(x + 10, y - radius - 30, text=title, font=('Arial', 14, 'bold'))
