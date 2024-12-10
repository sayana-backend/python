import tkinter as tk
import random

root = tk.Tk()
root.title("Игра в 15")

SIZE = 4
TILE_SIZE = 100

numbers = list(range(1, SIZE*SIZE))
numbers.append(None)
random.shuffle(numbers)

empty_tile_pos = numbers.index(None)

def move_tile(index):
    global empty_tile_pos
    if (abs(empty_tile_pos - index) == 1 and empty_tile_pos // SIZE == index // SIZE) or abs(empty_tile_pos - index) == SIZE:
        numbers[empty_tile_pos], numbers[index] = numbers[index], numbers[empty_tile_pos]
        empty_tile_pos = index
        update_buttons()

def update_buttons():
    for i, num in enumerate(numbers):
        if num is None:
            buttons[i].config(text="", state=tk.DISABLED)
        else:
            buttons[i].config(text=str(num), state=tk.NORMAL)

buttons = []
for i in range(SIZE * SIZE):
    btn = tk.Button(root, text="", width=4, height=2, font=("Arial", 24),
                    command=lambda i=i: move_tile(i))
    btn.grid(row=i//SIZE, column=i%SIZE)
    buttons.append(btn)

update_buttons()

root.mainloop()