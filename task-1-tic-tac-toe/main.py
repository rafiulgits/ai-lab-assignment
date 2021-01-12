import tkinter as tk
from tkinter import messagebox

window = tk.Tk()
window.title("Tic Tac Toe Bot")

buttons = []


def onButtonClick(btnId):
    btn = buttons[btnId - 1]
    print(btn)
    btn['text'] = '0'
    # messagebox.showwarning("done")


def generateGridBox(row, col, btnId):
    btn = tk.Button(window,
                    text=" ",
                    bg="red",
                    fg="black",
                    height=4,
                    width=8,
                    command=lambda: onButtonClick(btnId))
    btn.grid(row=row, column=col)
    return btn


def boardGenerate():
    btnId = 1
    for row in range(1, 4):
        for col in range(0, 3):
            btn = generateGridBox(row, col, btnId)
            buttons.append(btn)
            btnId = btnId + 1


boardGenerate()

window.mainloop()