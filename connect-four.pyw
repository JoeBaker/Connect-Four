import tkinter
from tkinter import messagebox
import random
import os
import functools

class connectFour:
    root = tkinter.Tk()

    colors = {"blue":"#00304A",
        "red":"#F21B3F",
        "yellow":"#EEE82C"}
    coulmn = 0
    grid = [0]*42
    score = [0,0]
    turn = random.choice([-1,1])

    root.title("Connect Four")
    root.geometry("540x540")
    root["bg"] = colors["blue"]
    root.minsize(width=540, height=540)

    def whatColor(turn):
        self = connectFour
        name = {-1:"red", 1:"yellow"}[turn]
        return {"color":self.colors[name], "name":name}

    # def hasWon(g):
    #     for row in range(6):
    #         row *= 7

    #         # Horizontal
    #         for i in range(4):
    #             a = g[row+i] + g[row+i+1] + g[row+i+2] + g[row+i+3]
    #             if a in [-4, 4]:
    #                 return a / 4

    #         # Vertical
    #         if row <= 14:
    #             for i in range(7):
    #                 a = g[row+i] + g[row+i+7] + g[row+i+14] + g[row+i+21]
    #                 if a in [-4, 4]:
    #                     return a / 4

    #     # Diaginal
    #     for row in range(4):
    #         for i in range(3):
    #             i *= 7
    #             a = g[row+i] + g[row+i+8] + g[row+i+16] + g[row+i+24]
    #             b = g[row+i+3] + g[row+i+9] + g[row+i+15] + g[row+i+21]
    #             if a in [-4, 4]:
    #                 return a / 4
    #             if b in [-4, 4]:
    #                 return b / 4

    #     return 0

    # def resetGrid():
    #     for i in range(42):
    #         buttons[i].config(bg=blue)
    #     grid = [0]*42
    #     turn = random.choice([-1,1])

    def fallAnimation():
        self = connectFour
        color = self.whatColor(self, self.turn)
        print(color)
    #     fall = True
    #     column += 7
    #     fall = False
    #     try:
    #         if grid[column] == 0:
    #             fall = True
    #     except: pass
    #     if fall == True:
    #         try:
    #             buttons[column - 7].config(bg=blue)
    #             buttons[column].config(bg=color)
    #         except:
    #             buttons[column].config(bg=color)
    #         text.after(200, fallAnimation)
    #     else:
    #         endAnimation()

    # def endAnimation():
    #     grid[column-7] = turn
    #     won = hasWon(grid)
    #     if won == 1:
    #         score[1] += 1
    #         tkinter.messagebox.showinfo(title="Yellow has won.", message="Yellow has won.")
    #         resetGrid()
    #     elif won == -1:
    #         score[0] += 1
    #         tkinter.messagebox.showinfo(title="Red has won.", message="Red has won.")
    #         resetGrid()
    #     elif won == 0 and 0 not in grid:
    #         tkinter.messagebox.showinfo(title="No one has won.", message="No one has won.")
    #         resetGrid()
    #     turn = 0 - turn
    #     text.config(text="Red's score: "+str(score[0])+"\nYellow's score: "+str(score[1])+"\n"+turnString(turn)+"'s turn")
    #     unlockButtons()

    def lockButtons(self, lock):
        for i in range(42):
            self.buttons[i].config(state={True:"disabled", False:"normal"}[lock])

    def buttonPressed(column):
        self = connectFour
        self.lockButtons(self, True)
        self.text.config(text="Red's score: "+str(self.score[0])+"\nYellow's score: "+str(self.score[1])+"\n")
        if self.grid[column] != 0:
            self.message("You can't go here", "You can't go here because this column is full.\nTry going somewhere else.")
            self.lockButtons(self, False)
        else:
            self.mainGrid.after(200, self.fallAnimation)
    #     while True:
    #         if grid[a] == 0:
    #             text.config(text="Red's score: "+str(score[0])+"\nYellow's score: "+str(score[1])+"\n")
    #             column = a
    #             lockButtons()
    #             buttons[column].config(bg=color)
    #             text.after(200, fallAnimation)
    #             break
    #         else:
    #             a -= 7
    #         if a < 0:
    #             global blue
    #             tkinter.messagebox.showinfo(title="You can't go here.", message="You can't go here because this column is full.\nTry going somewhere else.")
    #             break

    def message(title, text):
        tkinter.messagebox.showinfo(title=title, message=message)

    text = tkinter.Label(text="Red's score: 0\nYellow's score: 0\n"+{-1:"red", 1:"yellow"}[turn]+"'s turn")
    text.config(bg=colors["blue"], fg="white", font="Helvetica 9 bold")
    text.pack()

    mainGrid = tkinter.Frame(bg=colors["blue"])
    mainGrid.pack(expand=True)
    
    buttons = []
    for row in range(6):
        for column in range(7):
            buttons.append(tkinter.Button(mainGrid, height=4, width=8, bg=colors["blue"],
                command=functools.partial(buttonPressed, column)))
            buttons[(row*7)+column].grid(column=column, row=row, padx=5, pady=5)

    try:
        root.iconbitmap(os.path.join(os.path.abspath("."), "assets\icon.ico"))
    except Exception as e: print(e)

connectFour.root.mainloop()
