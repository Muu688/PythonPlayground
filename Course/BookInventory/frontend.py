from tkinter import *

from itsdangerous import exc
from backend import Database

database = Database("books.db")
window = Tk()
title = StringVar()
author = StringVar()
isbn = StringVar()
year = StringVar()

def view_command():
    lbox1.delete(0,END)
    for row in database.view():
        print(row)
        lbox1.insert(END,row)
        
def search_command():
    lbox1.delete(0,END)
    for row in database.search(eTitle.get(), eAuth.get(), eYear.get(), eISBN.get()):
        lbox1.insert(END,row)

def add_command():
    database.insert(eTitle.get(), eAuth.get(), eYear.get(), eISBN.get())
    lbox1.delete(0,END)
    lbox1.insert(END, (eTitle.get(), eAuth.get(), eYear.get(), eISBN.get()))

def get_selected_row(event):
    try:
        global selected_tuple
        index=lbox1.curselection()[0]
        selected_tuple=lbox1.get(index)
        eTitle.delete(0,END)
        eTitle.insert(END,selected_tuple[1])
        eAuth.delete(0,END)
        eAuth.insert(END,selected_tuple[2])
        eYear.delete(0,END)
        eYear.insert(END,selected_tuple[3])
        eISBN.delete(0,END)
        eISBN.insert(END,selected_tuple[4])
    except IndexError:
        pass

def delete_command():
    database.delete(selected_tuple[0])

def update_command():
    database.update(selected_tuple[0], eTitle.get(), eAuth.get(), eYear.get(), eISBN.get())
    view_command()

# Widgets between window = tk() and mainloop

l1 = Label(window, text="Title")
l1.grid(row=0, column=0)

eTitle = Entry(window, textvariable=title)
eTitle.grid(row=0, column=1)

l1 = Label(window, text="Author")
l1.grid(row=0, column=2)

eAuth = Entry(window, textvariable=author)
eAuth.grid(row=0, column=3)

l1 = Label(window, text="Year")
l1.grid(row=1, column=0)

eYear = Entry(window, textvariable=year)
eYear.grid(row=1, column=1)

l1 = Label(window, text="ISBN")
l1.grid(row=1, column=2)

eISBN = Entry(window, textvariable=isbn)
eISBN.grid(row=1, column=3)

lbox1 = Listbox(window, height=6, width=35)
lbox1.grid(row = 2, column= 0, rowspan=6, columnspan=2)

sbar1 = Scrollbar(window)
sbar1.grid(row = 2, column = 2, rowspan=6)
lbox1.config(yscrollcommand=sbar1.set)
sbar1.config(command=lbox1.yview)
lbox1.bind("<<ListboxSelect>>", get_selected_row)

# Buttons
b1 = Button(window, text="View All", command=view_command)
b1.grid(row=3,column=3)

b2 = Button(window, text="Search Entry", command=search_command)
b2.grid(row=4,column=3)

b3 = Button(window, text="Add Entry", command=add_command)
b3.grid(row=5,column=3)

b4 = Button(window, text="Update Selected", command=update_command)
b4.grid(row=6,column=3)

b5 = Button(window, text="Delete Selected", command=delete_command)
b5.grid(row=7,column=3)

b6 = Button(window, text="Close", command=window.destroy)
b6.grid(row=8,column=3)

window.mainloop()