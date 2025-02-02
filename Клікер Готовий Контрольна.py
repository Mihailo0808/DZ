import tkinter as tk

click = 0
multiplier = 1
def update_multiplier_button_text():
    cost = 5 * (2 ** (multiplier - 1))
    multiplier_button.config(text=f"Купити +1 до кліків ({cost} кліків)")
def clicker():
    global click
    click += 1 * multiplier
    title_label.config(text=f"Кліків: {click}")
def buy_multiplier():
    global click, multiplier
    cost = 5 * (2 ** (multiplier - 1))
    if click >= cost:
        click -= cost
        multiplier += 1
        title_label.config(text=f"Кліків: {click}")
        update_multiplier_button_text()
def buy_large_multiplier():
    global click, multiplier
    cost = 50000
    if click >= cost:
        multiplier = 1
        click = 0
        multiplier *= 2
        title_label.config(text=f"Кліків: {click}")
        update_multiplier_button_text()
root = tk.Tk()
root.title("Clicker")
frame = tk.Frame(root, bg='#00a1ff', padx=60, pady=30)
frame.pack(expand=True)
title_label = tk.Label(frame, text=f"Кліків: {click}", font=("Arial", 16, "bold"), fg='yellow', bg='#00a1ff')
title_label.pack(pady=10)
click_button = tk.Button(frame, text="Клікай мене!", font=("Arial", 14), bg='yellow', padx=20, pady=5, command=clicker)
click_button.pack(pady=10)
multiplier_button = tk.Button(frame, text="", command=buy_multiplier, font=("Arial", 12),  bg='green')
multiplier_button.pack(pady=5)
update_multiplier_button_text()
large_multiplier_button = tk.Button(frame, text="Все спочатку (50 тисяч кліків)", font=("Courier", 12), command=buy_large_multiplier, bg='red')
large_multiplier_button.pack(pady=5)
root.resizable(False, False)
root.mainloop()