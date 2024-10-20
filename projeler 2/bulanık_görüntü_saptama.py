import cv2
img = cv2.imread("3.jpg")
blur = cv2.medianBlur(img,7)
lap = cv2.Laplacian(blur,cv2.CV_64F).var() # blurlu olup olmadığını anlar.
if lap<500:
    print("blurlu resim")
cv2.imshow("img",img)
cv2.imshow("blur",blur)
cv2.waitKey(0)
cv2.destroyAllWindows()