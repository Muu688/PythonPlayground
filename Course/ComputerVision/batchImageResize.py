import cv2
from random import seed
from random import randint

import cv2
import os

def load_images_from_folder(folder):
    images = []
    for filename in os.listdir(folder):
        img = cv2.imread(os.path.join(folder,filename), 1)
        if img is not None:
            images.append(img)
    return images

def resize_Image(image):
    rezised=cv2.resize(image, (100,100))
    seed(100)
    randomNumber = randint(1,1000)
    cv2.imwrite(str(randomNumber) + "_resized.jpg", rezised)
    print("maybe it worked...?")

# images = load_images_from_folder("C:\\Users\\rapid\\source\\repos\\PythonPlayground\\Course\\ComputerVision\\resizeme")
# print(len(images))
# for img in images:
#     resize_Image(img)
#     # print(img)


# Their Solution (Works)
import glob

images = glob.glob("*.jpg")

for img in images:
    image=cv2.imread(img, 1)
    resized=cv2.resize(image,(100,100))
    cv2.imshow("hello",resized)
    cv2.waitKey(500)
    cv2.destroyAllWindows()
    cv2.imwrite("resized_" + img,resized)

print('Images processed for current directory')