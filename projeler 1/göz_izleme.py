import cv2 

cap = cv2.VideoCapture("eye_motion.mp4")




while (1):
    ret,frame = cap.read()
    if ret is False:
        break
    roi = frame[80:210,230:450]
    rows,cols,_ = roi.shape
    gray = cv2.cvtColor(roi,cv2.COLOR_BGR2GRAY)
    _,threshold = cv2.threshold(gray,3,255,cv2.THRESH_BINARY_INV)
    conters,_ = cv2.findContours(threshold,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
    conters = sorted(conters,key = lambda x: cv2.contourArea(x),reverse=True)
    for cnt in conters:
        (x,y,w,h) = cv2.boundingRect(cnt)
        cv2.rectangle(roi,(x,y),(x+w,y+h),(0,0,255),2)
        cv2.line(roi,(x+int(w/2),0),(x+int(w/2),rows),(255,0,0),2)
        cv2.line(roi,(0,y +int(h/2)),(cols,y +int (h/2)),(255,0,0),2)
        break
    frame[80:210,230:450] = roi
    cv2.imshow("frame",frame)

    if cv2.waitKey(50) & 0xFF == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()    