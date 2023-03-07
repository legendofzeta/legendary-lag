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
window.geometry("300x200")
window.title("Legendary Lag")
window.configure(bg="#2c3e50")

interface_label = tk.Label(window, text="Interface:", font=("Arial", 12), bg="#2c3e50", fg="white")
interface_label.place(x=30, y=10)

interface_entry = tk.Entry(window, font=("Arial", 12))
interface_entry.place(x=130, y=10, width=140)
interface_entry.insert(0, "enp2s0f2") # Default interface value

duration_label = tk.Label(window, text="Duration (s):", font=("Arial", 12), bg="#2c3e50", fg="white")
duration_label.place(x=30, y=50)

duration_entry = tk.Entry(window, font=("Arial", 12))
duration_entry.place(x=130, y=50, width=140)

freeze_button = tk.Button(window, text="Freeze", command=lambda: freeze_network(interface_entry.get(), int(duration_entry.get())), bg="#e74c3c", fg="white")
freeze_button.place(x=30, y=100, width=120, height=40)

unfreeze_button = tk.Button(window, text="Unfreeze", command=lambda: connect_network(interface_entry.get()), bg="#3498db", fg="white")
unfreeze_button.place(x=150, y=100, width=120, height=40)

countdown_label = tk.Label(window, text="", font=("Arial", 16), bg="#2c3e50", fg="white")
countdown_label.place(x=90, y=160)

window.mainloop()
