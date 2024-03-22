import cv2
import numpy as np

#Setting the width and height of the window.
frameWidth = 640
frameHeight = 480

# Video capture
cap = cv2.VideoCapture(0)
cap.set(3,frameWidth)
cap.set(4,frameHeight)
cap.set(10,150)

# List of HSV color boundaries in order to detect the color.
# [h_min,s_min,v_min,h_max,s_max,v_max]
myColors = [[5,107,0,19,255,255], #Orange
            [56,100,0,83,255,204], #Green
            [75,79,45,132,255,255]]  #Blue

myColorValues = [[51,153,255],  ## BGR draw color values
                 [0,255,0],
                 [255,0,0]]

myPoints = [] ## [x,y,color]

def getContours(img):
    #finding the Contour: RETR_EXTERNAL retrieves outter contours.
    contours, hierarchy = cv2.findContours(img, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
    x,y,w,h = 0,0,0,0

    #loop for each contours
    for cnt in contours:
        area = cv2.contourArea(cnt)
        if area >200:
            #cv2.drawContours(imgResult, cnt, -1, (255, 0, 0), 3)
            peri = cv2.arcLength(cnt, True)
            approx = cv2.approxPolyDP(cnt, 0.02*peri,True)
            x,y,w,h = cv2.boundingRect(approx)
    return x+w//2,y

def findColor(img,myColors,myColorValues):

    imgHSV = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
    count = 0
    newPoints = []

    for color in myColors:
        lower = np.array(color[0:3])
        upper = np.array(color[3:6])
        mask = cv2.inRange(imgHSV,lower,upper)
        x,y = getContours(mask)
        cv2.circle(imgResult,(x,y),10,myColorValues[count],cv2.FILLED)

        if x!=0 and y!=0:
            newPoints.append([x,y,count])

        count += 1
        #cv2.imshow(str(color[0]), mask)

    return newPoints

def drawOnCanvas(myPoints, myColorValues):
    for point in myPoints:
        cv2.circle(imgResult,(point[0],point[1]),10,myColorValues[point[2]],cv2.FILLED)

while True:
    success, img = cap.read()
    imgResult = img.copy()
    newPoints = findColor(img,myColors,myColorValues)
    if len(newPoints) != 0:
        for newP in newPoints:
            myPoints.append(newP)
    if len(myPoints) != 0:
        drawOnCanvas(myPoints,myColorValues)

    cv2.imshow("Result",imgResult)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break