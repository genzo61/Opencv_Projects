import face_recognition
import cv2
img = cv2.imread("a.jpg")
facelocations = face_recognition.face_locations(img)







cv2.imshow("text",img)
cv2.waitKey(0)
cv2.destroyAllWindows()