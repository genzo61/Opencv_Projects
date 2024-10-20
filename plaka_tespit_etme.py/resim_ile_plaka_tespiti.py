import cv2
import numpy as np
import pytesseract
import imutils

img = cv2.imread("1.jpg")
img = cv2.resize(img,(640,480))
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
filtred = cv2.bilateralFilter(gray,6,250,250)
edges = cv2.Canny(filtred,30,200)
counters = cv2.findContours(edges,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
cnts = imutils.grab_contours(counters)
cnts = sorted(cnts,key = cv2.contourArea,reverse=True)[:10]
screen = None
for c in cnts:
    epsilon = 0.018*cv2.arcLength(c,True)
    approx = cv2.approxPolyDP(c,epsilon,True)
    if len(approx) ==4:
        screen = approx
        break

mask = np.zeros(gray.shape,np.uint8)
new_img = cv2.drawContours(mask,[screen],0,(255,255,255),-1)
new_img = cv2.bitwise_and(img,img,mask=mask)

(x,y) = np.where(mask == 255)
(topx,topy) = (np.min(x),np.min(y))
(lowx,lowy) = (np.max(x),np.max(y))
cropped = gray[topx:lowx + 1,topy:lowy + 1]

text = pytesseract.image_to_string(cropped,lang = "eng")
print(text)

cv2.imshow("mask",cropped)
cv2.waitKey(0)
cv2.destroyAllWindows()