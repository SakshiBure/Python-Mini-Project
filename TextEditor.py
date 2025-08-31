import tkinter as tk
from tkinter import filedialog, messagebox

# Track current file
current_file = None

def new_file():
    global current_file
    text.delete(1.0, tk.END)
    current_file = None
    root.title("My Text Editor - Untitled")

def open_file():
    global current_file
    file_path = filedialog.askopenfilename(defaultextension=".txt",
                                           filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")])
    if file_path:
        try:
            with open(file_path, 'r', encoding="utf-8") as file:
                text.delete(1.0, tk.END)
                text.insert(tk.END, file.read())
            current_file = file_path
            root.title(f"My Text Editor - {file_path}")
        except Exception as e:
            messagebox.showerror("Error", f"Failed to open file:\n{e}")

def save_file():
    global current_file
    if current_file:  # If already opened/saved before
        try:
            with open(current_file, 'w', encoding="utf-8") as file:
                file.write(text.get(1.0, tk.END).rstrip())
            messagebox.showinfo("Info", "File saved successfully!")
        except Exception as e:
            messagebox.showerror("Error", f"Failed to save file:\n{e}")
    else:
        save_as_file()

def save_as_file():
    global current_file
    file_path = filedialog.asksaveasfilename(defaultextension=".txt",
                                             filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")])
    if file_path:
        try:
            with open(file_path, 'w', encoding="utf-8") as file:
                file.write(text.get(1.0, tk.END).rstrip())
            current_file = file_path
            root.title(f"My Text Editor - {file_path}")
            messagebox.showinfo("Info", "File saved successfully!")
        except Exception as e:
            messagebox.showerror("Error", f"Failed to save file:\n{e}")

# Create main window
root = tk.Tk()
root.title("My Text Editor - Untitled")
root.geometry("800x600")

# Menu
menu = tk.Menu(root)
root.config(menu=menu)

file_menu = tk.Menu(menu, tearoff=False)
menu.add_cascade(label="File", menu=file_menu)
file_menu.add_command(label="New", command=new_file)
file_menu.add_command(label="Open", command=open_file)
file_menu.add_command(label="Save", command=save_file)
file_menu.add_command(label="Save As", command=save_as_file)
file_menu.add_separator()
file_menu.add_command(label="Exit", command=root.quit)

# Text Area
text = tk.Text(root, wrap=tk.WORD, font=("Helvetica", 12), fg="blue", undo=True)
text.pack(expand=True, fill=tk.BOTH)

# Add Scrollbar
scrollbar = tk.Scrollbar(text)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
text.config(yscrollcommand=scrollbar.set)
scrollbar.config(command=text.yview)

# Run App
root.mainloop()
