from tkinter import *

window = Tk()
km = StringVar()
miles = None

def km_to_miles():
    print(km.get())
    miles = float(km.get()) * 1.6
    t1.insert(END, miles)

# Widgets between window = tk() and mainloop
b1 = Button(window, text="Execute", command=km_to_miles)
b1.grid(row=0,column=0)

e1 = Entry(window, textvariable=km)
e1.grid(row=0, column=1)

t1 = Text(window, height=1, width=20)
t1.grid(row=0, column=2)


window.mainloop()