import tkinter
from tkinter import messagebox
from random import choice
import os

blue = "#00304A"
red = "#F21B3F"
yellow = "#EEE82C"
color = ""
coulmn = 0
grid = [0]*42
score = [0,0]
turn = choice([-1,1])
root = tkinter.Tk()

def whatColor():
    global turn
    if turn == -1:
        return red
    return yellow

def turnString(a):
    if a == -1:
        return "red"
    return "yellow"

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

    

def resetGrid():
    global blue
    global buttons
    global grid
    global turn
    for i in range(42):
        buttons[i].config(bg=blue)
    grid = [0]*42
    turn = choice([-1,1])

def fallAnimation():
    global buttons
    global color
    global blue
    global grid
    global column
    global mainGrid
    fall = True
    column += 7
    try:
        if not grid[column] == 0:
            fall = False
    except:
        fall = False
    if fall == True:
        try:
            buttons[column - 7].config(bg=blue)
            buttons[column].config(bg=color)
        except:
            buttons[column].config(bg=color)
        text.after(200, fallAnimation)
    else:
        endAnimation()

def lockButtons():
    global buttons
    for i in range(42):
        buttons[i].config(command=nothing)
        

def unlockButtons():
    global buttons
    for i in range(6):
        buttons[(i*7)].config(command=c1)
        buttons[(i*7)+1].config(command=c2)
        buttons[(i*7)+2].config(command=c3)
        buttons[(i*7)+3].config(command=c4)
        buttons[(i*7)+4].config(command=c5)
        buttons[(i*7)+5].config(command=c6)
        buttons[(i*7)+6].config(command=c7)

def endAnimation():
    global buttons
    global color
    global blue
    global grid
    global column
    global text
    global mainGrid
    global turn
    grid[column-7] = turn
    won = hasWon(grid)
    if won == 1:
        score[1] += 1
        tkinter.messagebox.showinfo(title="Yellow has won.", message="Yellow has won.")
        resetGrid()
    elif won == -1:
        score[0] += 1
        tkinter.messagebox.showinfo(title="Red has won.", message="Red has won.")
        resetGrid()
    elif won == 0 and 0 not in grid:
        tkinter.messagebox.showinfo(title="No one has won.", message="No one has won.")
        resetGrid()
    turn = 0 - turn
    text.config(text="Red's score: "+str(score[0])+"\nYellow's score: "+str(score[1])+"\n"+turnString(turn)+"'s turn")
    unlockButtons()

def buttonPressed(a):
    global grid
    global buttons
    global text
    global turn
    global score
    global color
    color = whatColor()
    global column
    while True:
        if grid[a] == 0:
            text.config(text="Red's score: "+str(score[0])+"\nYellow's score: "+str(score[1])+"\n")
            column = a
            lockButtons()
            buttons[column].config(bg=color)
            text.after(200, fallAnimation)
            break
        else:
            a -= 7
        if a < 0:
            global blue
            tkinter.messagebox.showinfo(title="You can't go here.", message="You can't go here because this column is full.\nTry going somewhere else.")
            break

def c1():
    buttonPressed(0)

def c2():
    buttonPressed(1)

def c3():
    buttonPressed(2)

def c4():
    buttonPressed(3)

def c5():
    buttonPressed(4)

def c6():
    buttonPressed(5)

def c7():
    buttonPressed(6)

def nothing():
    pass
		
mainGrid = tkinter.Frame(bg=blue)
buttons = []

text = tkinter.Label(text="Red's score: 0\nYellow's score: 0\n"+turnString(turn)+"'s turn", bg=blue, fg="white", font="Helvetica 9 bold")

for i in range(6):
    buttons.append(tkinter.Button(mainGrid, height=4, width=8, bg=blue, command=c1))
    buttons.append(tkinter.Button(mainGrid, height=4, width=8, bg=blue, command=c2))
    buttons.append(tkinter.Button(mainGrid, height=4, width=8, bg=blue, command=c3))
    buttons.append(tkinter.Button(mainGrid, height=4, width=8, bg=blue, command=c4))
    buttons.append(tkinter.Button(mainGrid, height=4, width=8, bg=blue, command=c5))
    buttons.append(tkinter.Button(mainGrid, height=4, width=8, bg=blue, command=c6))
    buttons.append(tkinter.Button(mainGrid, height=4, width=8, bg=blue, command=c7))

text.pack()
mainGrid.pack(expand=True)

a = 0
for i in range(6):
    for x in range(7):
        buttons[a].grid(column=x, row=i, padx=5, pady=5)
        a += 1

def path(relativePath):
     return os.path.join(os.path.abspath("."), relativePath)

try:
    root.iconbitmap(path("assets\icon.ico"))
except Exception as e:
    print(e)
root.title("Connect Four")
root.geometry("540x540")
root["bg"] = blue
root.minsize(width=540, height=540)
root.mainloop()
