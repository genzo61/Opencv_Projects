import cv2
import face_recognition

cap = cv2.VideoCapture(0)
color = (0,0,255)
while True:
    ret,frame = cap.read()
    frame = cv2.flip(frame,1)
    facelocation = face_recognition.face_locations(frame)

    for index,faceloc in enumerate(facelocation):
        toplefty,bottomrightx,bottomrighty,topleftx = faceloc
        pt1 = (topleftx,toplefty)
        pt2 = (bottomrightx,bottomrighty)
        cv2.rectangle(frame,pt1,pt2,color,2)

        cv2.imshow("Frame",frame)

    if cv2.waitKey(30) & 0xFF == ord("q"):
        break
cap.release()
cv2.destroyAllWindows()