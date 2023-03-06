import tkinter as tk
import subprocess
import time

def disable_eth():
    subprocess.run(["nmcli", "dev", "disconnect", "enp2s0f2"])

def enable_eth():
    subprocess.run(["nmcli", "dev", "connect", "enp2s0f2"])

def freeze_eth():
    disable_eth()
    countdown_label.config(text="8 seconds left")
    window.update()
    time.sleep(1)
    countdown_label.config(text="7 seconds left")
    window.update()
    time.sleep(1)
    countdown_label.config(text="6 seconds left")
    window.update()
    time.sleep(1)
    countdown_label.config(text="5 seconds left")
    window.update()
    time.sleep(1)
    countdown_label.config(text="4 seconds left")
    window.update()
    time.sleep(1)
    countdown_label.config(text="3 seconds left")
    window.update()
    time.sleep(1)
    countdown_label.config(text="2 seconds left")
    window.update()
    time.sleep(1)
    countdown_label.config(text="1 seconds left")
    window.update()
    time.sleep(1)
    countdown_label.config(text="Done")
    enable_eth()

window = tk.Tk()
window.geometry("250x150")
window.title("Legendary Lag")
window.configure(bg="#2c3e50")

freeze_button = tk.Button(window, text="Freeze", command=freeze_eth, bg="#e74c3c", fg="white")
freeze_button.place(x=30, y=50, width=80, height=40)

unfreeze_button = tk.Button(window, text="Unfreeze", command=enable_eth, bg="#3498db", fg="white")
unfreeze_button.place(x=140, y=50, width=80, height=40)

countdown_label = tk.Label(window, text="", font=("Arial", 16), bg="#2c3e50", fg="white")
countdown_label.place(x=60, y=100)

window.mainloop()
