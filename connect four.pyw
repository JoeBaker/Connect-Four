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
button11 = tkinter.Button(mainGrid, height=4, width=8, bg=blue, command=c1)
button12 = tkinter.Button(mainGrid, height=4, width=8, bg=blue, command=c1)
button13 = tkinter.Button(mainGrid, height=4, width=8, bg=blue, command=c1)
button14 = tkinter.Button(mainGrid, height=4, width=8, bg=blue, command=c1)
button15 = tkinter.Button(mainGrid, height=4, width=8, bg=blue, command=c1)
button16 = tkinter.Button(mainGrid, height=4, width=8, bg=blue, command=c1)

button21 = tkinter.Button(mainGrid, height=4, width=8, bg=blue, command=c2)
button22 = tkinter.Button(mainGrid, height=4, width=8, bg=blue, command=c2)
button23 = tkinter.Button(mainGrid, height=4, width=8, bg=blue, command=c2)
button24 = tkinter.Button(mainGrid, height=4, width=8, bg=blue, command=c2)
button25 = tkinter.Button(mainGrid, height=4, width=8, bg=blue, command=c2)
button26 = tkinter.Button(mainGrid, height=4, width=8, bg=blue, command=c2)

button31 = tkinter.Button(mainGrid, height=4, width=8, bg=blue, command=c3)
button32 = tkinter.Button(mainGrid, height=4, width=8, bg=blue, command=c3)
button33 = tkinter.Button(mainGrid, height=4, width=8, bg=blue, command=c3)
button34 = tkinter.Button(mainGrid, height=4, width=8, bg=blue, command=c3)
button35 = tkinter.Button(mainGrid, height=4, width=8, bg=blue, command=c3)
button36 = tkinter.Button(mainGrid, height=4, width=8, bg=blue, command=c3)

button41 = tkinter.Button(mainGrid, height=4, width=8, bg=blue, command=c4)
button42 = tkinter.Button(mainGrid, height=4, width=8, bg=blue, command=c4)
button43 = tkinter.Button(mainGrid, height=4, width=8, bg=blue, command=c4)
button44 = tkinter.Button(mainGrid, height=4, width=8, bg=blue, command=c4)
button45 = tkinter.Button(mainGrid, height=4, width=8, bg=blue, command=c4)
button46 = tkinter.Button(mainGrid, height=4, width=8, bg=blue, command=c4)

button51 = tkinter.Button(mainGrid, height=4, width=8, bg=blue, command=c5)
button52 = tkinter.Button(mainGrid, height=4, width=8, bg=blue, command=c5)
button53 = tkinter.Button(mainGrid, height=4, width=8, bg=blue, command=c5)
button54 = tkinter.Button(mainGrid, height=4, width=8, bg=blue, command=c5)
button55 = tkinter.Button(mainGrid, height=4, width=8, bg=blue, command=c5)
button56 = tkinter.Button(mainGrid, height=4, width=8, bg=blue, command=c5)

button61 = tkinter.Button(mainGrid, height=4, width=8, bg=blue, command=c6)
button62 = tkinter.Button(mainGrid, height=4, width=8, bg=blue, command=c6)
button63 = tkinter.Button(mainGrid, height=4, width=8, bg=blue, command=c6)
button64 = tkinter.Button(mainGrid, height=4, width=8, bg=blue, command=c6)
button65 = tkinter.Button(mainGrid, height=4, width=8, bg=blue, command=c6)
button66 = tkinter.Button(mainGrid, height=4, width=8, bg=blue, command=c6)

button71 = tkinter.Button(mainGrid, height=4, width=8, bg=blue, command=c7)
button72 = tkinter.Button(mainGrid, height=4, width=8, bg=blue, command=c7)
button73 = tkinter.Button(mainGrid, height=4, width=8, bg=blue, command=c7)
button74 = tkinter.Button(mainGrid, height=4, width=8, bg=blue, command=c7)
button75 = tkinter.Button(mainGrid, height=4, width=8, bg=blue, command=c7)
button76 = tkinter.Button(mainGrid, height=4, width=8, bg=blue, command=c7)


mainGrid.pack(expand=True)
button11.grid(column=1, row=1, padx=5, pady=5)
button12.grid(column=1, row=2, padx=5, pady=5)
button13.grid(column=1, row=3, padx=5, pady=5)
button14.grid(column=1, row=4, padx=5, pady=5)
button15.grid(column=1, row=5, padx=5, pady=5)
button16.grid(column=1, row=6, padx=5, pady=5)

button21.grid(column=2, row=1, padx=5, pady=5)
button22.grid(column=2, row=2, padx=5, pady=5)
button23.grid(column=2, row=3, padx=5, pady=5)
button24.grid(column=2, row=4, padx=5, pady=5)
button25.grid(column=2, row=5, padx=5, pady=5)
button26.grid(column=2, row=6, padx=5, pady=5)

button31.grid(column=3, row=1, padx=5, pady=5)
button32.grid(column=3, row=2, padx=5, pady=5)
button33.grid(column=3, row=3, padx=5, pady=5)
button34.grid(column=3, row=4, padx=5, pady=5)
button35.grid(column=3, row=5, padx=5, pady=5)
button36.grid(column=3, row=6, padx=5, pady=5)

button41.grid(column=4, row=1, padx=5, pady=5)
button42.grid(column=4, row=2, padx=5, pady=5)
button43.grid(column=4, row=3, padx=5, pady=5)
button44.grid(column=4, row=4, padx=5, pady=5)
button45.grid(column=4, row=5, padx=5, pady=5)
button46.grid(column=4, row=6, padx=5, pady=5)

button51.grid(column=5, row=1, padx=5, pady=5)
button52.grid(column=5, row=2, padx=5, pady=5)
button53.grid(column=5, row=3, padx=5, pady=5)
button54.grid(column=5, row=4, padx=5, pady=5)
button55.grid(column=5, row=5, padx=5, pady=5)
button56.grid(column=5, row=6, padx=5, pady=5)

button61.grid(column=6, row=1, padx=5, pady=5)
button62.grid(column=6, row=2, padx=5, pady=5)
button63.grid(column=6, row=3, padx=5, pady=5)
button64.grid(column=6, row=4, padx=5, pady=5)
button65.grid(column=6, row=5, padx=5, pady=5)
button66.grid(column=6, row=6, padx=5, pady=5)

button71.grid(column=7, row=1, padx=5, pady=5)
button72.grid(column=7, row=2, padx=5, pady=5)
button73.grid(column=7, row=3, padx=5, pady=5)
button74.grid(column=7, row=4, padx=5, pady=5)
button75.grid(column=7, row=5, padx=5, pady=5)
button76.grid(column=7, row=6, padx=5, pady=5)


try:
    root.iconbitmap("assets/icon.ico")
except Exception as e:
    print(e)
root.title("Connect Four")
root.geometry("540x495")
root["bg"]=blue
root.minsize(width=540, height=495)
root.mainloop()
