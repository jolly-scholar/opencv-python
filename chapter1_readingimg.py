import cv2
import numpy as np

print("Chapter 1")

#importing PNG file
img = cv2.imread("Resources/Kobe.png")
kernel = np.ones((5,5),np.uint8)


#Converting original image
imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)         #To grayscale
imgBlur = cv2.GaussianBlur(img,(7,7),0)                 #To Blur
imgCanny = cv2.Canny(imgGray,100,100)                   #Detect edges
imgDilate = cv2.dilate(imgCanny,kernel,iterations=1)    #Dilate edges
imgEroded = cv2.erode(imgDilate, kernel, iterations=1)  #Erode edges


while True:
    cv2.imshow("Original Output", img)
    cv2.imshow("Gray Output", imgGray)
    cv2.imshow("Blur Output", imgBlur)
    cv2.imshow("Canny Output", imgCanny)
    cv2.imshow("Dilation Output", imgDilate)



    # Exit when Q is pressed
    key = cv2.waitKey(1)
    if key == ord('q'):
        break

