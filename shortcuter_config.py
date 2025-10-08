# This is a theoretical example of a GUI application to configure the Shortcuter device. I do not have access to the actual hardware or its specific commands, so this code is illustrative only.
# I will complete the code when I have the hardware wired up and can test it.

import serial
import time
import tkinter as tk
from tkinter import filedialog, messagebox

PORT = "COM5"  # Change this to your Arduino port
BAUD = 115200

ser = serial.Serial(PORT, BAUD, timeout=1)
time.sleep(2)

def send(cmd):
    ser.write((cmd + "\n").encode())
    time.sleep(0.05)
    reply = ser.readline().decode().strip()
    print("Arduino:", reply)

def set_button():
    try:
        page = int(page_entry.get()) - 1
        btn = int(btn_entry.get()) - 1
    except:
        messagebox.showerror("Error", "Enter valid numbers for page and button")
        return
    action = action_entry.get().strip()
    icon = filedialog.askopenfilename(title="Select Icon", filetypes=[("Images", "*.jpg *.png")])
    if not icon: return
    icon_name = icon.split("/")[-1]
    send(f"SET {page} {btn} {action} {icon_name}")

def save():
    send("SAVE")
    messagebox.showinfo("Shortcuter", "Configuration saved to device.")

root = tk.Tk()
root.title("Shortcuter Configurator")

tk.Label(root, text="Page (1-3):").grid(row=0, column=0)
page_entry = tk.Entry(root)
page_entry.grid(row=0, column=1)

tk.Label(root, text="Button (1-12):").grid(row=1, column=0)
btn_entry = tk.Entry(root)
btn_entry.grid(row=1, column=1)

tk.Label(root, text="Action:").grid(row=2, column=0)
action_entry = tk.Entry(root)
action_entry.grid(row=2, column=1)

tk.Button(root, text="Set Button", command=set_button).grid(row=3, column=0, columnspan=2, pady=10)
tk.Button(root, text="Save Config", command=save).grid(row=4, column=0, columnspan=2, pady=10)

root.mainloop()
