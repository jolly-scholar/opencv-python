import cv2
import numpy as np

print("Chapter 3")

#importing PNG file
img = cv2.imread("Resources/spacestation.png")
print(img.shape)

cv2.imshow("Original Output", img)

#resizing the image
imgResize = cv2.resize(img,(300,200))
cv2.imshow("Resized Output", imgResize)


#Cropping
imgCropped = img[0:200,200:500]
cv2.imshow("Cropped Output", imgCropped)

while True:

    # Exit when Q is pressed
    key = cv2.waitKey(1)
    if key == ord('q'):
        break
