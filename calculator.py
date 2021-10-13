from tkinter import *
import math

gui = Tk()
gui.configure(background="grey")
gui.title("Calculator")
gui.geometry("412x226")

result = ""
equation = StringVar()
entrResult = Entry(gui, text=equation)
entrResult.grid(columnspan=10, ipadx=150)
def press(num):
    global result
    result = result + str(num)
    equation.set(result)

def sqroot():
    global result
    if float(result)>=0:
        result = str(math.sqrt(float(result)))
        equation.set(result)
    else:
        equation.set('error')
        result = ""


def equal():
    try:
        global result
        total = str(eval(result))
        equation.set(total)
        result = total
    except:
        equation.set('error')
        result = ""

def clear():
    global result
    result = ""
    equation.set("")


btn0 = Button(gui, text='0', fg="black", bg="light blue", command=lambda: press(0), height=2, width=10)
btn0.grid(row=5, column=0)

btn1 = Button(gui, text='1', fg="black", bg="light blue", command=lambda: press(1), height=2, width=10)
btn1.grid(row=4, column=0)

btn2 = Button(gui, text='2', fg="black", bg="light blue", command=lambda: press(2), height=2, width=10)
btn2.grid(row=4, column=1)

btn3 = Button(gui, text='3', fg="black", bg="light blue", command=lambda: press(3), height=2, width=10)
btn3.grid(row=4, column=2)

btn4 = Button(gui, text='4', fg="black", bg="light blue", command=lambda: press(4), height=2, width=10)
btn4.grid(row=3, column=0)

btn5 = Button(gui, text='5', fg="black", bg="light blue", command=lambda: press(5), height=2, width=10)
btn5.grid(row=3, column=1)

btn6 = Button(gui, text='6', fg="black", bg="light blue", command=lambda: press(6), height=2, width=10)
btn6.grid(row=3, column=2)

btn7 = Button(gui, text='7', fg="black", bg="light blue", command=lambda: press(7), height=2, width=10)
btn7.grid(row=2, column=0)

btn8 = Button(gui, text='8', fg="black", bg="light blue", command=lambda: press(8), height=2, width=10)
btn8.grid(row=2, column=1)

btn9 = Button(gui, text='9', fg="black", bg="light blue", command=lambda: press(9), height=2, width=10)
btn9.grid(row=2, column=2)

btnminus = Button(gui, text='-', fg="white", bg="dark blue", command=lambda: press("-"), height=2, width=10)
btnminus.grid(row=3, column=3)

btnplus = Button(gui, text='+', fg="white", bg="dark blue", command=lambda: press("+"), height=2, width=10)
btnplus.grid(row=4, column=3)

btndiv = Button(gui, text='/', fg="white", bg="dark blue", command=lambda: press("/"), height=2, width=10)
btndiv.grid(row=5, column=3)

btnmult = Button(gui, text='x', fg="white", bg="dark blue", command=lambda: press("*"), height=2, width=10)
btnmult.grid(row=2, column=3)

btneq = Button(gui, text='=', fg="white", bg="dark red", command=equal, height=2, width=10)
btneq.grid(row=6, column=3)

btncl = Button(gui, text='C', fg="white", bg="purple", command=clear, height=2, width=10)
btncl.grid(row=6, column=0)

btndot = Button(gui, text='.', fg="white", bg="blue", command=lambda: press("."), height=2, width=10)
btndot.grid(row=6, column=2)

btnmod = Button(gui, text='mod', fg="white", bg="black", command=lambda: press("%"), height=2, width=10)
btnmod.grid(row=4, column=4)

btnp1 = Button(gui, text='(', fg="white", bg="blue", command=lambda: press("("), height=2, width=10)
btnp1.grid(row=5, column=1)

btnp2 = Button(gui, text=')', fg="white", bg="blue", command=lambda: press(")"), height=2, width=10)
btnp2.grid(row=5, column=2)

btnpow = Button(gui, text='^', fg="white", bg="blue", command=lambda: press("**"), height=2, width=10)
btnpow.grid(row=6, column=1)

btndivv = Button(gui, text='div', fg="white", bg="black", command=lambda: press("//"), height=2, width=10)
btndivv.grid(row=5, column=4)

btnsqrt = Button(gui, text='sqrt', fg="white", bg="black", command=sqroot, height=2, width=10)
btnsqrt.grid(row=3, column=4)


gui.mainloop()