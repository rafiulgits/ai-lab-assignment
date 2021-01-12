import tkinter as tk
from tkinter import messagebox
import engine


def onButtonClick(humanSelectedPosition):
    if board[humanSelectedPosition] != 0:
        return
    humanSelectedButton = buttons[humanSelectedPosition]
    humanSelectedButton['text'] = '0'
    humanSelectedButton['state'] = tk.DISABLED
    board[humanSelectedPosition] = -1

    computerSelectedPosition = engine.computeBotTurn(board)
    if computerSelectedPosition == -1:
        resultProcess()
    else:
        computerSelectedButton = buttons[computerSelectedPosition]
        computerSelectedButton['text'] = 'X'
        computerSelectedButton['state'] = tk.DISABLED
        board[computerSelectedPosition] = 1
    if checkIfGameIsOver():
        resultProcess()


def checkIfGameIsOver():
    return engine.analyzer(board) != 0


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
    btnId = 0
    for row in range(1, 4):
        for col in range(0, 3):
            btn = generateGridBox(row, col, btnId)
            buttons.append(btn)
            btnId = btnId + 1


def resultProcess():
    result = engine.analyzer(board)
    if result == 0:
        messagebox.showinfo(title="Result", message="Match Draw")
    elif result == -1:
        messagebox.showinfo(title="Result", message="Human Win!")
    else:
        messagebox.showinfo(title="Result", message="Bot Win!")


def main():
    global window, buttons, board
    window = tk.Tk()
    window.title("Tic Tac Toe Bot")

    buttons = []  #GUI buttons
    board = [0] * 9  #board tracker
    boardGenerate()
    window.mainloop()


if __name__ == '__main__':
    main()
