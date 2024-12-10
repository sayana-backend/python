import tkinter as tk
import random

# Список слов на русском языке, каждое слово состоит из 6 букв
words = ['арбуз', 'банан', 'лимон', 'носок', 'каблук', 'сосна', 'чашка', 'яблоко', 'лампа', 'кувшин']

word = random.choice(words)
guessed = ['_'] * len(word)
attempts = 6

def update_display():
    display_word.set(' '.join(guessed))
    attempts_left.set(f'Осталось попыток: {attempts}')
    guessed_letters.set(f'Угаданные буквы: {" ".join(guessed)}')

def guess_letter():
    global attempts
    letter = letter_entry.get().lower()
    letter_entry.delete(0, tk.END)

    if letter in word:
        for i, char in enumerate(word):
            if char == letter:
                guessed[i] = letter
    else:
        attempts -= 1

    update_display()

    if '_' not in guessed:
        result.set("Поздравляем! Вы угадали слово!")
        guess_button.config(state=tk.DISABLED)
    elif attempts == 0:
        result.set(f"Вы проиграли! Загаданное слово: {word}")
        guess_button.config(state=tk.DISABLED)

root = tk.Tk()
root.title("Виселица")

display_word = tk.StringVar()
attempts_left = tk.StringVar()
guessed_letters = tk.StringVar()
result = tk.StringVar()

tk.Label(root, textvariable=display_word, font=("Helvetica", 24)).pack(pady=10)
tk.Label(root, textvariable=attempts_left).pack(pady=5)
tk.Label(root, textvariable=guessed_letters).pack(pady=5)
tk.Entry(root, textvariable=result, state='readonly', font=("Helvetica", 18)).pack(pady=5)

tk.Label(root, text="Введите букву:").pack(pady=5)
letter_entry = tk.Entry(root)
letter_entry.pack()

guess_button = tk.Button(root, text="Угадать", command=guess_letter)
guess_button.pack(pady=10)

update_display()

root.mainloop()