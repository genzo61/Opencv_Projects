import cv2
import face_recognition
img = cv2.imread("cr7.jpg")
img = cv2.resize(img,(640,480))
path ="cr7or.jpg"
reevesimg = face_recognition.load_image_file(path)
reevesimgencoding = face_recognition.face_encodings(reevesimg)[0]


textpath = "cr7.jpg"
imgtext = face_recognition.load_image_file(textpath)
faceloc = face_recognition.face_locations(imgtext)
faceencoding = face_recognition.face_encodings(imgtext,faceloc)
topleftx = 291
toplefty = 110
bottomrightx = 510
bottomrighty = 345
matchedfaces = face_recognition.compare_faces(reevesimgencoding,faceencoding)
if True in matchedfaces:
    cv2.rectangle(img,(topleftx,toplefty),(bottomrightx,bottomrighty),(255,0,0),2)
    cv2.putText = (img," cristiano ronaldo CR7",(topleftx,toplefty),cv2.FONT_HERSHEY_SIMPLEX,1,(0,0,255),2)
    cv2.imshow("Face Detection System",img)
else:
    cv2.rectangle(img, (topleftx, toplefty), (bottomrightx, bottomrighty), (255, 0, 0), 2)
    cv2.putText = (img, "Unnokwn person", (topleftx, toplefty), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)
    cv2.imshow("Face Detection System", img)

cv2.waitKey(0)
cv2.destroyAllWindows()