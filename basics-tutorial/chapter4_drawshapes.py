# Chapter 4 - Drawing and putting text over images

import cv2
import numpy as np

#creating 512X512 3 channels RGB
img = np.zeros((512,512,3),np.uint8)
print(img)

#Making it blue (whole image)
#img[:]=255,0,0

#making it red on specific parts
#img[200:300, 400:500] = 255,0,0

#Drawing a line diagonal
cv2.line(img,(0,0),(img.shape[1],img.shape[0]),(0,255,0),5)
cv2.line(img,(0,img.shape[0]),(img.shape[1],0),(0,255,0),5)

#Rectangle
cv2.rectangle(img,(0,0),(img.shape[0],img.shape[1]),(0,0,255),4)

#Circle
cv2.circle(img,((img.shape[1]//2),(img.shape[0]//2)),30,(255,255,0),5)

#Text input
cv2.putText(img," OPENCV ", (300,300),cv2.FONT_HERSHEY_SIMPLEX,1,(0,150,0),2)

cv2.imshow("image",img)


cv2.waitKey(0)