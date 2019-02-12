import tkinter
from tkinter import messagebox
import random
import os
import sys

class connectFour:
    root = tkinter.Tk()

    colors = {"Blue":"#00304A",
        "Red":"#F21B3F",
        "Yellow":"#EEE82C"}
    grid = [0]*42
    score = [0,0]
    turn = random.choice([-1,1])

    root.title("Connect Four")
    root.geometry("540x520")
    root["bg"] = colors["Blue"]
    root.minsize(width=540, height=520)

    # Functions

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

    def changeWindow(name):
        self = connectFour
        self.frame[name].tkraise()
        if name == "game":
            name = "icon"
            self.root.title("Connect Four")
            self.updateSettings(self)
        else:
            self.root.title("Connect Four - Settings")
        try:
            self.root.iconbitmap(self.path("assets/"+name+".ico"))
        except Exception as e:
            print(e)

    def path(relativePath):
        if hasattr(sys, '_MEIPASS'):
            return os.path.join(sys._MEIPASS, relativePath)
        return os.path.join(os.path.abspath("."), relativePath)

    def isColor(color):
        if color[0] == "#":
            color = color[1:]
        if len(color) == 6:
            for character in color:
                if character.upper() not in "0123456789ABCDEF":
                    return False
            return True
        return False


    def updateSettings(self):
        #for setting in self.settings:
        #    print(setting, self.settings[setting].get())

        #for color in ["p1", "p2", "bg"]
        self.colors["Blue"] = self.settings["bg"].get()
        for item in [self.frame["game"], self.textFrame, self.text, self.settingsFrame, self.settingsButton, self.mainGrid]:
            item.config(bg=self.settings["bg"].get())

        self.colors["Red"] = self.settings["p1"].get()
        self.colors["Yellow"] = self.settings["p2"].get()
        self.root.attributes('-alpha', self.settings["alpha"].get())

    # Load Button Images

    try:
        images = {"connect-four":tkinter.PhotoImage(file=path("assets/connect-four.gif")),
            "settings":tkinter.PhotoImage(file=path("assets/settings.gif")),
            "none":tkinter.PhotoImage(), "images":True}
        images["settings"] = images["settings"].subsample(9)
        images["connect-four"] = images["connect-four"].subsample(8)
    except Exception as e:
        images = {"none":tkinter.PhotoImage(), "images":False}
        print(e, "\nAn error has occoured loading the image files.\nText will be used instead.")

    try:
        root.iconbitmap(path("assets/icon.ico"))
    except Exception as e: print(e)
    
    # Game Page

    frame = {}
    frame["game"] = tkinter.Frame(bg=colors["Blue"])
    frame["game"].grid(row=0, column=0, sticky="nesw")
    frame["game"].grid_columnconfigure(0, weight=1)
    frame["game"].grid_rowconfigure(1, weight=1)
    root.grid_columnconfigure(0, weight=1)
    root.grid_rowconfigure(0, weight=1)

    textFrame = tkinter.Frame(frame["game"], bg=colors["Blue"], height=1, width=1)
    textFrame.grid(column=0, row=0, sticky="n")
    text = tkinter.Label(textFrame, text="Red's score: 0\nYellow's score: 0\n"+{-1:"Red", 1:"Yellow"}[turn]+"'s turn",
        bg=colors["Blue"], fg="white", font="Helvetica 9 bold", padx=5, pady=5)
    text.grid(column=1, row=0, sticky="n")
    
    settingsFrame = tkinter.Frame(frame["game"], bg=colors["Blue"], height=1, width=1, padx=10, pady=10)
    settingsFrame.grid(column=0, row=0, sticky="nw")
    if images["images"]:
        settingsButton = tkinter.Button(settingsFrame, height=30, width=30, bg=colors["Blue"], image=images["settings"],
            command=lambda name="settings": connectFour.changeWindow(name), borderwidth=0)
    else:
        settingsButton = tkinter.Button(settingsFrame, height=30, width=60, bg=colors["Blue"], image=images["none"],
            command=lambda name="settings": connectFour.changeWindow(name), borderwidth=0, text="Settings",
            compound="center", font="Helvetica 9 bold", fg="#ffffff")
    settingsButton.pack(side=tkinter.LEFT, anchor="nw")

    mainGrid = tkinter.Frame(frame["game"], bg=colors["Blue"])
    mainGrid.grid(column=0, row=1)

    buttons = []
    for row in range(6):
        for column in range(7):
            buttons.append(tkinter.Button(mainGrid, height=60, width=60, bg=colors["Blue"],
                command=lambda arg=column: connectFour.buttonPressed(arg), image=images["none"]))
            buttons[(row*7)+column].grid(column=column, row=row, padx=5, pady=5)

    # Settings Page

    frame["settings"] = tkinter.Frame(bg=colors["Blue"])
    frame["settings"].grid(row=0, column=0, sticky="nesw")
    settingsHeaderGrid = tkinter.Frame(frame["settings"], bg=colors["Blue"])
    settingsHeaderGrid.grid_columnconfigure(0, weight=1)
    settingsHeaderGrid.pack(side=tkinter.TOP, fill="both")
    
    settingsTitleFrame = tkinter.Frame(settingsHeaderGrid, bg=colors["Blue"], height=1, width=1)
    settingsTitleFrame.grid(column=0, row=0, sticky="n")
    settingsTitle = tkinter.Label(settingsTitleFrame, text="Settings", bg=colors["Blue"], fg="white", font="Impact 28")
    settingsTitle.grid(column=0, row=0, sticky="n")
    
    homeFrame = tkinter.Frame(settingsHeaderGrid, bg=colors["Blue"], height=1, width=1, padx=10, pady=10)
    homeFrame.grid(column=0, row=0, sticky="nw")
    if images["images"]:
        home = tkinter.Button(homeFrame, height=30, width=30, bg=colors["Blue"], image=images["connect-four"],
            command=lambda name="game": connectFour.changeWindow(name), borderwidth=0)
    else:
        home = tkinter.Button(homeFrame, height=30, width=90, bg=colors["Blue"], image=images["none"],
            command=lambda name="game": connectFour.changeWindow(name), borderwidth=0, text="Back to game",
            compound="center", font="Helvetica 9 bold", fg="#ffffff")
    home.pack(side=tkinter.LEFT, anchor="nw")

    menu = []
    variables = ["bg", "p1", "p2", "alpha"]
    settings = {}
    for var in variables:
        settings[var] = tkinter.StringVar()
    del variables

    settings["bg"].set("#00304A")
    settings["p1"].set("#F21B3F")
    settings["p2"].set("#EEE82C")
    settings["alpha"].set("1")

    menu.append(tkinter.Label(frame["settings"], text="(Hex Color) Background Color", bg=colors["Blue"],
        fg="white", font="Helvetica 9 bold").pack(padx=10, anchor="nw"))
    menu.append(tkinter.Entry(frame["settings"], textvariable=settings["bg"], font="Helvetica 9 bold",
        width = 8).pack(padx=15, anchor="nw"))
    
    menu.append(tkinter.Label(frame["settings"], text="(Hex Color) Player 1 Color", bg=colors["Blue"],
        fg="white", font="Helvetica 9 bold").pack(padx=10, anchor="nw"))
    menu.append(tkinter.Entry(frame["settings"], textvariable=settings["p1"], font="Helvetica 9 bold",
        width = 8).pack(padx=15, anchor="nw"))

    menu.append(tkinter.Label(frame["settings"], text="(Hex Color) Player 2 Color", bg=colors["Blue"],
        fg="white", font="Helvetica 9 bold").pack(padx=10, anchor="nw"))
    menu.append(tkinter.Entry(frame["settings"], textvariable=settings["p2"], font="Helvetica 9 bold",
        width = 8).pack(padx=15, anchor="nw"))

    menu.append(tkinter.Label(frame["settings"], text="Transparency (Number between 0 and 1)", bg=colors["Blue"],
        fg="white", font="Helvetica 9 bold").pack(padx=10, anchor="nw"))
    menu.append(tkinter.Entry(frame["settings"], textvariable=settings["alpha"], font="Helvetica 9 bold",
        width = 5).pack(padx=15, anchor="nw"))
    

connectFour.frame["game"].tkraise()
connectFour.root.mainloop()
