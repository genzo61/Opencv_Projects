import cv2
import numpy as np

img = cv2.imread("klon.jpg",0)

ret, th1 = cv2.threshold(img,125,255,cv2.THRESH_BINARY)


# adaptivethereshold kullan dahah belirgin olsun resim ... kılavuzdan bakkk

cv2.imshow("img",img)
cv2.imshow("th1",th1)
cv2.waitKey(0)
cv2.destroyAllWindows()