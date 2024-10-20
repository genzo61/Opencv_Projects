import cv2 

cap = cv2.VideoCapture(0)
face_cascade = cv2.CascadeClassifier("1.xml") # veya burada hata var

while True:
    ret,frame = cap.read()
    cv2.flip(frame,1)
    gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray,1.3,4)  # burada hata 
    for (x,y,w,h) in faces:
        cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),2)
    cv2.imshow("img",frame)

    if cv2.waitKey(20) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()    