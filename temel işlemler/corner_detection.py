import cv2 
import numpy as np 
import matplotlib as plt

img1 = cv2.imread("61.png")
img = cv2.imread("52.png")

gray1 = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
gray = np.float32(gray1)
corners = cv2.goodFeaturesToTrack(gray,50,0.01,10)   # köşeleri bulma fonksiyon...
corners = np.int8(corners)

for corner in corners:
    x,y = corner.ravel()
    cv2.circle(img,(x,y),3,(0,0,255), -1)

cv2.imshow("corner", img)
cv2.waitKey(0)
cv2.destroyAllWindows()    
        