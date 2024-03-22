import cv2
import mediapipe as mp
import time


class handDetector():
    def __init__(self, mode=False, maxHands=2, modelComplex=1, detection_confidence=0.5, track_confidence=0.5):
        self.mode = mode
        self.maxHand = maxHands
        self.model_complexity = modelComplex
        self.detection_confidence = detection_confidence
        self.track_confidence = track_confidence

        self.mpHands = mp.solutions.hands
        self.hands = self.mpHands.Hands(self.mode,  self.maxHand, self.model_complexity,
                                        self.detection_confidence, self.track_confidence)
        self.mpDraw = mp.solutions.drawing_utils


    def find_hands(self, img, draw=True):
        img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        self.results = self.hands.process(img_rgb)
        if self.results.multi_hand_landmarks:
            for handLms in self.results.multi_hand_landmarks:
                if draw:
                    self.mpDraw.draw_landmarks(img, handLms, self.mpHands.HAND_CONNECTIONS)
        return img

    def findPosition(self, img, handNo=0, draw=True):

        h, w, c = img.shape
        # store landmark list
        lmList=[]

        if self.results.multi_hand_landmarks:
            myHand  = self.results.multi_hand_landmarks[handNo]

            for id, lm in enumerate(myHand.landmark):
                cx, cy = int(lm.x * w), int(lm.y * h)
                lmList.append([id, cx, cy])
                if draw:
                    cv2.circle(img, (cx, cy), 2, (255, 0, 255), cv2.FILLED)

        return lmList

def main():
    # Time variables
    pTime = 0
    cTime = 0

    # Use first webcam
    cap = cv2.VideoCapture(0)
    detector = handDetector()

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
        if key == ord('q'):
            break
        
        cap.release()
        cv2.destroyAllWindows()


if __name__ == "__main__":
    main()
