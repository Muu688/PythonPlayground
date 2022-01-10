import cv2

img = cv2.imread('20211212_134322.jpg', 1)
print(img.shape)
rezised=cv2.resize(img, (int(img.shape[1]/4),int(img.shape[0]/4)))
cv2.imshow("Bogong", rezised)
cv2.waitKey(20000)
cv2.destroyAllWindows()
cv2.imwrite("new image.jpg", rezised)