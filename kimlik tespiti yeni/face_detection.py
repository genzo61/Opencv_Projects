import cv2
import face_recognition
img = cv2.imread("1.jpg")

face_locations = face_recognition.face_locations(img)
color = (255,0,0)
color2 = (0,0,255)
pt1_0 = (290,110)  # yüz kordinatları deneyerek yapacan mecbur...
pt2_0 = (330,155)
pt1_1 = (383,95)
pt2_1 = (435,147)
cv2.rectangle(img,pt1_0,pt2_0,color)
cv2.rectangle(img,pt1_1,pt2_1,color2)



cv2.imshow("text",img)
cv2.waitKey(0)
cv2.destroyAllWindows()

#  [(108, 333, 151, 290), (95, 435, 147, 383)] # ilk tuple birinci resmi ifade eder.