import cv2
import numpy as np
font1 = cv2.FONT_HERSHEY_SIMPLEX
font2 = cv2.FONT_HERSHEY_COMPLEX
img = cv2.imread("polygons.png")
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
_,threshold = cv2.threshold(gray,240,255,cv2.THRESH_BINARY)
counters,_ = cv2.findContours(threshold,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
for cnt in counters:
    epsilon = 0.01 * cv2.arcLength(cnt,True)
    appprox = cv2.approxPolyDP(cnt,epsilon,True)
    cv2.drawContours(img,[appprox],0,(0),5)
    x = appprox.ravel()[0]
    y = appprox.ravel()[1]
    if len(appprox) ==3:
        cv2.putText(img,"Triangle",(x,y),font1,1,(0))
    elif len(appprox) ==4:
        cv2.putText(img,"Rectangle",(x,y),font1,1,(0))
    elif len(appprox) == 5:
        cv2.putText(img,"Pentagon",(x,y),font1,1,(0))
    elif len(appprox) == 6:
        cv2.putText(img,"Hexagon",(x,y),font2,1,(0))
    else:
        cv2.putText(img,"Elips",(x,y),font2,1,(0))

cv2.imshow("İmage",img)
cv2.waitKey(0)
cv2.destroyAllWindows()