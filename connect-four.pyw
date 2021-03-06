#!/usr/bin/env python3

import tkinter
from tkinter import messagebox
import random
import os
import sys

class connectFour:
    root = tkinter.Tk()

    colors = {"bg":"#00304A",
        "p1":"#F21B3F",
        "p2":"#EEE82C",
        "text":"#FFFFFF"}
    names = ["Red", "Yellow"]
    grid = [0]*42
    score = [0,0]
    turn = random.choice([-1,1])
    fall = 80
    root.title("Connect Four")
    root["bg"] = colors["bg"]
    messagebox = True

    # Window sizes

    def updateSize(sizeMultiplyer):
        size = {}
        size["x"] = 165 + (33 * sizeMultiplyer)
        size["y"] = 200 + (30 * sizeMultiplyer)
        size["bh"] = 20 + (((sizeMultiplyer) // 4) * 5)
        if sizeMultiplyer == 0:
            size["bw+p"] = 20
        elif sizeMultiplyer in [1,2]:
            size["bw+p"] = 25
        else:
            size["bw+p"] = 30
        size["bw+t"] = 20 + (((sizeMultiplyer + 1) // 3) * 10)
        size["b+t"] = 4 + ((sizeMultiplyer + 4) // 3)
        size["info"] = 7 + ((sizeMultiplyer + 2) // 2)
        size["grid"] = 15 + (4 * sizeMultiplyer)
        size["pad"] = 1 + (((sizeMultiplyer) // 6) * 2)
        return size

    size = updateSize(10)
    root.geometry(str(size["x"])+"x"+str(size["y"]))
    root.minsize(width=size["x"], height=size["y"])

    # Functions

    def whatColor(self):
        name = {-1:self.names[0], 1:self.names[1]}[self.turn]
        hex = {-1:self.colors["p1"], 1:self.colors["p2"]}[self.turn]
        return {"hex":hex, "name":name, "turn":self.turn}

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
            self.buttons[i].config(bg=self.colors["bg"])
        self.grid = [0]*42

    def fallAnimation(self, place):
        color = self.whatColor(self)
        if not place < 7:
            self.buttons[place - 7].config(bg=self.colors["bg"])
        self.buttons[place].config(bg=color["hex"])
        if self.grid[place + 7:place + 8] == [0]:
            place += 7
            self.mainGrid.after(self.fall, lambda: self.fallAnimation(self, place))
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
                message = title + ("\n"+self.names[0]+"'s score: "+str(self.score[0])+
                    "\n"+self.names[1]+"'s score: "+str(self.score[1]))
            else:
                title, message = ["No one has won"]*2
            self.text.config(text=self.names[0]+"'s score: "+str(self.score[0])+
                "\n"+self.names[1]+"'s score: "+str(self.score[1])+"\n")
            self.message(title, message)
            self.resetGrid(self)
        self.turn = 0 - self.turn
        self.updateInfo(self)

    def lockButtons(self, lock):
        for i in range(42):
            self.buttons[i].config(state={True:"disabled", False:"normal"}[lock])

    def buttonPressed(column):
        self = connectFour
        self.lockButtons(self, True)
        self.text.config(text=self.names[0]+"'s score: "+str(self.score[0])+"\n"+self.names[1]+
            "'s score: "+str(self.score[1])+"\n")
        if self.grid[column] != 0:
            self.message("You can't go here", "You can't go here because this column is full."+
                "\nTry going somewhere else.")
            self.lockButtons(self, False)
            self.updateInfo(self)
        else:
            self.fallAnimation(self, column)

    def changeWindow(name):
        self = connectFour
        self.frame[name].tkraise()
        if name == "game":
            name = "connect-four"
            self.root.title("Connect Four")
            self.updateSettings(self)
            self.root.minsize(width=self.size["x"], height=self.size["y"])
        else:
            self.root.title("Connect Four - Settings")
            self.root.minsize(width=264, height=256)

        try:
            icon = tkinter.PhotoImage(file=self.path("assets/"+name+".gif"))
            self.root.tk.call("wm", "iconphoto", self.root._w, icon)
        except Exception as e: print(e)


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

    def reloadGrid(self):
        for place in range(42):
            color = {-1:self.colors["p1"], 0:self.colors["bg"], 1:self.colors["p2"]}[self.grid[place]]
            self.buttons[place].config(bg=color, height=self.size["grid"], width=self.size["grid"])
            self.buttons[place].grid(padx=self.size["pad"], pady=self.size["pad"])

    def updateSettings(self):
        if self.isColor(self.settings["bg"].get()):
            self.colors["bg"] = self.settings["bg"].get()
            for item in [self.frame["game"], self.textFrame, self.text, self.settingsFrame, self.settingsButton, self.mainGrid]:
                item.config(bg=self.settings["bg"].get())
        else:
            self.settings["bg"].set(self.colors["bg"])

        if self.isColor(self.settings["text"].get()):
            self.colors["text"] = self.settings["text"].get()
            self.text.config(fg=self.colors["text"])
        else:
            self.settings["text"].set(self.colors["text"])

        for player in ["p1", "p2"]:
            if self.isColor(self.settings[player].get()):
                self.colors[player] = self.settings[player].get()
            else:
                self.settings[player].set(self.colors[player])

            nameIndex = {"p1":0, "p2":1}[player]
            if 0 < len(self.settings[player+"Name"].get()) <= 32:
                self.names[nameIndex] = self.settings[player+"Name"].get()
            else:
                self.settings[player+"Name"].set(self.names[nameIndex])

        try:
            if 0 < float(self.settings["alpha"].get()) <= 1:
                self.root.attributes('-alpha', self.settings["alpha"].get())
            else:
                self.root.attributes('-alpha', 1)
                self.settings["alpha"].set("1")
        except:
            self.root.attributes('-alpha', 1)
            self.settings["alpha"].set("1")

        try:
            self.fall = int(self.settings["fall"].get())
        except:
            self.fall = 80
            self.settings["fall"].set("80")

        self.size = self.updateSize(int(self.settings["size"].get()))
        self.settingsButton.config(width={True:self.size["bw+p"], False:self.size["bw+t"]}[self.images["images"]],
            height=self.size["bh"], font="Helvetica "+str(self.size["b+t"])+" bold")

        self.reloadGrid(self)
        self.updateInfo(self)
        self.messagebox = int(self.settings["messagebox"].get())

    def updateInfo(self):
        self.text.config(text=self.names[0]+"'s score: "+str(self.score[0])+"\n"+self.names[1]+"'s score: "+
            str(self.score[1])+"\n"+{-1:self.names[0], 1:self.names[1]}[self.turn]+"'s turn",
            font="Helvetica "+str(self.size["info"])+" bold")

    def resetScores(self):
        self.message("Scores Reset", "Scores reset\n"+self.names[0]+"'s old score: "+str(self.score[0])+
            "\n"+self.names[1]+"'s old score: "+str(self.score[1]))
        self.score = [0,0]
        self.updateInfo(self)

    # Lambdas

    message = (lambda title, message: tkinter.messagebox.showinfo(title=title, message=message)
        if connectFour.messagebox else False)

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
        icon = tkinter.PhotoImage(file=path("assets/connect-four.gif"))
        root.tk.call("wm", "iconphoto", root._w, icon)
    except Exception as e: print(e)

    # Game Page

    frame = {}
    frame["game"] = tkinter.Frame(bg=colors["bg"])
    frame["game"].grid(row=0, column=0, sticky="nesw")
    frame["game"].grid_columnconfigure(0, weight=1)
    frame["game"].grid_rowconfigure(1, weight=1)
    root.grid_columnconfigure(0, weight=1)
    root.grid_rowconfigure(0, weight=1)

    textFrame = tkinter.Frame(frame["game"], bg=colors["bg"], height=1, width=1)
    textFrame.grid(column=0, row=0, sticky="n")
    text = tkinter.Label(textFrame, text="Red's score: 0\nYellow's score: 0\n"+{-1:"Red", 1:"Yellow"}[turn]+"'s turn",
        bg=colors["bg"], fg="white", font="Helvetica "+str(size["info"])+" bold", padx=5, pady=5)
    text.grid(column=1, row=0, sticky="n")

    settingsFrame = tkinter.Frame(frame["game"], bg=colors["bg"], height=1, width=1, padx=10, pady=10)
    settingsFrame.grid(column=0, row=0, sticky="nw")
    if images["images"]:
        settingsButton = tkinter.Button(settingsFrame, height=size["bh"], width=size["bw+p"], bg=colors["bg"],
            image=images["settings"], command=lambda name="settings": connectFour.changeWindow(name), borderwidth=0)
    else:
        settingsButton = tkinter.Button(settingsFrame, height=size["bh"], width=size["bw+t"], bg=colors["bg"],
            image=images["none"], command=lambda name="settings": connectFour.changeWindow(name), borderwidth=0,
            text="Settings", compound="center", font="Helvetica "+str(size["b+t"])+" bold", fg="#ffffff")
    settingsButton.pack(side=tkinter.LEFT, anchor="nw")

    mainGrid = tkinter.Frame(frame["game"], bg=colors["bg"])
    mainGrid.grid(column=0, row=1)

    buttons = []
    for row in range(6):
        for column in range(7):
            buttons.append(tkinter.Button(mainGrid, height=size["grid"], width=size["grid"], bg=colors["bg"],
                command=lambda arg=column: connectFour.buttonPressed(arg), image=images["none"]))
            buttons[(row*7)+column].grid(column=column, row=row, padx=size["pad"], pady=size["pad"])

    # Settings Page

    frame["settings"] = tkinter.Frame(bg=colors["bg"])
    frame["settings"].grid(row=0, column=0, sticky="snew")

    scrollbar = tkinter.Scrollbar(frame["settings"], orient="vertical")
    scrollbar.pack(side="right", fill="y")

    settingsHeaderGrid = tkinter.Frame(frame["settings"], bg=colors["bg"])
    settingsHeaderGrid.grid_columnconfigure(1, weight=1)
    settingsHeaderGrid.pack(side="top", fill="x")

    alignmentFrame = tkinter.Frame(settingsHeaderGrid, bg=colors["bg"], width=34)
    alignmentFrame.grid(column=2, row=0, sticky="ne")

    settingsTitleFrame = tkinter.Frame(settingsHeaderGrid, bg=colors["bg"], height=1, width=1)
    settingsTitleFrame.grid(column=1, row=0, sticky="n")
    settingsTitle = tkinter.Label(settingsTitleFrame, text="Settings", bg=colors["bg"], fg="white", font="Consolas 28 bold")
    settingsTitle.grid(column=0, row=0, sticky="n")

    homeFrame = tkinter.Frame(settingsHeaderGrid, bg=colors["bg"], height=1, width=1, padx=10, pady=10)
    homeFrame.grid(column=0, row=0, sticky="nw")
    if images["images"]:
        home = tkinter.Button(homeFrame, height=30, width=30, bg=colors["bg"], image=images["connect-four"],
            command=lambda name="game": connectFour.changeWindow(name), borderwidth=0)
    else:
        home = tkinter.Button(homeFrame, height=30, width=90, bg=colors["bg"], image=images["none"],
            command=lambda name="game": connectFour.changeWindow(name), borderwidth=0, text="Back to game",
            compound="center", font="Helvetica 9 bold", fg="#ffffff")
    home.pack(side=tkinter.LEFT, anchor="nw")

    menu = []
    variables = ["bg", "text", "p1", "p2", "p1Name", "p2Name", "fall", "alpha", "size", "messagebox"]
    settings = {}
    for var in variables:
        settings[var] = tkinter.StringVar()
    del variables

    settings["bg"].set("#00304A")
    settings["text"].set("#FFFFFF")
    settings["p1"].set("#F21B3F")
    settings["p2"].set("#EEE82C")
    settings["p1Name"].set(names[0])
    settings["p2Name"].set(names[1])
    settings["fall"].set("80")
    settings["alpha"].set("1")
    settings["size"].set("10")
    settings["messagebox"].set("1")

    canvas = tkinter.Canvas(frame["settings"], height=1000, bg=colors["bg"],
        scrollregion=(0, 0, 0, 1000), highlightthickness=0)
    canvas.pack(anchor="nw")
    scrollbar.config(command=canvas.yview)
    canvas.config(yscrollcommand=scrollbar.set)
    canvas.configure(scrollregion=canvas.bbox("all"))
    canvasFrame= tkinter.Frame(canvas, bg=colors["bg"])
    canvas.create_window((0,0),window=canvasFrame,anchor='nw')
    canvasFrame.bind("<Configure>",(lambda event: connectFour.canvas.configure(scrollregion=connectFour.canvas.bbox("all"))))

    for item in [["Background Color (Hex Color)", "bg", 8], ["Text Color (Hex Color)", "text", 8],
            ["Player 1's Color (Hex Color)", "p1", 8], ["Player 2's Color (Hex Color)", "p2", 8],
            ["Player 1's name", "p1Name", 31], ["Player 2's name", "p2Name", 31],
            ["Fall Speed (Milliseconds)", "fall", 8], ["Transparency (0 to 1)", "alpha", 5]]:
        menu.append(tkinter.Label(canvasFrame, text=item[0], bg=colors["bg"],
            fg="white", font="Helvetica 9 bold").pack(padx=5, anchor="nw"))
        menu.append(tkinter.Entry(canvasFrame, textvariable=settings[item[1]], font="Helvetica 9 bold",
            width = item[2]).pack(padx=10, anchor="nw"))

    menu.append(tkinter.Label(canvasFrame, text="Grid size", bg=colors["bg"],
        fg="white", font="Helvetica 9 bold").pack(padx=5, anchor="nw"))
    menu.append(tkinter.Scale(canvasFrame, highlightthickness=0, activebackground=colors["bg"], length=228,
        orient="horizontal", highlightbackground=colors["bg"], to=50, from_=0, variable=settings["size"],
        bg=colors["bg"], fg="white", font="Helvetica 9 bold").pack(padx=5, anchor="nw"))

    menu.append(tkinter.Label(canvasFrame, text="Show messagebox", bg=colors["bg"],
        fg="white", font="Helvetica 9 bold").pack(padx=5, anchor="nw"))
    menu.append(tkinter.Checkbutton(canvasFrame, activebackground=colors["bg"],
        bg=colors["bg"], font="Helvetica 9 bold", variable=settings["messagebox"]).pack(padx=5, anchor="nw"))

    menu.append(tkinter.Button(canvasFrame, height=1, width=12, bg=colors["bg"], fg=colors["text"],
        text="Reset scores", command=lambda name="settings": connectFour.resetScores(connectFour)).pack(padx=5, pady=30, anchor="nw"))

    menu.append(tkinter.Label(canvasFrame, text="Connect Four by Joe Baker\nhttps://github.com/JoeBaker/connect-four",
        bg=colors["bg"], fg="white", font="Helvetica 9 bold", justify="left").pack(padx=5, anchor="nw"))

    def _on_mousewheel(event):
        connectFour.canvas.yview_scroll(int(-1*(event.delta/120)), "units")
    canvas.bind_all("<MouseWheel>", _on_mousewheel)


connectFour.frame["game"].tkraise()
connectFour.root.mainloop()
