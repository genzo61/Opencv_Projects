import cv2 
windowname = "live video"
cv2.namedWindow(windowname)
cap = cv2.VideoCapture(0)
print("width : " + str(cap.get(3)))
print("high : " + str(cap.get(4)))
cap.set(3,1280)
cap.set(4,720)
print("width* : " + str(cap.get(3)))
print("high* : " + str(cap.get(4)))
while(1):
    ret,frame = cap.read()
    frame = cv2.flip(frame,1)
    cv2.imshow("frame",frame)

    if cv2.waitKey(20)==27:
        break
cap.release()
cv2.destroyAllWindows()    