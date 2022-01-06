from tkinter import *
from tkinter import ttk
import tkinter as tk

# Function to update expression
# in the text entry box
def press(num):
    # point out the global expression variable
    global expression
    operations = ("*", "+", "-", "÷")
    expression = str(expression) # Always treat as string
    if(expression.endswith(operations) and num in operations):
        return

    # concatenation of string
    expression = expression + str(num)
 
    # update the expression by using set method
    equation.set(expression)
 
def clear():
    global expression
    expression=""
    equation.set("") 

def easterEggs():
    global expression
    if (str(expression) in ("420", "69", "42069", "69420", "58,008")):
        content.config(background='Black')
        oneButton.config(background='Green')
        twoButton.config(background='Yellow')
        threeButton.config(background='Blue')
        fourButton.config(background='Pink')
        fiveButton.config(background='Grey')
        sixButton.config(background='Orange')
        sevenButton.config(background='Purple')
        eightButton.config(background='Brown')
        nineButton.config(background='Green')
        btn_Clear.config(background='Yellow')
        btn_Zero.config(background='Blue')
        btn_Decimalpoint.config(background='Pink')
        btn_Equals.config(background='Grey')
        btn_Add.config(background='Orange')
        btn_Subtract.config(background='Purple')
        btn_Multiply.config(background='Brown')
        btn_Divide.config(background='Red')
        btn_Back.config(background='Pink')
    else:   
        content.config(background='White')
        oneButton.config(background='White')
        twoButton.config(background='White')
        threeButton.config(background='White')
        fourButton.config(background='White')
        fiveButton.config(background='White')
        sixButton.config(background='White')
        sevenButton.config(background='White')
        eightButton.config(background='White')
        nineButton.config(background='White')
        btn_Clear.config(background='White')
        btn_Zero.config(background='White')
        btn_Decimalpoint.config(background='White')
        btn_Equals.config(background='White')
        btn_Add.config(background='White')
        btn_Subtract.config(background='White')
        btn_Multiply.config(background='White')
        btn_Divide.config(background='White')
        btn_Back.config(background='White')

def calculate():
    try:
        global expression
        if("÷0" in str(expression)):
            expression = str(expression).replace("÷0","")
        expression = cleanseInput()
        total = str(eval(expression))
        expression = total
        equation.set(total)
        easterEggs()
    except:
        equation.set(" error ")
        expression = ""

def cleanseInput():
     global expression
     expression = str(expression).replace("÷","/")
     expression = str(expression).replace("x","*")
     return expression
 

def backsp():
    global expression
    expression = str(expression[:-1])
    equation.set(expression) 

root = Tk()
root.geometry("400x500")
root.title("Calculator")

# globally declare the expression variable
expression = ""
 
equation = StringVar()

buttonWidth=12
buttonHeight=4
buttonPadX=-10
buttonPadY=-8

content = tk.Frame(root)
content.config(height=550)
input = ttk.Entry(content, textvariable=equation, justify=RIGHT, font=("Calibri",28))
btn_Back = tk.Button(content, text="⌫", command=lambda: backsp(), width=buttonWidth, height=buttonHeight, padx=buttonPadX, pady=buttonPadY,)
btn_Divide = tk.Button(content, text="÷", command=lambda:press('÷'), width=buttonWidth, height=buttonHeight, padx=buttonPadX, pady=buttonPadY)
btn_Multiply = tk.Button(content, text="x", command=lambda:press('x'), width=buttonWidth, height=buttonHeight, padx=buttonPadX, pady=buttonPadY)
btn_Subtract = tk.Button(content, text="-", command=lambda:press('-'), width=buttonWidth, height=buttonHeight, padx=buttonPadX, pady=buttonPadY)
btn_Add = tk.Button(content, text="+", command=lambda:press('+'), width=buttonWidth, height=buttonHeight, padx=buttonPadX, pady=buttonPadY)
btn_Equals = tk.Button(content, text="=", command=lambda:calculate(), width=buttonWidth, height=buttonHeight, padx=buttonPadX, pady=buttonPadY)
btn_Decimalpoint = tk.Button(content, text=".", command=lambda:press('.'), width=buttonWidth, height=buttonHeight, padx=buttonPadX, pady=buttonPadY)
btn_Zero = tk.Button(content, text="0", command=lambda:press(0), width=buttonWidth, height=buttonHeight, padx=buttonPadX, pady=buttonPadY)
btn_Clear = tk.Button(content, text="C", command=lambda:clear(), width=buttonWidth+14, height=buttonHeight, padx=buttonPadX, pady=buttonPadY)

oneButton = tk.Button(
    master=content,
    text="1",
    command=lambda: press(1),
    width=buttonWidth, height=buttonHeight, padx=buttonPadX, pady=buttonPadY
)

twoButton = tk.Button(
    master=content,
    text="2",
    command=lambda: press(2),
    width=buttonWidth, height=buttonHeight, padx=buttonPadX, pady=buttonPadY
)

threeButton = tk.Button(
    master=content,    
    text="3",
    command=lambda: press(3),
    width=buttonWidth, height=buttonHeight, padx=buttonPadX, pady=buttonPadY
)

fourButton = tk.Button(
    master=content,
    text="4",
    command=lambda: press(4),
    width=buttonWidth, height=buttonHeight, padx=buttonPadX, pady=buttonPadY
)

fiveButton = tk.Button(
    master=content,
    text="5",
    command=lambda: press(5),
    width=buttonWidth, height=buttonHeight, padx=buttonPadX, pady=buttonPadY
)

sixButton = tk.Button(
    master=content,
    text="6",
    command=lambda: press(6),
    width=buttonWidth, height=buttonHeight, padx=buttonPadX, pady=buttonPadY
)

sevenButton = tk.Button(
    master=content,
    text="7",
    command=lambda: press(7),
    width=buttonWidth, height=buttonHeight, padx=buttonPadX, pady=buttonPadY
)

eightButton = tk.Button(
    master=content,
    text="8",
    command=lambda: press(8),
    width=buttonWidth, height=buttonHeight, padx=buttonPadX, pady=buttonPadY
)

nineButton = tk.Button(
    master=content,
    text="9",
    command=lambda: press(9),
    width=buttonWidth, height=buttonHeight, padx=buttonPadX, pady=buttonPadY
)

zeroButton = tk.Button(
    master=content,
    text="0",
    command=lambda: press(0),
    width=buttonWidth, height=buttonHeight, padx=buttonPadX, pady=buttonPadY
)

content.grid(column=0, row=0)
input.grid(column=0, row=0, columnspan=6, rowspan=2)
btn_Back.grid(column=2, row=3)
btn_Clear.grid(column=0, row=3, columnspan=2)
btn_Divide.grid(column=3, row=3)
btn_Multiply.grid(column=3, row=4)
btn_Subtract.grid(column=3, row=5)
btn_Add.grid(column=3, row=6)
btn_Equals.grid(column=3, row=7)
btn_Zero.grid(column=1, row=7)
btn_Decimalpoint.grid(column=2, row=7)
oneButton.grid(column=0, row=6)
twoButton.grid(column=1, row=6)
threeButton.grid(column=2, row=6)
fourButton.grid(column=0, row=5)
fiveButton.grid(column=1, row=5)
sixButton.grid(column=2, row=5)
sevenButton.grid(column=0, row=4)
eightButton.grid(column=1, row=4)
nineButton.grid(column=2, row=4)

root.mainloop()

