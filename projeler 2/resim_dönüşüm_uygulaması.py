import cv2 
import numpy as np 
def nothing(x):
    pass
img1 = cv2.imread("1.jpg")
img1_r = cv2.resize(img1,(640,480))
img2 = cv2.imread("3.jpg")
img2_r = cv2.resize(img2,(640,480))
outpute = cv2.addWeighted(img1_r,0.5,img2_r,0.5,0)
windowname = "live window"
cv2.namedWindow(windowname)

cv2.createTrackbar("Alpha - Beta",windowname,0,1000,nothing)
while True:
    cv2.imshow(windowname,outpute)
    alpha = cv2.getTrackbarPos("Alpha - Beta",windowname)/1000
    beta = 1 - alpha
    outpute = cv2.addWeighted(img1_r,alpha,img2_r,beta,0)
    if cv2.waitKey(1) == 27:
        break
cv2.destroyAllWindows()    