import cv2
import numpy as np 
img1 = cv2.imread("1.jpg")
img1 = cv2.resize(img1,(640,480))
img2 = cv2.imread("1.jpg")
img2 = cv2.resize(img2,(640,480))
if img1.shape == img2.shape:
    print("same size")
else:
    print("not same size")    
diff = cv2.subtract(img1,img2)
b,g,r = cv2.split(diff)
if cv2.countNonZero(b)==0 and cv2.countNonZero(g)==0 and cv2.countNonZero(r)==0:
    print("complaletly equal")
else:
    print("not equal")    

cv2.imshow("difference",diff)
cv2.waitKey(0)
cv2.destroyAllWindows()