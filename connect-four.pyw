import tkinter
from tkinter import messagebox
import random
import os

class connectFour:
    root = tkinter.Tk()

    colors = {"Blue":"#00304A",
        "Red":"#F21B3F",
        "Yellow":"#EEE82C"}
    grid = [0]*42
    score = [0,0]
    turn = random.choice([-1,1])

    root.title("Connect Four")
    root.geometry("540x540")
    root["bg"] = colors["Blue"]
    root.minsize(width=540, height=540)

    def whatColor(self):
        name = {-1:"Red", 1:"Yellow"}[self.turn]
        return {"hex":self.colors[name], "name":name, "turn":self.turn}

    def hasWon(g):
        for row in range(6):
            row *= 7
            # Horizontal
            for i in range(4):
                a = g[row+i] + g[row+i+1] + g[row+i+2] + g[row+i+3]
                if a in [-4, 4]:
                    return a / 4
            # Vertical
            if row <= 14:
                for i in range(7):
                    a = g[row+i] + g[row+i+7] + g[row+i+14] + g[row+i+21]
                    if a in [-4, 4]:
                        return a / 4
        # Diaginal
        for row in range(4):
            for i in range(3):
                i *= 7
                a = g[row+i] + g[row+i+8] + g[row+i+16] + g[row+i+24]
                b = g[row+i+3] + g[row+i+9] + g[row+i+15] + g[row+i+21]
                if a in [-4, 4]:
                    return a / 4
                if b in [-4, 4]:
                    return b / 4
        return 0

    def resetGrid(self):
        for i in range(42):
            self.buttons[i].config(bg=self.colors["Blue"])
        self.grid = [0]*42

    def fallAnimation(self, place):
        color = self.whatColor(self)
        if not place < 7:
            self.buttons[place - 7].config(bg=self.colors["Blue"])
        self.buttons[place].config(bg=color["hex"])
        if self.grid[place + 7:place + 8] == [0]:
            place += 7
            self.mainGrid.after(300, lambda: self.fallAnimation(self, place))
        else:
            self.grid[place] = self.turn
            self.endAnimation(self, place, color)

    def endAnimation(self, place, color):
        won = self.hasWon(self.grid)
        self.lockButtons(self, False)
        if won != 0 or 0 not in self.grid:
            if won != 0:
                title = color["name"] + " has won"
                scoreID = int((self.turn+3)/2-1)
                self.score[scoreID] += 1
                message = title + ("\nRed's score: "+str(self.score[0])+
                    "\nYellow's score: "+str(self.score[1]))
            else:
                title, message = ["No one has won"]*2
            self.text.config(text="Red's score: "+str(self.score[0])+
                "\nYellow's score: "+str(self.score[1])+"\n")
            self.message(title, message)
            self.resetGrid(self)
        self.turn = 0 - self.turn
        self.text.config(text="Red's score: "+str(self.score[0])+"\nYellow's score: "+
            str(self.score[1])+"\n"+{-1:"Red", 1:"Yellow"}[self.turn]+"'s turn")

    def lockButtons(self, lock):
        for i in range(42):
            self.buttons[i].config(state={True:"disabled", False:"normal"}[lock])

    def buttonPressed(column):
        self = connectFour
        self.lockButtons(self, True)
        self.text.config(text="Red's score: "+str(self.score[0])+"\nYellow's score: "+str(self.score[1])+"\n")
        if self.grid[column] != 0:
            self.message("You can't go here", "You can't go here because this column is full."+
                "\nTry going somewhere else.")
            self.lockButtons(self, False)
        else:
            self.fallAnimation(self, column)

    def message(title, message):
        tkinter.messagebox.showinfo(title=title, message=message)

    text = tkinter.Label(text="Red's score: 0\nYellow's score: 0\n"+{-1:"Red", 1:"Yellow"}[turn]+"'s turn")
    text.config(bg=colors["Blue"], fg="white", font="Helvetica 9 bold")
    text.pack()

    mainGrid = tkinter.Frame(bg=colors["Blue"])
    mainGrid.pack(expand=True)
    
    buttons = []
    for row in range(6):
        for column in range(7):
            buttons.append(tkinter.Button(mainGrid, height=4, width=8, bg=colors["Blue"],
                command=lambda arg=column: connectFour.buttonPressed(arg)))
            buttons[(row*7)+column].grid(column=column, row=row, padx=5, pady=5)

    try:
        root.iconbitmap(os.path.join(os.path.abspath("."), "assets\icon.ico"))
    except Exception as e: print(e)

connectFour.root.mainloop()
