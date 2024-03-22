import cv2
import time
import HandTrackingModule as htm

# Time variables
pTime = 0
cTime = 0

# Use first webcam
cap = cv2.VideoCapture(0)
detector = htm.handDetector()

while True:
    # read image input
    success, img = cap.read()
    img = detector.find_hands(img)
    lmList = detector.findPosition(img)

    if len(lmList) != 0:
        print(lmList[4])

    # time metrics
    cTime = time.time()
    fps = 1 / (cTime - pTime)
    pTime = cTime

    # putting FPS display up
    cv2.putText(img, str(int(fps)), (20, 70), cv2.FONT_HERSHEY_PLAIN, 3, (255, 0, 255), 3)
    cv2.imshow("Image", img)
    key = cv2.waitKey(1)
    if key == ord('q'):  # Exit loop if 'q' key is pressed
        break

#release camera
cap.release()
cv2.destroyAllWindows()