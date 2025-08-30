import tkinter as tk
from time import strftime

# Create main window
root = tk.Tk()
root.title("Digital Clock")

# Function to update time
def time():
    string = strftime('%H:%M:%S %p \n %d-%m-%Y')  # Time + Date
    label.config(text=string)
    label.after(1000, time)  # Refresh every 1 second

# Clock label
label = tk.Label(root, font=('calibri', 50, 'bold'),
                 background='pink', foreground='black')
label.pack(anchor='center')

# Run clock
time()
root.mainloop()
