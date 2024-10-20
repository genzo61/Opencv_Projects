import cv2
cap = cv2.VideoCapture("body.mp4")
body_cascade = cv2.CascadeClassifier("fullbody.xml")

while True:
    ret,frame = cap.read()
    # frame = cv2.flip(frame,1)
    gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    bodies = body_cascade.detectMultiScale(gray,1.1,4)
    for (x,y,w,h) in bodies:
        cv2.rectangle(frame,(x,y),(x + w, y + h),(0,255,0),4)

    cv2.imshow("frame",frame)

    if cv2.waitKey(30) & 0xFF == ord("q"):
        break
cap.release()
cv2.destroyAllWindows()       