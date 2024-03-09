from tkinter import *
from datetime import datetime
import pytz
import math
from PIL import Image, ImageTk

def get_bangladesh_time():
    bangladesh_time = datetime.now(pytz.timezone('Asia/Dhaka'))
    return bangladesh_time.strftime("%I:%M %p")

def get_greeting():
    current_hour = datetime.now(pytz.timezone('Asia/Dhaka')).hour
    if 6 <= current_hour < 12:
        return "Good Morning"
    elif 12 <= current_hour < 15:
        return "Good Noon"  # Add the new option for Good Noon
    elif 15 <= current_hour < 17:
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
    income_data = {'Salary': 400, 'Freelance': 1500, 'Investment': 800, 'Other': 200}
    expenses_data = {'Rent': 1000, 'Food': 600, 'Transport': 400, 'Entertainment': 300, 'Others': 300}
    return income_data, expenses_data

def draw_pie_chart(canvas, data, title, x, y, radius, colors):
    total = sum(data.values())
    start_angle = 0

    for category, value, color in zip(data.keys(), data.values(), colors):
        angle = 360 * value / total
        canvas.create_arc(x - radius, y - radius, x + radius, y + radius, start=start_angle, extent=angle,
                          fill=color)
        start_angle += angle

    # Draw legend
    legend_x, legend_y = x + radius + 20, y - radius
    for category, value, color in zip(data.keys(), data.values(), colors):
        canvas.create_rectangle(legend_x, legend_y, legend_x + 20, legend_y + 20, fill=color)
        canvas.create_text(legend_x + 25, legend_y + 10, text=f"{category} ({value})", anchor='w')
        legend_y += 25

    # Draw title
    canvas.create_text(x, y - radius - 30, text=title, font=('Arial', 14, 'bold'))

def win():
    window = Tk()
    window.title("Money Manager")
    window.geometry("1116x582")
    window.geometry("+150+40")
    window.configure(bg="#28283F")
    window.resizable(False,False)

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
    logo.place(x=15, y=8)
    # User name
    cname = Label(header, text='Ratin Sharafat', fg='#BD2EEF', bg='#C07BB5', font=("", 15, "bold"))
    cname.place(x=53, y=15)

    #sidebar
    # Sidebar
    sidebar = Frame(window, bg='#151A21')
    sidebar.place(x=0, y=0, width=290, height=582)

   # Add image to the sidebar
    image_path = r"D:\New folder\expense\image_1.png"
    img_sidebar = Image.open(image_path)
    img_sidebar = img_sidebar.resize((300, 750))  # Resize the image if needed
    photo_sidebar = ImageTk.PhotoImage(img_sidebar)
    image_label = Label(sidebar, image=photo_sidebar, bg='#151A21')
    image_label.image = photo_sidebar
    image_label.place(x=0, y=5)
    
    #buttons section
    # Buttons section
    

# Add buttons to the buttons section
    button_paths = [
      r"D:\New folder\expense\button_1.png",
      r"D:\New folder\expense\button_2.png",
      r"D:\New folder\expense\button_3 .png",
      r"D:\New folder\expense\button_4.png",
      r"D:\New folder\expense\button_5.png"
]

    button_images = []
    for i, button_path in enumerate(button_paths):
     img_button = Image.open(button_path)
     img_button = img_button.resize((189, 26))  # Resize the button image if needed
     photo_button = ImageTk.PhotoImage(img_button)
     button_images.append(photo_button)
     button_label = Label(image_label, image=photo_button, bg='#151A21')
     button_label.image = photo_button
     button_label.place(x=50, y=95 + i * 70)

    

    
    
    

    # Body
    #heading = Label(window, text='Dashboard', font=("", 13, "bold"), fg='#0064d3', bg='#170422')
    #heading.place(x=325, y=70)

    # Frame 1
    frame1 = Frame(window, bg='#7CCEC9')
    frame1.place(x=300, y=70, width=800, height=350)

    # Calculate income and expenses
    income_data, expenses_data = calculate_income_expenses()

    # Create a canvas for drawing pie charts
    canvas = Canvas(frame1, bg='#7CCEC9', width=800, height=350, bd=0, highlightthickness=0)
    canvas.pack()

    # Define colors for the pie chart slices
    income_colors = ['#FF9999', '#66B2FF', '#99FF99', '#FFCC99']
    expenses_colors = ['#FF9999', '#66B2FF', '#99FF99', '#FFCC99', '#FFD700']

    # Draw pie charts with specified colors
    draw_pie_chart(canvas, income_data, "Income Details", 135, 175, 125, income_colors)
    draw_pie_chart(canvas, expenses_data, "Expenses Details", 520, 175, 125, expenses_colors)

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
