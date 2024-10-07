import cv2
import numpy as np

img1 = cv2.imread("bitwise_1.png")
img2 = cv2.imread("bitwise_2.png")

bit_and = cv2.bitwise_and(img2, img1)  # siyah = 1 beyaz = 0 diye kodla 
bit_or = cv2.bitwise_or(img2,img1)


cv2.imshow("img1", img1)
cv2.imshow("img2", img2)
cv2.imshow("bit_and",bit_and)
cv2.imshow("bit_or",bit_or)

cv2.waitKey(0)
cv2.destroyAllWindows()