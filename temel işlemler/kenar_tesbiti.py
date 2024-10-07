import cv2 
# cv2.Canny fonksiyonu ....  # cv2.flip --> görüntüye takla attırır....
cap = cv2.VideoCapture(0)


while True:
    ret, frame = cap.read()
    cv2.flip(frame, 1)
    adges = cv2.Canny(frame,100,200)
    cv2.imshow("Frame", frame)
    cv2.imshow("ADGES", adges)
    

    if cv2.waitKey(5) & 0xFF == ord("q"):
        break


cap.release()
cv2.destroyAllWindows()    