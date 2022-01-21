import cv2, time, pandas
from datetime import datetime

# Read the Video
video=cv2.VideoCapture(0)
firstFrame = None
status_list = [None, None]
times = []
df = pandas.DataFrame(columns=["Start","End"])

while True:
    check, frame = video.read()
    isMotion=0 # No Motion
    gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    gray = cv2.GaussianBlur(gray,(21,21), 0)

    # Get our baseline to compare against by capturing the first frame
    if firstFrame is None:
        time.sleep(1)
        firstFrame=gray
        continue

    # Setup our comparisons
    delta_frame = cv2.absdiff(firstFrame,gray)
    thresh_frame = cv2.threshold(delta_frame, 30, 255, cv2.THRESH_BINARY)[1]
    thresh_frame = cv2.dilate(thresh_frame, None, iterations=2)
    (contours,_) = cv2.findContours(thresh_frame.copy(), cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    for contour in contours:
        if cv2.contourArea(contour) < 2000:
            continue
        isMotion=1 # Motion detected
        (x, y, w, h) = cv2.boundingRect(contour)
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0,255,0), 3)

    # Append timestamps for when motion enters the frame or exits the frame
    status_list.append(isMotion)
    status_list=status_list[-2:]

    if status_list[-1] == 1 and status_list[-2] == 0:
        times.append(datetime.now())
    if status_list[-1] == 0 and status_list[-2] == 1:
        times.append(datetime.now())
    # statusList.append(isMotion)

    cv2.imshow("Delta", delta_frame)
    cv2.imshow("Threshold", thresh_frame)

    # Show a frame of the captured video
    cv2.imshow("Omicron",frame)

    key=cv2.waitKey(1)
    if key==ord('q'):
        if isMotion == 1:
            times.append(datetime.now())
        break

    print(isMotion)
    
cv2.destroyAllWindows()

# Release the Video Capture object
video.release()

# Apply Processing
for time in times:
    print(time)

print(status_list)    

for i in range(0,len(times), 2):
    df=df.append({"Start":times[i], "End":times[i+1]}, ignore_index=True)

df.to_csv("Times.csv")