import cv2
import numpy as np 

img = cv2.imread("balls.jpg")
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
img_blur = cv2.medianBlur(gray,7)
circles = cv2.HoughCircles(img_blur,cv2.HOUGH_GRADIENT,1,img.shape[0]/200,param1=200,param2=10,minRadius=40,maxRadius=100)
if circles is not None:
    circles = np.uint16(np.around(circles))
    for i in circles[0,:]:
        cv2.circle(img,(i[0],i[1]),i[2],(255,0,0),2)
cv2.imshow("image",img)
cv2.waitKey(0)
cv2.destroyAllWindows()