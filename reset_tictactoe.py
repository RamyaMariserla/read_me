from tkinter import *
import tkinter.messagebox


bclick = True
flag = 0

'''once game is over all the buttons are reset'''
def disableButton():
    button1.configure(state=NORMAL)
    button2.configure(state=NORMAL)
    button3.configure(state=NORMAL)
    button4.configure(state=NORMAL)
    button5.configure(state=NORMAL)
    button6.configure(state=NORMAL)
    button7.configure(state=NORMAL)
    button8.configure(state=NORMAL)
    button9.configure(state=NORMAL)

def SetToZero():
    button1['text']=' '
    button2['text']=' '
    button3['text']=' '
    button4['text']=' '
    button4['text']=' '
    button5['text']=' '
    button6['text']=' '
    button7['text']=' '
    button8['text']=' '
    button9['text']=' '
    global bclick,flag,condition
    bclick=True
    flag=0
    #condition=True

def btnClick(buttons):
    
    global bclick, flag, player2_name, player1_name, playerb, pa
    
    if buttons["text"] == " " and bclick == True:
        buttons["text"] = "X"
        bclick = False
        playerb = p2.get() + " Wins!"
        pa = p1.get() + " Wins!"
        checkForWin()
        flag += 1


    elif buttons["text"] == " " and bclick == False:
        buttons["text"] = "O"
        bclick = True
        checkForWin()
        flag += 1
    else:
        tkinter.messagebox.showinfo("Tic-Tac-Toe", "Button already Clicked!")

def checkForWin():
    if (button1['text'] == 'X' and button2['text'] == 'X' and button3['text'] == 'X' or
        button4['text'] == 'X' and button5['text'] == 'X' and button6['text'] == 'X' or
        button7['text'] =='X' and button8['text'] == 'X' and button9['text'] == 'X' or
        button1['text'] == 'X' and button5['text'] == 'X' and button9['text'] == 'X' or
        button3['text'] == 'X' and button5['text'] == 'X' and button7['text'] == 'X' or
        button1['text'] == 'X' and button2['text'] == 'X' and button3['text'] == 'X' or
        button1['text'] == 'X' and button4['text'] == 'X' and button7['text'] == 'X' or
        button2['text'] == 'X' and button5['text'] == 'X' and button8['text'] == 'X' or
        button7['text'] == 'X' and button6['text'] == 'X' and button9['text'] == 'X'):
        disableButton()
        tkinter.messagebox.showinfo("Tic-Tac-Toe", pa)

        tkinter.messagebox.showinfo("play again"," do u wanna play agian\nclick on reset")

    elif(flag >= 8):
        tkinter.messagebox.showinfo("Tic-Tac-Toe", "It is a Tie")

    elif (button1['text'] == 'O' and button2['text'] == 'O' and button3['text'] == 'O' or
          button4['text'] == 'O' and button5['text'] == 'O' and button6['text'] == 'O' or
          button7['text'] == 'O' and button8['text'] == 'O' and button9['text'] == 'O' or
          button1['text'] == 'O' and button5['text'] == 'O' and button9['text'] == 'O' or
          button3['text'] == 'O' and button5['text'] == 'O' and button7['text'] == 'O' or
          button1['text'] == 'O' and button2['text'] == 'O' and button3['text'] == 'O' or
          button1['text'] == 'O' and button4['text'] == 'O' and button7['text'] == 'O' or
          button2['text'] == 'O' and button5['text'] == 'O' and button8['text'] == 'O' or
          button7['text'] == 'O' and button6['text'] == 'O' and button9['text'] == 'O'):
        disableButton()
        tkinter.messagebox.showinfo("Tic-Tac-Toe", playerb)
#while(condition):
tk = Tk()
tk.title("Tic Tac Toe")

pa = StringVar()
playerb = StringVar()
p1 = StringVar()
p2 = StringVar()
'''these lines are labelling player 1 and player 2 in console'''
player1_name = Entry(tk, textvariable=p1, bd=5)
player1_name.grid(row=1, column=1, columnspan=8)
player2_name = Entry(tk, textvariable=p2, bd=5)
player2_name.grid(row=2, column=1, columnspan=8)
    

buttons = StringVar()

label = Label( tk, text="Player 1:", font='Times 20 bold', bg='white', fg='black', height=1, width=8)
label.grid(row=1, column=0)


label = Label( tk, text="Player 2:", font='Times 20 bold', bg='white', fg='black', height=1, width=8)
label.grid(row=2, column=0)

button1 = Button(tk, text=" ", font='Times 20 bold', bg='gray', fg='blue', height=4, width=8, command=lambda: btnClick(button1))
button1.grid(row=3, column=0)

button2 = Button(tk, text=' ', font='Times 20 bold', bg='gray', fg='white', height=4, width=8, command=lambda: btnClick(button2))
button2.grid(row=3, column=1)

button3 = Button(tk, text=' ',font='Times 20 bold', bg='gray', fg='white', height=4, width=8, command=lambda: btnClick(button3))
button3.grid(row=3, column=2)

button4 = Button(tk, text=' ', font='Times 20 bold', bg='gray', fg='white', height=4, width=8, command=lambda: btnClick(button4))
button4.grid(row=4, column=0)

button5 = Button(tk, text=' ', font='Times 20 bold', bg='gray', fg='white', height=4, width=8, command=lambda: btnClick(button5))
button5.grid(row=4, column=1)

button6 = Button(tk, text=' ', font='Times 20 bold', bg='gray', fg='white', height=4, width=8, command=lambda: btnClick(button6))
button6.grid(row=4, column=2)

button7 = Button(tk, text=' ', font='Times 20 bold', bg='gray', fg='white', height=4, width=8, command=lambda: btnClick(button7))
button7.grid(row=5, column=0)

button8 = Button(tk, text=' ', font='Times 20 bold', bg='gray', fg='white', height=4, width=8, command=lambda: btnClick(button8))
button8.grid(row=5, column=1)

button9 = Button(tk, text=' ', font='Times 20 bold', bg='gray', fg='white', height=4, width=8, command=lambda: btnClick(button9))
button9.grid(row=5, column=2)

reset = Button(tk, text=' reset ',font='Times 20 bold',height=2, width=4, command=lambda:SetToZero())
reset.grid(row=6,column=1)


tk.mainloop()

