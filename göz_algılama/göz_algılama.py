import cv2 

img = cv2.imread("eye.png")
img =
eye_cascade = cv2.CascadeClassifier("eye.xml")
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
eyes = eye_cascade.detectMultiScale(gray,1.3,5)
for (x,y,w,h) in eyes:
    cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,255),3)

img2 = img[y:y+h:x+w]
gray2 = gray[y:y+h:x+w]

eyes = eye_cascade.detectMultiScale(gray2)
for (ex,ey,ew,eh) in eyes:
    cv2.rectangle(img2,(ex,ey),(ex+ew,ey+eh),(255,0,0),2)

cv2.imshow("img",img2)
cv2.waitKey(0)
cv2.destroyAllWindows()