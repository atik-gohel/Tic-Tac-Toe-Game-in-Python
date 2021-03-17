import tkinter as tk
from tkinter import *
from tkinter import Label
from tkinter import messagebox
from tkinter import Button
from tkinter import Checkbutton



tw = tk.Tk()
tw.title("Tic-Tac-Toe")
tw.geometry('1920x1080')
tw.configure(bg='white')


heading = Label(tw, text="Start Game Now Tic-Tac-Toe",width=30, fg='white', bg='black', font='Times 20 bold')
heading.place(x=540, y=30)


lblLine0 = Label(tw, bg='white', text = "*******************************************************************************************************************************************************************************************************************************************************************************************************************")
lblLine0.place(x=0, y=90)



label = Label( tw, text="Player 1:", font='Times 15 bold', bg='white', fg='black', height=1, width=8)
label.place(x=300, y=140)

label = Label( tw, text="Player 2:", font='Times 15 bold', bg='white', fg='black', height=1, width=8)
label.place(x=850, y=140)




#get player name for result 
PlayerA = StringVar()
PlayerB = StringVar()
# get string of player1_name and player2_name
p1 = StringVar()
p2 = StringVar()

#input box
player1_name = Entry(tw, textvariable=p1, bd=2, width="20", font=('arial',14))
player1_name.place(x=450, y=140)
player2_name = Entry(tw, textvariable=p2, bd=2, width="20", font=('arial',14))
player2_name.place(x=1010, y=140)

bclick = True
flag = 0

# dusabled butoon after one click
def gameover():
    # button1.configure(state=DISABLED)
    # button2.configure(state=DISABLED)
    # button3.configure(state=DISABLED)
    # button4.configure(state=DISABLED)
    # button5.configure(state=DISABLED)
    # button6.configure(state=DISABLED)
    # button7.configure(state=DISABLED)
    # button8.configure(state=DISABLED)
    # button9.configure(state=DISABLED)
    global flag
    button1["text"]=" "
    button2["text"]=" "
    button3["text"]=" "
    button4["text"]=" "
    button5["text"]=" "
    button6["text"]=" "
    button7["text"]=" "
    button8["text"]=" "
    button9["text"]=" "
    flag = 0

def btnClick(buttons):

    global bclick, flag, player1_name, player2_name, PlayerA, PlayerB

    if buttons["text"] == " " and bclick == True:
        buttons["text"] = "X"
        bclick = False
        PlayerB = p2.get() + "  Wins!"
        PlayerA = p1.get() + "  Wins!"
        checkForWin()
        flag +=1
    elif buttons["text"] == " " and bclick == False:
        buttons["text"] = "O"
        bclick = True
        checkForWin()
        flag +=1
    else:
        msg_w = messagebox.showinfo("warning!!!","Button already Clicked!")


def checkForWin():
    if (button1['text'] == 'X' and button2['text'] == 'X' and button3['text'] == 'X' or
        button4['text'] == 'X' and button5['text'] == 'X' and button6['text'] == 'X' or
        button7['text'] == 'X' and button8['text'] == 'X' and button9['text'] == 'X' or
        button1['text'] == 'X' and button5['text'] == 'X' and button9['text'] == 'X' or
        button1['text'] == 'X' and button4['text'] == 'X' and button7['text'] == 'X' or
        button2['text'] == 'X' and button5['text'] == 'X' and button8['text'] == 'X' or
        button3['text'] == 'X' and button5['text'] == 'X' and button7['text'] == 'X' or
        button3['text'] == 'X' and button6['text'] == 'X' and button9['text'] == 'X'):
        gameover()
        winMsg = messagebox.showinfo("winner !!", PlayerA)
        
    elif(flag == 8):
        gameover()
        tiwMsg= messagebox.showinfo("Ops!!", "It is a Tie")

    elif (button1['text'] == 'O' and button2['text'] == 'O' and button3['text'] == 'O' or
          button4['text'] == 'O' and button5['text'] == 'O' and button6['text'] == 'O' or
          button7['text'] == 'O' and button8['text'] == 'O' and button9['text'] == 'O' or
          button1['text'] == 'O' and button5['text'] == 'O' and button9['text'] == 'O' or
          button1['text'] == 'O' and button4['text'] == 'O' and button7['text'] == 'O' or
          button2['text'] == 'O' and button5['text'] == 'O' and button8['text'] == 'O' or
          button3['text'] == 'O' and button5['text'] == 'O' and button7['text'] == 'O' or
          button3['text'] == 'O' and button6['text'] == 'O' and button9['text'] == 'O'):
        gameover()
        winMsg = messagebox.showinfo("winner !!", PlayerB)



w = Canvas(tw, width=478, height=489, bg="#10171f")
w.place(x=525, y=190)


buttons = StringVar()

button1 = Button(tw, text=" " , font='Times 60 bold', bg="#ffe715", fg="#fefefe", activebackground="#fefefe", activeforeground="#ffe715", height=1, width=3  , bd=1, command=lambda : btnClick(button1))
button1.place(x=535, y=201)

button2 = Button(tw, text=" " , font='Times 60 bold', bg="#ffe715", fg="#fefefe", activebackground="#fefefe", activeforeground="#ffe715", height=1, width=3  , bd=1, command=lambda : btnClick(button2))
button2.place(x=690, y=201)

button3 = Button(tw, text=" " , font='Times 60 bold', bg="#ffe715", fg="#fefefe", activebackground="#fefefe", activeforeground="#ffe715", height=1, width=3  , bd=1, command=lambda : btnClick(button3))
button3.place(x=845, y=201)


button4 = Button(tw, text=" " , font='Times 60 bold', bg="#ffe715", fg="#fefefe", activebackground="#fefefe", activeforeground="#ffe715", height=1, width=3  , bd=1, command=lambda : btnClick(button4))
button4.place(x=535, y=360)

button5 = Button(tw, text=" " , font='Times 60 bold', bg="#ffe715", fg="#fefefe", activebackground="#fefefe", activeforeground="#ffe715", height=1, width=3  , bd=1, command=lambda : btnClick(button5))
button5.place(x=690, y=360)

button6 = Button(tw, text=" " , font='Times 60 bold', bg="#ffe715", fg="#fefefe", activebackground="#fefefe", activeforeground="#ffe715", height=1, width=3  , bd=1, command=lambda : btnClick(button6))
button6.place(x=845, y=360)


button7 = Button(tw, text=" " , font='Times 60 bold', bg="#ffe715", fg="#fefefe", activebackground="#fefefe", activeforeground="#ffe715", height=1, width=3  , bd=1, command=lambda : btnClick(button7))
button7.place(x=535, y=519)

button8 = Button(tw, text=" " , font='Times 60 bold', bg="#ffe715", fg="#fefefe", activebackground="#fefefe", activeforeground="#ffe715", height=1, width=3  , bd=1, command=lambda : btnClick(button8))
button8.place(x=690, y=519)

button9 = Button(tw, text=" " , font='Times 60 bold', bg="#ffe715", fg="#fefefe", activebackground="#fefefe", activeforeground="#ffe715", height=1, width=3  , bd=1, command=lambda : btnClick(button9))
button9.place(x=845, y=519)


tw.mainloop()