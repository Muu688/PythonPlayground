from tkinter import *

window = Tk()
kg = StringVar()
miles = None

def convert():
    grams = float(kg.get()) * 1000
    pounds = float(kg.get()) * 2.20462
    ounces = float(kg.get()) * 35.274
    tGrams.insert(END, grams)
    tPounds.insert(END, pounds)
    tOunces.insert(END, ounces)

# Widgets between window = tk() and mainloop

l1 = Label(window, text="Kg")
l1.grid(row=0, column=0)

e1 = Entry(window, textvariable=kg)
e1.grid(row=0, column=1)

b1 = Button(window, text="Convert", command=convert)
b1.grid(row=0,column=2)

tGrams = Text(window, height=1, width=20)
tGrams.grid(row=1, column=0)

tPounds = Text(window, height=1, width=20)
tPounds.grid(row=1, column=1)

tOunces = Text(window, height=1, width=20)
tOunces.grid(row=1, column=2)

window.mainloop()