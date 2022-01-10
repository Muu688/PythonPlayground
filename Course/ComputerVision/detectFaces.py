import cv2

face_cascade=cv2.CascadeClassifier("haarcascade_frontalface_default.xml") #Select the Haar Cascade (Can be other ones)

img=cv2.imread("weeee.jpg") # Read the Image we want to search for faces in
gray_img=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY) # Convert to Grey (Because it is better to use Grayscale when processing images for recognition)

faces=face_cascade.detectMultiScale(gray_img, 
scaleFactor=1.2,
minNeighbors=5) # 5% scale less in the image to search for faces (scaleFactor)

for x, y, w, h in faces:
    img=cv2.rectangle(img, (x,y), (x+w,y+h), (0,255,0), 3) # Draw a GREEN rectangle over the face that has been detected.

# print(type(faces))
# print(faces)

print(img.shape)
if img.shape[0] > 1000 or img.shape[1] > 1000:
    resized=cv2.resize(img, (int(img.shape[1]/4),int(img.shape[0]/4)))
else:
    resized=img


cv2.imshow("Faces", resized)
cv2.waitKey(0)
cv2.destroyAllWindows()

