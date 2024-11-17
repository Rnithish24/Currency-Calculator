from currency_converter import CurrencyConverter
import tkinter as tk

# Create CurrencyConverter instance
c = CurrencyConverter()

# Initialize main window
window = tk.Tk()
window.geometry("500x360")
window.title("Currency Converter")

# Function to perform currency conversion
def clicked():
    try:
        # Get values from input fields
        amount = float(entry1.get())
        cur1 = entry2.get().strip().upper()
        cur2 = entry3.get().strip().upper()

        # Convert currency and update the label
        converted_amount = c.convert(amount, cur1, cur2)
        result_label.config(text=f"{amount} {cur1} = {converted_amount:.2f} {cur2}")
    except Exception as e:
        result_label.config(text=f"Error: {e}")

# Create labels and input fields
tk.Label(window, text="Currency Converter", font="Arial 20 italic bold").pack(pady=10)

tk.Label(window, text="Enter amount here:", font="Times 16 bold").place(x=70, y=80)
entry1 = tk.Entry(window)
entry1.place(x=270, y=85)

tk.Label(window, text="Enter your currency here:", font="Times 16 bold").place(x=20, y=130)
entry2 = tk.Entry(window)
entry2.place(x=270, y=135)

tk.Label(window, text="Enter your desired currency:", font="Times 16 bold").place(x=10, y=180)
entry3 = tk.Entry(window)
entry3.place(x=270, y=185)

# Add button and result label
tk.Button(window, text="Convert", font="Times 16 bold", command=clicked).place(x=220, y=230)

result_label = tk.Label(window, text="", font="Times 16 bold")
result_label.place(x=100, y=280)

# Start the GUI event loop
window.mainloop()
