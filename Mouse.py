from tkinter import *
import mouse, keyboard
import time

window = Tk()
mins = StringVar()
seconds = 0

def go():
    try:
        seconds = int(mins.get()) * 60
        while(seconds != 0):
            mouse.move("600", "100")
            time.sleep(1)
            seconds = seconds - 1
            print(seconds)
            mouse.move("600", "200")
            time.sleep(1)
            seconds = seconds - 1
            print(seconds)
            mouse.move("600", "300")
            time.sleep(1)
            seconds = seconds - 1
            print(seconds)
            mouse.move("600", "400")
            time.sleep(1)
            seconds = seconds - 1
            print(seconds)
            mouse.move("600", "500")
            time.sleep(1)
            seconds = seconds - 1
            print(seconds)
            if keyboard.is_pressed("q"):
                print("q pressed, ending loop")
                break
    except KeyboardInterrupt:
        pass

def back():
    seconds = 0

def key(event):
    kp = repr(event.char)
    print ("pressed", kp) #repr(event.char))
    if (kp == '\\x1b'):
        back()
def callback(event):
    window.focus_set()
    print("clicked at", event.x, event.y)

# Widgets between window = tk() and mainloop
w=Label(window, text="Key Pressed:")
w.grid(row=0,column=4)

l1 = Label(window, text="Mins")
l1.grid(row=0, column=0)

e1 = Entry(window, textvariable=mins)
e1.grid(row=0, column=1)

b1 = Button(window, text="AFK", command=go)
b1.grid(row=0,column=2)

b1 = Button(window, text="I'm Back", command=back)
b1.grid(row=0,column=3)

window.bind("<Key>", key)
window.mainloop()


# mins = 1
seconds = mins * 60


