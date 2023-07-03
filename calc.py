from tkinter import *

root = Tk()
root.title('Calculator')

def button_click(num):
    entry.insert(END,num)

def button_clear():
    entry.delete(0,END)

def button_equal():
    ans = eval(entry.get())
    entry.delete(0,END)
    entry.insert(END,ans)

def button_del():
    eq = entry.get()[:-1]
    entry.delete(0,END)
    entry.insert(END,eq)






entry = Entry(root,width=35, borderwidth=5)
entry.grid(row=0, column=0, columnspan=4,padx=10,pady=10)






btn1 = Button(root, text='1', padx=20,pady=20, command= lambda: button_click(1))
btn2 = Button(root, text='2', padx=20,pady=20, command= lambda: button_click(2))
btn3 = Button(root, text='3', padx=20,pady=20, command= lambda: button_click(3))
btn4 = Button(root, text='4', padx=20,pady=20, command= lambda: button_click(4))
btn5 = Button(root, text='5', padx=20,pady=20, command= lambda: button_click(5))
btn6 = Button(root, text='6', padx=20,pady=20, command= lambda: button_click(6))
btn7 = Button(root, text='7', padx=20,pady=20, command= lambda: button_click(7))
btn8 = Button(root, text='8', padx=20,pady=20, command= lambda: button_click(8))
btn9 = Button(root, text='9', padx=20,pady=20, command= lambda: button_click(9))
btn0 = Button(root, text='0', padx=20,pady=20, command= lambda: button_click(0))

btnEnter = Button(root, text='Enter', padx=20,pady=20, command=lambda : button_equal())
btnClear = Button(root, text='Clear', padx=20,pady=20, command=lambda: button_clear())
btnDel = Button(root, text='Del', padx=20,pady=20, command=lambda : button_del())
btnPlus = Button(root, text='+', padx=20,pady=20, command=lambda: button_click('+'))
btnMin = Button(root, text='-', padx=20,pady=20, command=lambda: button_click('-'))
btnDiv = Button(root, text='/', padx=20,pady=20, command=lambda: button_click('/'))
btnMul = Button(root, text='*', padx=20,pady=20, command=lambda: button_click('*'))
btnParL = Button(root, text='(', padx=20,pady=20, command=lambda: button_click('('))
btnParR = Button(root, text=')', padx=20,pady=20, command=lambda: button_click(')'))


btn1.grid(row=1, column=0)
btn2.grid(row=1, column=1)
btn3.grid(row=1, column=2)
btn4.grid(row=2, column=0)
btn5.grid(row=2, column=1)
btn6.grid(row=2, column=2)
btn7.grid(row=3, column=0)
btn8.grid(row=3, column=1)
btn9.grid(row=3, column=2)
btn0.grid(row=4, column=0)
btnPlus.grid(row=1,column= 3)
btnMin.grid(row=2,column= 3)
btnMul.grid(row=3,column= 3)
btnDiv.grid(row=4,column= 3)
btnEnter.grid(row=5,column= 3)
btnClear.grid(row=5,column=1)
btnDel.grid(row=5, column=0)
btnParR.grid(row=4, column=2)
btnParL.grid(row=4, column=1)



root.mainloop()
