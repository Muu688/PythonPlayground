import cv2
import time


# Read the Video
video=cv2.VideoCapture(0)

a=0
while True:
    a=a+1

    check, frame = video.read()

    # print(check)
    # print(frame)

    # gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)

    # Show a frame of the captured video
    cv2.imshow("hello",frame)

    key=cv2.waitKey(1)
    if key==ord('q'):
        break
    
print(a)    
cv2.destroyAllWindows()

# Release the Video Capture object
video.release()

# Apply Processing