import tkinter as tk
from tkinter import messagebox
import csv
from datetime import datetime

class MoneyManagerApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Money Manager")
        
        self.balance = 0.00
        self.transactions = []

        # Background color
        background_color = "#003300"  # Mix of blue, black, and green
        self.configure(bg=background_color)

        # Create and pack widgets
        self.label_balance = tk.Label(self, text="Balance: $0.00", bg=background_color, fg="white")
        self.label_balance.pack(pady=10)
        
        self.label_amount = tk.Label(self, text="Amount:", bg=background_color, fg="white")
        self.label_amount.pack()
        self.entry_amount = tk.Entry(self)
        self.entry_amount.pack()

        self.label_category = tk.Label(self, text="Category:", bg=background_color, fg="white")
        self.label_category.pack()
        self.entry_category = tk.Entry(self)
        self.entry_category.pack()

        self.label_date = tk.Label(self, text="Date (Optional):", bg=background_color, fg="white")
        self.label_date.pack()
        self.entry_date = tk.Entry(self)
        self.entry_date.pack()

        # Buttons
        self.button_income = tk.Button(self, text="Add Income", command=self.add_income, bg="orange", fg="white")
        self.button_income.pack(pady=5)

        self.button_expense = tk.Button(self, text="Add Expense", command=self.add_expense, bg="orange", fg="white")
        self.button_expense.pack(pady=5)

        self.listbox_transactions = tk.Listbox(self, height=10, width=50, bg="blue", fg="white")
        self.listbox_transactions.pack(pady=10)

        self.button_delete = tk.Button(self, text="Delete Transaction", command=self.delete_transaction, bg="magenta", fg="white")
        self.button_delete.pack()

        self.button_summary = tk.Button(self, text="View Summary", command=self.view_summary, bg="magenta", fg="white")
        self.button_summary.pack()

        self.button_export = tk.Button(self, text="Export Transactions", command=self.export_transactions, bg="magenta", fg="white")
        self.button_export.pack()

        self.update_balance()

    def add_income(self):
        self.process_transaction("Income")

    def add_expense(self):
        self.process_transaction("Expense")

    def process_transaction(self, transaction_type):
        try:
            amount = float(self.entry_amount.get())
            category = self.entry_category.get()
            date = self.entry_date.get() if self.entry_date.get() else datetime.now().strftime("%Y-%m-%d")
            if amount > 0:
                if transaction_type == "Expense" and amount > self.balance:
                    messagebox.showerror("Error", "Insufficient balance.")
                else:
                    self.balance += amount if transaction_type == "Income" else -amount
                    self.transactions.append((date, transaction_type, category, amount))
                    self.update_balance()
                    self.update_transaction_history()
                    messagebox.showinfo("Success", f"{transaction_type} of ${amount:.2f} added successfully.")
            else:
                messagebox.showerror("Error", "Amount must be greater than zero.")
        except ValueError:
            messagebox.showerror("Error", "Please enter valid amount.")

    def delete_transaction(self):
        selected_index = self.listbox_transactions.curselection()
        if selected_index:
            idx = selected_index[0]
            date, transaction_type, category, amount = self.transactions.pop(idx)
            if transaction_type == "Income":
                self.balance -= amount
            else:
                self.balance += amount
            self.update_balance()
            self.update_transaction_history()

    def view_summary(self):
        total_income = sum(amount for date, t_type, cat, amount in self.transactions if t_type == "Income")
        total_expenses = sum(amount for date, t_type, cat, amount in self.transactions if t_type == "Expense")
        total_profit_loss = total_income - total_expenses
        messagebox.showinfo("Summary", f"Total Income: ${total_income:.2f}\nTotal Expenses: ${total_expenses:.2f}\nProfit/Loss: ${total_profit_loss:.2f}")

    def export_transactions(self):
        filename = tk.filedialog.asksaveasfilename(defaultextension=".csv", filetypes=(("CSV files", "*.csv"), ("All files", "*.*")))
        if filename:
            with open(filename, "w", newline="") as file:
                writer = csv.writer(file)
                writer.writerow(["Date", "Type", "Category", "Amount"])
                writer.writerows(self.transactions)

    def update_balance(self):
        self.label_balance.config(text=f"Balance: ${self.balance:.2f}")

    def update_transaction_history(self):
        self.listbox_transactions.delete(0, tk.END)
        for date, transaction_type, category, amount in self.transactions:
            self.listbox_transactions.insert(tk.END, f"{date}: {transaction_type} - {category} - ${amount:.2f}")

    def run(self):
        self.mainloop()

if __name__ == "__main__":
    app = MoneyManagerApp()
    app.run()
