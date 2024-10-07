import cv2
import numpy as np 

cap = cv2.VideoCapture(0)

def nothing():
    pass

cv2.namedWindow("Trackhbar")
cv2.resizeWindow("Trackhbar",500,500)

cv2.createTrackbar("Lower - H","Trackhbar",0,180,nothing)
cv2.createTrackbar("Lower - S","Trackhbar",0,255,nothing)
cv2.createTrackbar("Lower - V","Trackhbar",0,255,nothing)

cv2.createTrackbar("Upper - H","Trackhbar",0,180,nothing)
cv2.createTrackbar("Upper - S","Trackhbar",0,255,nothing)
cv2.createTrackbar("Upper - V","Trackhbar",0,255,nothing)

cv2.setTrackbarPos("Upper - H","Trackhbar",180)
cv2.setTrackbarPos("Upper - S","Trackhbar",255)
cv2.setTrackbarPos("Upper - V","Trackhbar",255)

while True:
    ret, frame = cap.read()
    frame = cv2.flip(frame, 1)

    frame_HSV = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    lower_h = cv2.getTrackbarPos("Lower - H","Trackhbar")
    lower_s = cv2.getTrackbarPos("Lower - S","Trackhbar")
    lower_v = cv2.getTrackbarPos("Lower - V","Trackhbar")

    upper_h = cv2.getTrackbarPos("Upper - H","Trackhbar")
    upper_s = cv2.getTrackbarPos("Upper - S","Trackhbar")
    upper_v = cv2.getTrackbarPos("Upper - V","Trackhbar")

    lower_color = np.array([lower_h, lower_s, lower_v])
    upper_color = np.array([upper_h, upper_s, upper_v])

    mask = cv2.inRange(frame_HSV, lower_color, upper_color)

    cv2.imshow("orijinal",frame)
    cv2.imshow("mask",mask)

    if cv2.waitKey(20) & 0xFF == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()    