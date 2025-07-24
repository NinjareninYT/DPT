import tkinter as tk
from tkinter import messagebox, simpledialog
import os

FILENAME = "pins.txt"

# --- File Handling Functions ---
def load_pins():
    if not os.path.exists(FILENAME):
        return []
    with open(FILENAME, "r") as file:
        return [line.strip() for line in file.readlines()]

def save_pins(pins):
    with open(FILENAME, "w") as file:
        for pin in pins:
            file.write(pin + "\n")

# --- GUI Functions ---
def refresh_listbox():
    pin_listbox.delete(0, tk.END)
    for pin in pins:
        pin_listbox.insert(tk.END, pin)

def add_pin():
    pin = simpledialog.askstring("Add Pin", "Enter the pin name or ID:")
    if pin:
        pins.append(pin.strip())
        save_pins(pins)
        refresh_listbox()

def remove_pin():
    selected = pin_listbox.curselection()
    if not selected:
        messagebox.showwarning("No selection", "Please select a pin to remove.")
        return
    index = selected[0]
    pin = pins.pop(index)
    save_pins(pins)
    refresh_listbox()
    messagebox.showinfo("Removed", f"Removed pin: {pin}")

# --- Main App Window ---
app = tk.Tk()
app.title("Disney Pin Collector")
app.geometry("400x400")
app.resizable(False, False)

pins = load_pins()

# --- Widgets ---
title_label = tk.Label(app, text="🎉 Your Disney Pins", font=("Arial", 16))
title_label.pack(pady=10)

pin_listbox = tk.Listbox(app, width=50, height=15)
pin_listbox.pack(pady=5)
refresh_listbox()

button_frame = tk.Frame(app)
button_frame.pack(pady=10)

add_button = tk.Button(button_frame, text="Add Pin", command=add_pin, width=15)
add_button.pack(side=tk.LEFT, padx=5)

remove_button = tk.Button(button_frame, text="Remove Selected", command=remove_pin, width=15)
remove_button.pack(side=tk.LEFT, padx=5)

# --- Run App ---
app.mainloop()
