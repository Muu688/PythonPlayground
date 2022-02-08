import mouse

import time

mins = 30
seconds = mins * 60

while(seconds != 0):
    mouse.move("500", "500")
    time.sleep(1)
    mouse.move("1000", "1000")
    mins = mins - 1

