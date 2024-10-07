import cv2
import numpy as np 

img_filter = cv2.imread("klon.jpg")
# img_median = cv2.imread("C:\\Users\\aliha\\OneDrive\\Masaüstü\\median.png")
# img_blateral = cv2.imread("C:\\Users\\aliha\\OneDrive\\Masaüstü\\bilateral.png")

blur = cv2.blur(img_filter,(7,7))   #blur bulanıklaştırmadır.
blur2 = cv2.GaussianBlur(img_filter,(7,7),cv2.BORDER_DEFAULT)
cv2.imshow("blur", blur)
cv2.imshow("orijinal", img_filter)     # medianblur tanecikli bulanıklaşmayı azaltır.  # sayılar tek sayı olacak.
cv2.imshow("blur2", blur2)

cv2.waitKey(0)
cv2.destroyAllWindows()