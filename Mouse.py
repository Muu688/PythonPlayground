import mouse

import time

mins = 1
seconds = mins * 60
origin = ["600", "300"]

while(seconds != 0):
    mouse.move(origin[0], origin[1])
    time.sleep(1)
    seconds = seconds - 1
    print(seconds)
    mouse.move("600", "500")
    time.sleep(1)
    seconds = seconds - 1
    print(seconds)
    mouse.move("600", "600")
    time.sleep(1)
    seconds = seconds - 1
    print(seconds)
    mouse.move("600", "700")
    time.sleep(1)
    seconds = seconds - 1
    print(seconds)
    mouse.move("600", "800")
    time.sleep(1)
    seconds = seconds - 1
    print(seconds)

