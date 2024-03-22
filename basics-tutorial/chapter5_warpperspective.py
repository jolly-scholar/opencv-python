import cv2
import numpy as np

img = cv2.imread("Resources/Pokercards.png")

width, height = 250,350

#Getting the corner locations of the card
pts1 = np.float32([[485, 516],[568,131],[911, 168],[858, 563]])

#defining second set of points to transform the image into
pts2 = np.float32([[0,0],[0,height],[width,height],[width,0]])

#getting transformation matrix
matrix = cv2.getPerspectiveTransform(pts1,pts2)
imgOutput = cv2.warpPerspective(img,matrix,(width,height))


winname = "Output"
cv2.namedWindow(winname)

cv2.imshow(winname,imgOutput)
cv2.imshow("image",img)
cv2.moveWindow(winname,30,40)

cv2.waitKey(0)