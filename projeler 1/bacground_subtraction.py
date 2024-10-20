import cv2
import numpy as np 

cap = cv2.VideoCapture("car.mp4")
_,first_frame = cap.read()
first_frame = cv2.resize(first_frame,(640,480))
gray1 = cv2.cvtColor(first_frame,cv2.COLOR_BGR2GRAY)
blur1 = cv2.GaussianBlur(gray1,(5,5),0)
while True:
    _,frame = cap.read()
    frame = cv2.resize(frame,(640,480))
    gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    blur = cv2.GaussianBlur(gray,(5,5),0)
    diff = cv2.absdiff(gray1,blur)
    _,diff1 = cv2.threshold(diff,25,255,cv2.THRESH_BINARY)

    cv2.imshow("frame",frame)
    cv2.imshow("firs frame",first_frame)
    cv2.imshow("frame",diff1)

    if cv2.waitKey(20) & 0xFF == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()    


# ikinci videosu hazır fonksiyonlu udemy deki ...