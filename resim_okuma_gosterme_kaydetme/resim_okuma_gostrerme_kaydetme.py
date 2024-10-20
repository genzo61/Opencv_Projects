import cv2

img = cv2.imread("klon.jpg")
#  print(img)

#büyütüp küçültme operasyonu
cv2.namedWindow("image",cv2.WINDOW_NORMAL)
cv2.imshow("image", img)


#resmi kayıt etme operasyonu
cv2.imwrite("klon61.jpg",img)


cv2.waitKey(0)
cv2.destroyAllWindows()