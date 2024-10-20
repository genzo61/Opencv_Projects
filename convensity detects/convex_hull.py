import cv2
import numpy as np 
img = cv2.imread("map.jpg")
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
blur = cv2.blur(gray,(3,3))
ret, thresh = cv2.threshold(blur,30,255,cv2.THRESH_BINARY)

counturs, hiearshy = cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
hull = []
for i in range(len(counturs)):
    hull.append(cv2.convexHull(counturs[i],False))
bg = np.zeros((thresh.shape[0],thresh.shape[1],3),np.uint8)
for i in range(len(counturs)):
    cv2.drawContours(bg,counturs,i,(0,0,255),3,8)
    cv2.drawContours(bg,hull,i,(0,255,0),1,8)    

cv2.imshow("ımage",bg)
cv2.waitKey(0)
cv2.destroyAllWindows()