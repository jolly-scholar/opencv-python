import  cv2


# Parameter definition
########################################################
frameWidth = 640            # Display frame width
frameHeight = 480           # Display frame height
minArea = 10               # minimum area of the license plate in px
textColor = (255, 0, 0)     # Text color to display it in the image

#nPlateCascade = cv2.CascadeClassifier('Resources\haarcascade_russian_plate_number.xml')
nPlateCascade = cv2.CascadeClassifier('Resources\haarcascade_frontalface_default.xml')


########################################################


cap = cv2.VideoCapture(0)
cap.set(3,frameWidth)
cap.set(4,frameHeight)
cap.set(10,100)

count = 0

while True:
    success, img = cap.read()

    # Detecting number plates using the nPlateCascade file
    numberPlates = nPlateCascade.detectMultiScale(img,
                                     scaleFactor= 1.1,
                                     minNeighbors=4,
                                     minSize=(30,30)
                                    )

    # Create bounding boxes around the detected images.
    for (x, y, w, h) in numberPlates:
        area = w*h
        if area > minArea:
            cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)
            cv2.putText(img,"NumberPlates", (x,y-5),
                        cv2.FONT_HERSHEY_COMPLEX_SMALL,1,textColor,2)
            imgRoi = img[y:y+h, x:x+w]  # Cropping region of interest
            cv2.imshow("Roi", imgRoi)


    cv2.imshow("Result", img)
    if cv2.waitKey(1) & 0xFF == ord('s'):
        cv2.imwrite("Resources/Scanned/NoPlate_" + str(count) + ".jpg", imgRoi)
        cv2.rectangle(img, (0,200),(640,300),(0,255,0),cv2.FILLED)
        cv2.putText(img,"Scan Saved", (150,265), cv2.FONT_HERSHEY_DUPLEX,
                    2,(0,0,255),2)
        cv2.imshow("Result", img)
        cv2.waitKey(500)
        count += 1
    elif cv2.waitKey(1) & 0xFF == ord('q'):
        break
