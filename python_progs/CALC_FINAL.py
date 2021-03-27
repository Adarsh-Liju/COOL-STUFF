'''FINAL DRAFT OF CALC?'''
from tkinter import *
from tkinter import font as tkFont
import math as m

root = Tk()
root.title("SIMPLE CALCULATOR")
#rootlabel = Label(root, text="CALCULATOR", bg='gray3', fg = 'snow', font=("Times", 10, 'bold'))
#rootlabel.grid(row = 0,column = 2)
#root.geometry("538x540")
root.config(background='gray3')


e = Entry(root , width = 60, relief= SUNKEN, borderwidth = 8)
e.grid(row = 1 , column = 0 , columnspan = 6 , padx = 20, pady = 40)
btfont = tkFont.Font(size=12)


def click(number):
    current = e.get()
    e.delete(0, END)
    e.insert(0, str(current) + str(number))
def input1():
    global inp
    inp=e.get()
    e.delete(0,END)
    temp=inp
    global calc_output
    try:
        calc_output=eval(inp)
    except ZeroDivisionError:
        calc_output="CANNOT DIVIDE BY ZERO"
        print(calc_output)
    except SyntaxError:
        calc_output="WRONG INPUT"
        print(calc_output)
    except TypeError:
        calc_output="SYNTAX ERROR"
        print(calc_output)
    else:
        print(calc_output)
    e.insert(0, calc_output)
def output1():
    e.insert(0,calc_output)
def clearall():
    e.delete(0,END)
def close():
    root.destroy()

def Sqrt():
    global f_num, ans
    f_num = float(e.get())
    ans = m.sqrt(f_num)
    e.delete(0, END)
    e.insert(0, str(ans))

def sine():
    global f_num,ans
    f_num = float(e.get())
    ans = m.sin(m.radians(f_num))
    e.delete(0,END)
    e.insert(0,str(ans))

def cosine():
    global f_num, ans
    f_num = float(e.get())
    ans = m.cos(m.radians(f_num))
    e.delete(0, END)
    e.insert(0, str(ans))


def tangent():
    global f_num, ans
    f_num = float(e.get())
    ans = m.tan(m.radians(f_num))
    e.delete(0, END)
    e.insert(0, str(ans))


def logarithm():
    global f_num, ans
    f_num = float(e.get())
    ans = m.log10(f_num)
    e.delete(0, END)
    e.insert(0, str(ans))


#btinp= Button(root, text = "inp", padx = 40 , pady = 20, command = input1, bg='black',fg='snow',font=btfont)
btequal=Button(root, text = " = ", padx = 40 , pady = 20, command =  input1, bg='black',fg='snow',font=btfont)
btclear=Button(root, text = " C ", padx = 40 , pady = 20,  command =  clearall, bg='red4',fg='snow',font=btfont)


bt1 = Button(root, text = "1", padx = 40 , pady = 20, command = lambda : click(1),font=btfont)
bt2 = Button(root, text = "2", padx = 40 , pady = 20, command = lambda : click(2),font=btfont)
bt3 = Button(root, text = "3", padx = 40 , pady = 20, command = lambda : click(3),font=btfont)
bt4 = Button(root, text = "4", padx = 40 , pady = 20, command = lambda : click(4),font=btfont)
bt5 = Button(root, text = "5", padx = 40 , pady = 20, command = lambda : click(5),font=btfont)
bt6 = Button(root, text = "6", padx = 40 , pady = 20, command = lambda : click(6),font=btfont)
bt7 = Button(root, text = "7", padx = 40 , pady = 20, command = lambda : click(7),font=btfont)
bt8 = Button(root, text = "8", padx = 40 , pady = 20, command = lambda : click(8),font=btfont)
bt9 = Button(root, text = "9", padx = 40 , pady = 20, command = lambda : click(9),font=btfont)
bt0 = Button(root, text = "0", padx = 40 , pady = 20, command = lambda : click(0),font=btfont)
decimalpt = Button(root, text=".", command= lambda: click('.'), padx=40, pady=20,font=btfont,bg='black',fg='snow')

btexponent=Button(root, text = " ^ ", padx = 40 , pady = 20, command = lambda : click('**') , bg='black',fg='snow',font=btfont)
btadd = Button(root, text = "+", padx = 40 , pady = 20, command = lambda : click('+'),font=btfont,bg='black',fg='snow')
btsub = Button(root, text = "-", padx = 40 , pady = 20, command = lambda : click('-'),font=btfont,bg='black',fg='snow')
btmul = Button(root, text = "*", padx = 40 , pady = 20, command = lambda : click('*'),font=btfont,bg='black',fg='snow')
btdiv = Button(root, text = "/", padx = 40 , pady = 20, command = lambda : click('/'),font=btfont,bg='black',fg='snow')

btclose= Button(root, text = "CLOSE", padx = 40 , pady = 20, width = 50, command = close ,font=btfont,bg='red3',fg='snow')
btopenbracket= Button(root, text = "(", padx = 40 , pady = 20, command = lambda : click('('),font=btfont,bg='black',fg='snow')
btclosebracket= Button(root, text = ")", padx = 40 , pady = 20, command = lambda : click(')'),font=btfont,bg='black',fg='snow')

btsqrt=Button(root,fg='snow',bg="black", text = "Sqt", padx = 41 , pady = 20, command = Sqrt,font=btfont)
btsin=Button(root,fg='snow',bg="black", text = "sin", padx = 41 , pady = 20, command =sine,font=btfont)
btcos=Button(root,fg='snow',bg="black", text = "cos", padx = 41 , pady = 20, command =cosine,font=btfont)
bttan=Button(root,fg='snow',bg="black", text = "tan", padx = 41 , pady = 20, command =tangent,font=btfont)
btlog=Button(root,fg='snow',bg="black", text = "log", padx = 41 , pady = 20, command =logarithm,font=btfont)

btequal.grid(row = 6, column = 3)
btclose.grid(row = 7, column = 0, columnspan = 5)
btclear.grid(row = 2,column = 3)
btopenbracket.grid( row = 2,column = 1)
btclosebracket.grid( row = 2,column = 2)
btexponent.grid( row = 6,column =4)

bt1.grid(row = 5, column = 1)
bt2.grid(row = 5, column = 2)
bt3.grid(row = 5, column = 3)

bt4.grid(row = 4, column = 1)
bt5.grid(row = 4, column = 2)
bt6.grid(row = 4, column = 3)

bt7.grid(row = 3, column = 1)
bt8.grid(row = 3, column = 2)
bt9.grid(row = 3, column = 3)

btadd.grid(row = 2, column = 4 )
btsub.grid(row = 3, column = 4 )
btmul.grid(row = 4, column = 4 )
btdiv.grid(row = 5, column = 4 )

bt0.grid(row = 6, column = 2 )
decimalpt.grid(row = 6,column = 1)

btsqrt.grid(row=2,column=0)
btsin.grid(row=3,column=0)
btcos.grid(row=4,column=0)
bttan.grid(row=5,column=0)
btlog.grid(row=6,column=0)


root.mainloop()
