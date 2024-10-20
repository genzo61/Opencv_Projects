import cv2
cv2.namedWindow("klon")
img = cv2.imread("klon61.jpg")

img = cv2.resize(img,(300,450))

cv2.imshow("klon",img)
cv2.waitKey(0)
cv2.destroyAllWindows()