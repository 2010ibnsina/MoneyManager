from tkinter import *
from PIL import Image, ImageTk
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from datetime import datetime
import pytz

def get_bangladesh_time():
    bangladesh_time = datetime.now(pytz.timezone('Asia/Dhaka'))
    return bangladesh_time.strftime("%I:%M %p")

def get_greeting():
    current_hour = datetime.now(pytz.timezone('Asia/Dhaka')).hour
    if 6 <= current_hour < 12:
        return "Good Morning"
    elif 12 <= current_hour < 17:
        return "Good Afternoon"
    elif 17 <= current_hour < 20:
        return "Good Evening"
    elif 20 <= current_hour < 24:
        return "Good Night"
    else:
        return "Good Night"

def calculate_income_expenses():
    # This function should fetch the data for income and expenses dynamically
    # For this example, I'll return static sample data
    income_data = {'Salary': 4000, 'Freelance': 1500, 'Investment': 800, 'Other': 200}
    expenses_data = {'Rent': 1000, 'Food': 600, 'Transport': 400, 'Entertainment': 300, 'Others': 300}
    return income_data, expenses_data

def win():
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
    canvas.pack()

    # Header
    header = Frame(window, bg='#C07BB5')
    header.place(x=300, y=0, width=800, height=50)

    # Greeting text (in red)
    greeting_text = Label(header, text=f"{get_greeting()}", font=("Pacifico", 14, "bold"), fg='#1789CA', bg='#C07BB5')
    greeting_text.place(x=350, y=5)

    # Time text (in blue)
    time_text = f'It\'s {get_bangladesh_time()}'
    time_label = Label(header, text=time_text, font=("Pacifico", 14, "bold"), fg='#0000FF', bg='#C07BB5')
    time_label.place(x=640, y=5)

    # Profile
    filename = r"D:\New folder\images\avatar_7235981.png"
    img = Image.open(filename)
    photo = ImageTk.PhotoImage(img)
    logo = Label(header, image=photo, bg='red')
    logo.image = photo
    logo.place(x=30, y=8)

    # User name
    cname = Label(header, text='Ratin Sharafat', fg='#BD2EEF', bg='#C07BB5', font=("", 14, "bold"))
    cname.place(x=75, y=12)

    # Sidebar
    sidebar = Frame(window, bg='#1C1221')
    sidebar.place(x=0, y=0, width=300, height=750)

    # Body
    #heading = Label(window, text='Dashboard', font=("", 13, "bold"), fg='#0064d3', bg='#170422')
    #heading.place(x=325, y=70)

    # Frame 1
    frame1 = Frame(window, bg='#7CCEC9')
    frame1.place(x=300, y=70, width=800, height=350)

    # Calculate income and expenses
    income_data, expenses_data = calculate_income_expenses()

    # Create a figure and two subplots
    fig, (ax1, ax2) = plt.subplots(1, 2)

    # Pie Chart for Income
    labels_income = list(income_data.keys())
    sizes_income = list(income_data.values())
    ax1.pie(sizes_income, labels=labels_income, autopct='%1.1f%%', startangle=90)
    ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle
    ax1.set_title('Income Details')  # Add title to the pie chart

    # Pie Chart for Expenses
    labels_expenses = list(expenses_data.keys())
    sizes_expenses = list(expenses_data.values())
    ax2.pie(sizes_expenses, labels=labels_expenses, autopct='%1.1f%%', startangle=90)
    ax2.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle
    ax2.set_title('Expenses Details')  # Add title to the pie chart

    # Embedding each subplot into a Tkinter canvas
    canvas_income = FigureCanvasTkAgg(fig, master=frame1)
    canvas_income.draw()
    canvas_income.get_tk_widget().pack(side=LEFT, padx=5, pady=10, expand=True)

    # Frame 2
    frame2 = Frame(window, bg='#F6636B')
    frame2.place(x=300, y=430, width=210, height=148)

    # Label for "Total Users"
    total_users_label = Label(frame2, text='Total Users', font=("", 15, "bold"), fg='#5154A1', bg='#F6636B')
    total_users_label.place(x=40, y=20)

    # Label for total count
    total_count_label = Label(frame2, text='100', font=("", 25, "bold"), fg='#2ACF94', bg='#F6636B')
    total_count_label.place(x=80, y=60)

    # Frame 3
    frame3 = Frame(window, bg='#EA2EFB')
    frame3.place(x=600, y=430, width=210, height=148)

    # Calculate the most income-earning source
    most_income_source = max(income_data, key=income_data.get)
    most_income_amount = income_data[most_income_source]

    # Display the most income-earning source and its amount
    most_income_label = Label(frame3, text=f"Most Income Source\n\n{most_income_source}\n\nAmount: {most_income_amount}",
                              font=("bold", 15), fg='blue', bg='#EA2EFB')
    most_income_label.place(x=100, y=70, anchor=CENTER)

    # Frame 4
    frame4 = Frame(window, bg='#3462D9')
    frame4.place(x=890, y=430, width=210, height=148)

    # Calculate the most expense source
    most_expense_source = max(expenses_data, key=expenses_data.get)
    most_expense_amount = expenses_data[most_expense_source]

    # Display the most expense source and its amount
    most_expense_label = Label(frame4,
                               text=f"Most Expense Source\n\n{most_expense_source}\n\nAmount: {most_expense_amount}",
                               font=("bold", 15), fg='#FFFFFF', bg='#3462D9')
    most_expense_label.place(x=110, y=70, anchor=CENTER)

    window.mainloop()

if __name__ == '__main__':
    win()
