import tkinter as tk
from datetime import datetime

def show_time():
    current_time = datetime.now().strftime("%I:%M:%S %p")
    time_label.config(text="Current Time: " + current_time)

# Create window
root = tk.Tk()
root.title("IPA TIME ENNANU SOLLANUMA")
root.geometry("600x400")

# Heading
heading = tk.Label(root, text="IPA CURRENT TIME ",
                   font=("Arial", 20, "bold"))
heading.pack(pady=20)

# Button
button = tk.Button(root, text="CLICK PANNUGA GUYS TIME SOLLUREN",
                   font=("Arial", 14),
                   command=show_time)
button.pack(pady=15)

# Display time
time_label = tk.Label(root, text="Click the button!",
                      font=("Arial", 16))
time_label.pack(pady=20)

root.mainloop()