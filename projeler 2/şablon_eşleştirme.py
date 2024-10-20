import cv2
import numpy as np 

img = cv2.imread("3.jpg")
template = cv2.imread("3.2.jpg",0)
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
w,h = template.shape[::-1]
result = cv2.matchTemplate(gray,template,cv2.TM_CCOEFF_NORMED)
location = np.where(result>=0.9)
for point in zip(*location[::-1]):
    cv2.rectangle(img,point,(point[0]+w,point[1]+h),(255,0,0),3)


cv2.imshow("img",img)
cv2.imshow("template",template)
cv2.imshow("result",result)
cv2.waitKey(0)
cv2.destroyAllWindows()