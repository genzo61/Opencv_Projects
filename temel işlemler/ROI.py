import cv2

img = cv2.imread("klon.jpg")
cv2.imshow("klon : ", img)
# print(img.shape[:2])

roi = img[30:200, 200:400] # kullanımı bu şekilde...
cv2.imshow("ROI : ", roi)

cv2.waitKey(0)
cv2.destroyAllWindows()