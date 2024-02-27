from pathlib import Path
from tkinter import *
import csv
from tkinter import messagebox

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"D:\moneymanage\MoneyManager\build\assets\expense")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

def submit_expense():
    # Retrieve expense reason and amount entered by the user
    reason = entry_1.get()
    amount = entry_2.get()

    # Check if both reason and amount are provided
    if not reason or not amount:
        messagebox.showwarning("Warning", "Please fill in both Expense reason and Expense amount.", icon='warning')
        return

    # Write the expense details to a CSV file
    with open('expenses.csv', 'a', newline='') as csvfile:
        fieldnames = ['Reason', 'Amount']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        # Write the header if the file is empty
        if csvfile.tell() == 0:
            writer.writeheader()

        writer.writerow({'Reason': reason, 'Amount': amount})

    # Clear the entry fields after submission
    entry_1.delete(0, 'end')
    entry_2.delete(0, 'end')

    # Show a message to the user indicating successful submission
    messagebox.showinfo("Success", "Submitted successfully", icon='info')


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

canvas.place(x=0, y=0)

image_image_1 = PhotoImage(
    file=relative_to_assets("image_1.png"))
image_1 = canvas.create_image(
    134.0,
    367.0,
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
    x=51.0,
    y=107.0,
    width=189.0,
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
    x=53.0,
    y=139.0,
    width=193.0,
    height=32.0
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
    y=173.0,
    width=196.0,
    height=31.0
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

canvas.create_rectangle(
    486.0,
    46.0,
    881.0,
    539.0,
    fill="#28283F",
    outline="")

image_image_2 = PhotoImage(
    file=relative_to_assets("image_2.png"))
image_2 = canvas.create_image(
    684.0,
    292.0,
    image=image_image_2
)

button_image_6 = PhotoImage(
    file=relative_to_assets("button_6.png"))
button_6 = Button(
    image=button_image_6,
    borderwidth=0,
    highlightthickness=0,
    command=submit_expense,  # Call submit_expense function when clicked
    relief="flat"
)
button_6.place(
    x=612.0,
    y=391.0,
    width=136.0,
    height=65.46057891845703
)

canvas.create_rectangle(
    503.0,
    107.0,
    858.0,
    191.0,
    fill="#454567",
    outline="")

canvas.create_rectangle(
    503.0,
    247.0,
    858.0,
    331.0,
    fill="#454567",
    outline="")

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
    text="Enter Expense Reason",
    fill="#FEFAD9",
    font=("Poppins SemiBold", 18 * -1)
)

canvas.create_text(
    503.0,
    209.0,
    anchor="nw",
    text="Enter Expense Amount",
    fill="#FEFAD9",
    font=("Poppins SemiBold", 18 * -1)
)
window.resizable(False, False)
window.mainloop()
