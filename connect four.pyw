import tkinter
import tkinter.messagebox
import random

blue = "#00304A"
red = "#F21B3F"
yellow = "#EEE82C"

grid = [0,0,0,0,0,0,0,
        0,0,0,0,0,0,0,
        0,0,0,0,0,0,0,
        0,0,0,0,0,0,0,
        0,0,0,0,0,0,0,
        0,0,0,0,0,0,0]
score = [0,0]
turn = random.choice([-1,1])
root = tkinter.Tk()

def hasWon(a):
    b = [a[0]+a[1]+a[2]+a[3], a[1]+a[2]+a[3]+a[4], a[2]+a[3]+a[4]+a[5], a[3]+a[4]+a[5]+a[6], ## horisontal -
         a[7]+a[8]+a[9]+a[10], a[8]+a[9]+a[10]+a[11], a[9]+a[10]+a[11]+a[12], a[10]+a[11]+a[12]+a[13],
         a[14]+a[15]+a[16]+a[17], a[15]+a[16]+a[17]+a[18], a[16]+a[17]+a[18]+a[19], a[17]+a[18]+a[19]+a[20],
         a[21]+a[22]+a[23]+a[24], a[22]+a[23]+a[24]+a[25], a[23]+a[24]+a[25]+a[26], a[24]+a[25]+a[26]+a[27],
         a[28]+a[29]+a[30]+a[31], a[29]+a[30]+a[31]+a[32], a[30]+a[31]+a[32]+a[33], a[31]+a[32]+a[33]+a[34],
         a[35]+a[36]+a[37]+a[38], a[36]+a[37]+a[38]+a[39], a[37]+a[38]+a[39]+a[40], a[38]+a[39]+a[40]+a[41],
         
         a[0]+a[7]+a[14]+a[21], a[7]+a[14]+a[21]+a[28], a[14]+a[21]+a[28]+a[35], ## vertical |
         a[1]+a[8]+a[15]+a[22], a[8]+a[15]+a[22]+a[29], a[15]+a[22]+a[29]+a[36],
         a[2]+a[9]+a[16]+a[23], a[9]+a[16]+a[23]+a[30], a[16]+a[23]+a[30]+a[37],
         a[3]+a[10]+a[17]+a[24], a[10]+a[17]+a[24]+a[31], a[17]+a[24]+a[31]+a[38],
         a[4]+a[11]+a[18]+a[25], a[11]+a[18]+a[25]+a[32], a[18]+a[25]+a[32]+a[39],
         a[5]+a[12]+a[19]+a[26], a[12]+a[19]+a[26]+a[33], a[19]+a[26]+a[33]+a[40],
         a[6]+a[13]+a[20]+a[27], a[13]+a[20]+a[27]+a[34], a[20]+a[27]+a[34]+a[41],

         a[0]+a[8]+a[16]+a[24], a[1]+a[9]+a[17]+a[25], a[2]+a[10]+a[18]+a[26], a[3]+a[11]+a[19]+a[27], ## diaginal \
         a[8]+a[16]+a[24]+a[31], a[9]+a[17]+a[25]+a[32], a[10]+a[18]+a[26]+a[33], a[11]+a[19]+a[27]+a[34],
         a[16]+a[24]+a[31]+a[39], a[17]+a[25]+a[32]+a[40], a[18]+a[26]+a[33]+a[41], a[19]+a[27]+a[34]+a[41],

         a[3]+a[9]+a[15]+a[21], a[4]+a[10]+a[16]+a[22], a[5]+a[11]+a[17]+a[23], a[6]+a[12]+a[18]+a[24], ## diaginal /
         a[9]+a[15]+a[21]+a[28], a[10]+a[16]+a[22]+a[29], a[11]+a[17]+a[23]+a[30], a[12]+a[18]+a[24]+a[31],
         a[15]+a[21]+a[28]+a[35], a[16]+a[22]+a[29]+a[36], a[17]+a[23]+a[30]+a[37], a[18]+a[24]+a[31]+a[38]]
    
    if 4 in b:
        print("1 has won")
        return 1
    elif -4 in b:
        print("-1 has won")
        return -1
    else:
        print("no one has won")
        return 0

def c1():
    print("!!!!c1")

def c2():
    print("!!!!c2")

def c3():
    print("!!!!c3")

def c4():
    print("!!!!c4")

def c5():
    print("!!!!c5")

def c6():
    print("!!!!c6")

def c7():
    print("!!!!c7")
		
		
mainGrid = tkinter.Frame(bg=blue)
buttons = []

for i in range(6):
    buttons.append(tkinter.Button(mainGrid, text=(str(i)), height=4, width=8, bg=blue, command=c1))
    buttons.append(tkinter.Button(mainGrid, text=(str(i)), height=4, width=8, bg=blue, command=c2))
    buttons.append(tkinter.Button(mainGrid, text=(str(i)), height=4, width=8, bg=blue, command=c3))
    buttons.append(tkinter.Button(mainGrid, text=(str(i)), height=4, width=8, bg=blue, command=c4))
    buttons.append(tkinter.Button(mainGrid, text=(str(i)), height=4, width=8, bg=blue, command=c5))
    buttons.append(tkinter.Button(mainGrid, text=(str(i)), height=4, width=8, bg=blue, command=c6))
    buttons.append(tkinter.Button(mainGrid, text=(str(i)), height=4, width=8, bg=blue, command=c7))

mainGrid.pack(expand=True)

a = 0
for i in range(7):
    for x in range(6):
        buttons[a].grid(column=i, row=x, padx=5, pady=5)
        a += 1

try:
    root.iconbitmap("assets/icon.ico")
except Exception as e:
    print(e)
root.title("Connect Four")
root.geometry("540x495")
root["bg"]=blue
root.minsize(width=540, height=495)
root.mainloop()
