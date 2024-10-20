import cv2 
import numpy as np
def nothing(x):
    pass 
cap = cv2.VideoCapture(0)
cv2.namedWindow("trackbar")
cv2.createTrackbar("LH","trackbar",0,179,nothing)
cv2.createTrackbar("LS","trackbar",0,255,nothing)
cv2.createTrackbar("LV","trackbar",0,255,nothing)
cv2.createTrackbar("UH","trackbar",0,179,nothing)
cv2.createTrackbar("US","trackbar",0,255,nothing)
cv2.createTrackbar("UV","trackbar",0,255,nothing)



while 1:
    _,frame = cap.read()
    frame = cv2.flip(frame,1)
    hsv = cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
    lh = cv2.getTrackbarPos("LH","trackbar")
    ls = cv2.getTrackbarPos("LS","trackbar")
    lv = cv2.getTrackbarPos("LS","trackbar")
    uh = cv2.getTrackbarPos("UH","trackbar")
    us = cv2.getTrackbarPos("US","trackbar")
    uv = cv2.getTrackbarPos("UV","trackbar")

    lower_blue = np.array([ls,ls,lv])
    upper_blue = np.array([uh,us,uv])
    mask = cv2.inRange(hsv,lower_blue,upper_blue)
    bitwise = cv2.bitwise_and(frame,frame,mask=mask)
    cv2.imshow("frame",frame)
    cv2.imshow("mask",mask)
    cv2.imshow("bitwise",bitwise)

    if cv2.waitKey(20) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()    