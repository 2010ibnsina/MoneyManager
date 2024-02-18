from pathlib import Path
from tkinter import *
import csv

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"D:/moneygit/MoneyManager/build/assets/income")

def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

def save_to_csv(income_source, income_amount):
    with open('income_data.csv', mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['Income Source', 'Income Amount'])
        writer.writerow([income_source, income_amount])

def submit_button_clicked():
    income_source = entry_1.get().strip()
    income_amount = entry_2.get().strip()

    if income_source and income_amount:
        save_to_csv(income_source, income_amount)
        print("Data saved to CSV file.")
        warning_label.config(text="Successfully Submitted!!",fg="green")
    else:
        warning_label.place(x=515.0, y=350.0)
        warning_label.config(text="Please provide both Income Source and Income Amount.", fg="red", font=("Poppins", 10))
        # Place the warning label one space later from the button and centered horizontally
        #warning_label.place(x=612.0 + 136.0/2 + 10, y=391.0, anchor="center")

window = Tk()
window.title("Money Manager")
window.geometry("1116x582")
window.geometry("+150+40")
window.configure(bg="#28283F")

canvas = Canvas(
    window,
    bg="#28283F",
    height=582,
    width=1116,
    bd=0,
    highlightthickness=0,
    relief="ridge"
)

image_image_2 = PhotoImage(
    file=relative_to_assets("image_2.png"))
image_2 = canvas.create_image(
    684.0,
    292.0,
    image=image_image_2
)

canvas.place(x=0, y=0)
entry_image_1 = PhotoImage(
    file=relative_to_assets("entry_1.png"))
entry_bg_1 = canvas.create_image(
    680.5,
    149.0,
    image=entry_image_1
)

entry_1 = Entry(
    bd=0,
    bg="#FFFFFF",
    fg="#000716",
    highlightthickness=0
)
entry_1.place(
    x=526.0,
    y=107.0,
    width=309.0,
    height=82.0
)
entry_image_2 = PhotoImage(
    file=relative_to_assets("entry_2.png"))
entry_bg_2 = canvas.create_image(
    680.5,
    289.0,
    image=entry_image_2
)

entry_2 = Entry(
    bd=0,
    bg="#FFFFFF",
    fg="#000716",
    highlightthickness=0
)
entry_2.place(
    x=526.0,
    y=247.0,
    width=309.0,
    height=82.0
)

canvas.create_text(
    503.0,
    69.0,
    anchor="nw",
    text="Enter Income Source",
    fill="#FEFAD9",
    font=("Poppins SemiBold", 18 * -1)
)

canvas.create_text(
    503.0,
    209.0,
    anchor="nw",
    text="Enter Income Amount",
    fill="#FEFAD9",
    font=("Poppins SemiBold", 18 * -1)
)

warning_label = Label(
    window,
    text="",
    bg="#28283F",
    fg="red",
    font=("Poppins", 12)
)
#warning_label.place(x=503.0, y=330.0)

canvas.place(x = 0, y = 0)
image_image_1 = PhotoImage(
    file=relative_to_assets("image_1.png"))
image_1 = canvas.create_image(
    135.0,
    298.0,
    image=image_image_1
)

button_image_1 = PhotoImage(
    file=relative_to_assets("button_1.png"))
button_1 = Button(
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_1 clicked"),
    relief="flat"
)
button_1.place(
    x=50.0,
    y=74.0,
    width=196.0,
    height=33.0
)

button_image_2 = PhotoImage(
    file=relative_to_assets("button_2.png"))
button_2 = Button(
    image=button_image_2,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_2 clicked"),
    relief="flat"
)
button_2.place(
    x=50.0,
    y=111.0,
    width=196.0,
    height=26.0
)

button_image_3 = PhotoImage(
    file=relative_to_assets("button_3.png"))
button_3 = Button(
    image=button_image_3,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_3 clicked"),
    relief="flat"
)
button_3.place(
    x=47.0,
    y=140.0,
    width=196.0,
    height=33.3245849609375
)

button_image_4 = PhotoImage(
    file=relative_to_assets("button_4.png"))
button_4 = Button(
    image=button_image_4,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_4 clicked"),
    relief="flat"
)
button_4.place(
    x=47.0,
    y=167.0,
    width=196.0,
    height=33.0
)

button_image_5 = PhotoImage(
    file=relative_to_assets("button_5.png"))
button_5 = Button(
    image=button_image_5,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_5 clicked"),
    relief="flat"
)
button_5.place(
    x=87.0,
    y=440.0,
    width=136.0,
    height=64.0
)

button_image_6 = PhotoImage(
    file=relative_to_assets("button_6.png"))
button_6 = Button(
    image=button_image_6,
    borderwidth=0,
    highlightthickness=0,
    command=submit_button_clicked,
    relief="flat"
)
button_6.place(
    x=612.0,
    y=391.0,
    width=136.0,
    height=65.46057891845703
)

window.resizable(False, False)
window.mainloop()
