import cv2

import HandTrackingModule

cap=cv2.VideoCapture(0)
detector = HandTrackingModule.handDetector()
while True:
    success,img=cap.read()
    img=detector.findHands(img)
    lmList,bbox=detector.findPosition(img,draw=False)
    if len(lmList) != 0:
        x1,y1=(lmList[4][1],lmList[4][2])
        x2,y2=(lmList[8][1],lmList[8][2])
        cv2.circle(img,(x1,y1),
       15,(255,0,255),cv2.FILLED)
        cv2.circle(img,(x2,y2),
        15,(255,0,255),cv2.FILLED)

    cv2.imshow("video",img)
    cv2.waitKey(1)