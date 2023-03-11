import tkinter as tk
import subprocess
import time

def disconnect_network(interface):
    subprocess.run(["nmcli", "dev", "disconnect", interface])

def connect_network(interface):
    subprocess.run(["nmcli", "dev", "connect", interface])

def freeze_network(interface, duration):
    disconnect_network(interface)
    for i in range(duration, 0, -1):
        countdown_label.config(text=f"{i} seconds left")
        window.update()
        time.sleep(1)
    countdown_label.config(text="Done")
    connect_network(interface)

window = tk.Tk()
window.geometry("400x400")
window.title("Legendary Lag")
window.configure(bg="#2c3e50")

title_label = tk.Label(window, text="Legendary Lag", font=("Arial", 24, "bold"), bg="#2c3e50", fg="white")
title_label.pack(pady=20)

interface_frame = tk.Frame(window, bg="#2c3e50")
interface_frame.pack(pady=10)

interface_label = tk.Label(interface_frame, text="Interface:", font=("Arial", 14), bg="#2c3e50", fg="white")
interface_label.pack(side="left", padx=10)

interface_entry = tk.Entry(interface_frame, font=("Arial", 14), width=20)
interface_entry.pack(side="left", padx=10)
interface_entry.insert(0, "enp2s0f2") # Default interface value

duration_frame = tk.Frame(window, bg="#2c3e50")
duration_frame.pack(pady=10)

duration_label = tk.Label(duration_frame, text="Duration (s):", font=("Arial", 14), bg="#2c3e50", fg="white")
duration_label.pack(side="left", padx=10)

duration_entry = tk.Entry(duration_frame, font=("Arial", 14), width=20)
duration_entry.pack(side="left", padx=10)

button_frame = tk.Frame(window, bg="#2c3e50")
button_frame.pack(pady=20)

freeze_button = tk.Button(button_frame, text="Freeze", command=lambda: freeze_network(interface_entry.get(), int(duration_entry.get())), bg="#e74c3c", fg="white", font=("Arial", 14), width=12)
freeze_button.pack(side="left", padx=10)

unfreeze_button = tk.Button(button_frame, text="Unfreeze", command=lambda: connect_network(interface_entry.get()), bg="#3498db", fg="white", font=("Arial", 14), width=12)
unfreeze_button.pack(side="left", padx=10)

credit_label = tk.Label(window, text="Created by LegendaryZeta", font=("Arial", 12), bg="#2c3e50", fg="white")
credit_label.pack(side="bottom", pady=10)

warning_label = tk.Label(window, text="Warning: Do not freeze for more than 8 seconds at a time.", font=("Arial", 12), bg="#2c3e50", fg="white")
warning_label.pack(side="bottom", pady=10)

countdown_label = tk.Label(window, text="", font=("Arial", 16), bg="#2c3e50", fg="white")
countdown_label.pack(pady=30)

window.mainloop()
