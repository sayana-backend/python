import tkinter as tk
import random

class GuessNumberGame:
    def __init__(self, master):
        self.master = master
        master.title("Угадай число")

        self.number = random.randint(1, 100)
        self.guess_count = 0

        self.label = tk.Label(master, text="Угадай чило от 1 до 100")
        self.label.pack()

        self.entry = tk.Entry(master)
        self.entry.pack()

        self.guess_button = tk.Button(master, text="Угадать", command=self.check_guess)
        self.guess_button.pack()

        self.new_game_button = tk.Button(master, text="Новая игра", command=self.new_game)
        self.new_game_button.pack()

        self.result_label = tk.Label(master, text="")
        self.result_label.pack()

    def check_guess(self):
        try:
            guess = int(self.entry.get())
            self.guess_count += 1

            if guess < self.number:
                self.result_label.config(text="Заданное число больше")
            elif guess > self.number:
                self.result_label.config(text="Заланное число меньше")
            else:
                self.result_label.config(text=f"Ура! Вы угадали число {self.number} за {self.guess_count} попыток")
                self.new_game_button.config(state=tk.NORMAL)
                self.guess_button.config(state=tk.DISABLED)
        except ValueError:
            self.result_label.config(text="Пожалуйстаб введите корректное число.")

    def new_game(self):
        self.number = random.randint(1, 100)
        self.guess_count = 0
        self.entry.delete(0, tk.END)
        self.result_label.config(text="")
        self.guess_button.config(state=tk.NORMAL)
        self.new_game_button.config(state=tk.DISABLED)

root = tk.Tk()
game = GuessNumberGame(root)
root.mainloop()
