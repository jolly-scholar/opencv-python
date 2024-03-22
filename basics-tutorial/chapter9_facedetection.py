import cv2
import numpy as np

# fxn for convering BGR to HSV and increasing the image brightness
def increase_brightness(img, value=30):
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    h, s, v = cv2.split(hsv)

    lim = 255 - value
    v[v > lim] = 255
    v[v <= lim] += value

    final_hsv = cv2.merge((h, s, v))
    img = cv2.cvtColor(final_hsv, cv2.COLOR_HSV2BGR)
    return img

# Chapter 9 -
# Face detection using Viola and Jones technique.
# We will be importing pre-built cascade of XML files provided by cv2.

#Importing default XML files
faceCascade = cv2.CascadeClassifier('Resources\haarcascade_frontalface_default.xml')

# Import original image
img = cv2.imread('Resources\south_korean_team.jpg')

# Increase the brightness as needed
# img = increase_brightness(img,30)

#convert the image into grayscale img. Detection in grayscale is a lot faster.
imgGray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

#Detecting images using the provided default cascade
faces = faceCascade.detectMultiScale(imgGray,
                                     scaleFactor= 1.3,
                                     minNeighbors=1,
                                     minSize=(30,30)
                                    )
print("Found {0} faces".format(len(faces)))

#Create bounding boxes around the detected images.
for (x,y,w,h) in faces:
    cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)


cv2.imshow("Face Image", img)
cv2.waitKey(0)