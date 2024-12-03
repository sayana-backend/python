import tkinter as tk
import random

def move_on_button(event):
    no_button.place(x=random.randint(0, window.winfo_width()-no_button.winfo_width()),
                    y=random.randint(0, window.winfo_height() - no_button.winfo_height()))

def yes_action():
    new_window = tk.Toplevel(window)
    new_window.title("Oтвет")
    new_window.geometry("300x100")
    response_label = tk.Label(new_window, text="Я так и думал")
    response_label.pack(pady=20)

window = tk.Tk()
window.title("Вопрос")
window.geometry("400x200")

question_label = tk.Label(window, text="Ты любишь суши?")
question_label.pack(pady=20)

yes_button = tk.Button(window, text="Yes", command=yes_action)
yes_button.pack(side="right", padx=50, pady=20)

no_button = tk.Button(window, text="No")
no_button.pack(side="right", padx=50, pady=20)
no_button.bind("<Enter>", move_on_button)

window.mainloop()


