import cv2
import mediapipe as mp
import time
import math

# Use first webcam
cap = cv2.VideoCapture(0)

# Hands model
mpHands = mp.solutions.hands
hands = mpHands.Hands()

# Draw utilz
mpDraw = mp.solutions.drawing_utils

# Time variables
pTime = 0
cTime = 0


while True:
    success, img = cap.read()    # read the image

    imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    results = hands.process(imgRGB)

    # Checking whether if hand is in there
    # print(results.multi_hand_landmarks)

    mpHands = mp.solutions.hands
    hands = mpHands.Hands()

    h, w, c = img.shape

    if results.multi_hand_landmarks:
        for handLms in results.multi_hand_landmarks:
            for id, lm in enumerate(handLms.landmark):
                cx, cy = int(lm.x*w), int(lm.y*h)
                print(id, cx, cy)

                if id == 8:
                    cv2.circle(img, (cx,cy), 15, (255,0,255), cv2.FILLED)

            mpDraw.draw_landmarks(img, handLms, mpHands.HAND_CONNECTIONS)

    # Calculating time difference and inverse to get frame per second for each frame
    cTime = time.time()
    fps = 1/(cTime - pTime)
    pTime = cTime


    #putting FPS display up
    cv2.putText(img, str(int(fps)), (20,70), cv2.FONT_HERSHEY_PLAIN, 3, (255,0,255), 3)

    cv2.imshow("Image",img)
    cv2.waitKey(1)




