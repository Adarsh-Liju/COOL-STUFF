from Tkinter import *
#Look at this awesome code created by Adarsh!
#creating buttons
root = Tk() #creates a window
root.title("Simple Calculator")

e = Entry(root , width = 40, borderwidth = 5)
e.grid(row = 0 , column = 0 , columnspan = 3 , padx = 10, pady = 10)

def click(number):
     current = e.get()
     e.delete(0,END)
     e.insert(0, str(current) + str(number))
     

def clear():
     e.delete(0,END)

def add():
     f_n = e.get()
     global f_num
     global math
     math = "addition"
     f_num = int(f_n)
     e.delete(0,END)

def squareroot():
     f_n = e.get()
     global f_num
     global math
     math = "squareroot"
     f_num = int(f_n)
     e.delete(0,END)

def sub():
     f_n = e.get()
     global f_num
     global math
     math = "subtraction"
     f_num = int(f_n)
     e.delete(0,END)

def mul():
     f_n = e.get()
     global f_num
     global math
     math = "multiplication"
     f_num = int(f_n)
     e.delete(0,END)

def div():
     f_n = e.get()
     global f_num
     global math
     math = "division"
     f_num = int(f_n)
     e.delete(0,END)

def exponent():
     f_n = e.get()
     global f_num
     global math
     math = "exponent"
     f_num = int(f_n)
     e.delete(0,END)

def equal():
     s_num=0

     if math == "addition":
          s_num = int(e.get())
          e.delete(0, END)
          e.insert(0 , "ADDITION RESULT :" + str(f_num + s_num))
     elif math == "subtraction":
          s_num = int(e.get())
          e.delete(0, END)
          e.insert(0 ,"SUBTRACTION  RESULT :" +str(f_num - s_num))
     elif math == "multiplication":
          s_num = int(e.get())
          e.delete(0, END)
          e.insert(0 , "MULTIPLICATION RESULT :" +str(f_num * s_num))
     elif math == "division":
          s_num = int(e.get())
          e.delete(0, END)
          e.insert(0 , "DIVISION RESULT :" +str(f_num ** s_num))
          e.insert(0 , f_num / s_num)
     elif math == "exponent":
          s_num = int(e.get())
          e.delete(0, END)
          e.insert(0 , "EXPONENT IS : " +str(f_num ** s_num))
     elif math == "squareroot":
          e.delete(0, END)
          e.insert(0,"SQRT IS :" + str(f_num ** 1/2))

#define buttons
bt1 = Button(root, text = "1", padx = 40 , pady = 20, command = lambda : click(1))#callback
bt2 = Button(root, text = "2", padx = 40 , pady = 20, command = lambda : click(2))#callback
bt3 = Button(root, text = "3", padx = 40 , pady = 20, command = lambda : click(3))#callback
bt4 = Button(root, text = "4", padx = 40 , pady = 20, command = lambda : click(4))#callback
bt5 = Button(root, text = "5", padx = 40 , pady = 20, command = lambda : click(5))#callback
bt6 = Button(root, text = "6", padx = 40 , pady = 20, command = lambda : click(6))#callback
bt7 = Button(root, text = "7", padx = 40 , pady = 20, command = lambda : click(7))#callback
bt8 = Button(root, text = "8", padx = 40 , pady = 20, command = lambda : click(8))#callback
bt9 = Button(root, text = "9", padx = 40 , pady = 20, command = lambda : click(9))#callback
bt0 = Button(root, text = "0", padx = 40 , pady = 20, command = lambda : click(0))#callback
btadd = Button(root, text = "+", padx = 39 , pady = 20, command = add)#callback
btsub = Button(root, text = "-", padx = 41 , pady = 20, command = sub)#callback
btmul = Button(root, text = "*", padx = 40 , pady = 20, command = mul)#callback
btdiv = Button(root, text = "/", padx = 41 , pady = 20, command = div)#callback
btexponent=Button(root, text = "^", padx = 41 , pady = 20, command =exponent)#callback

btEquals = Button(root,bg = "blue",fg = "white", text = "=", padx = 90 , pady = 20, command = equal)#callback
btClear = Button(root,bg = "red",fg = "white",text = "Clear", padx = 79 , pady = 20, command = clear)#callback
btsqrt = Button(root,text = "Sqrt", padx = 79 , pady = 20, command = squareroot)#callback

bt1.grid(row = 3, column = 0)
bt2.grid(row = 3, column = 1)
bt3.grid(row = 3, column = 2)

bt4.grid(row = 2, column = 0)
bt5.grid(row = 2, column = 1)
bt6.grid(row = 2, column = 2)

bt7.grid(row = 1, column = 0)
bt8.grid(row = 1, column = 1)
bt9.grid(row = 1, column = 2)

bt0.grid(row = 4, column = 0 )
btadd.grid(row = 5, column = 0 )
btEquals.grid(row = 5, column = 1, columnspan = 2)
btClear.grid(row = 4, column = 1, columnspan = 2)
btsqrt.grid(row = 8, column = 1, columnspan = 2)
btsub.grid(row = 6, column = 0 )
btmul.grid(row = 6, column = 1 )
btdiv.grid(row = 6, column = 2 )
btexponent.grid(row = 6, column = 2)
root.mainloop()





