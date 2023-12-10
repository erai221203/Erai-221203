import tkinter as tk
from tkinter import messagebox
from datetime import datetime


def calculate_total():
    # Calculate the total amount based on the items and quantities
    by_price = float(by_price_entry.get())
    by_quantity = int(by_quantity_entry.get())
    by_total = by_price * by_quantity

    soap_price = float(soap_price_entry.get())
    soap_quantity = int(soap_quantity_entry.get())
    soap_total = soap_price * soap_quantity

    # Calculate the overall total
    total = by_total + soap_total

    # Update the total label
    total_label.config(text="Total: $%.2f" % total)

def print_bill():
    # Get the current date and time
    current_datetime = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    # Get the item details and quantities
    by_quantity = int(by_quantity_entry.get())
    soap_quantity = int(soap_quantity_entry.get())

    # Calculate the total amount
    by_total = float(by_price_entry.get()) * by_quantity
    soap_total = float(soap_price_entry.get()) * soap_quantity
    total_amount = by_total + soap_total

    # Generate the bill
    bill = f"==== Bill ====\n\nDate: {current_datetime}\n\n"
    bill += f"Item\t\tQuantity\t\tPrice\t\tTotal\n"
    bill += f"------------------------------------------------------\n"
    bill += f"by\t\t{by_quantity}\t\t\t{by_price}\t\t{by_total}\n"
    bill += f"Soap\t\t{soap_quantity}\t\t\t{soap_price}\t\t{soap_total}\n"
    bill += f"------------------------------------------------------\n"
    bill += f"Total Amount:\t\t\t\t\t\t{total_amount}\n"

    # Show the bill in a message box
    messagebox.showinfo("Bill", bill)

# Create the main window
root = tk.Tk()
root.title("Billing Software")

# Create labels for the items
by_label = tk.Label(root, text="by:", bg="lightgray")
by_label.pack()

soap_label = tk.Label(root, text="Soap:", bg="lightgray")
soap_label.pack()

# Create entry fields for item prices
by_price_entry = tk.Entry(root)
by_price_entry.pack()

soap_price_entry = tk.Entry(root)
soap_price_entry.pack()

# Create entry fields for item quantities
by_quantity_entry = tk.Entry(root)
by_quantity_entry.pack()

soap_quantity_entry = tk.Entry(root)
soap_quantity_entry.pack()

# Set default values for item prices
by_price_entry.insert(0, "100.00")
soap_price_entry.insert(0, "50.00")

# Set default values for item quantities
by_quantity_entry.insert(0, "1")
soap_quantity_entry.insert(0, "2")

# Create a button to calculate the total
calculate_button = tk.Button(root, text="Calculate", command=calculate_total)
calculate_button.pack()

# Create a label to display the total
total_label = tk.Label(root, text="Total: $0.00", bg="lightgray")
total_label.pack()

# Create a button to print the bill
print_button = tk.Button(root, text="Print Bill", command=print_bill)
print_button.pack()

root.mainloop()
