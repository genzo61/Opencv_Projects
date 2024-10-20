import cv2 
img = cv2.imread("ucgen.png")
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
ret,thresh = cv2.threshold(gray,127,255,cv2.THRESH_BINARY)

counters,_ = cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
cnt = counters[0]
area = cv2.contourArea(cnt)          # alandır print ile yazdırabilirsin.
M = cv2.moments(cnt)
perimeter = cv2.arcLength(cnt,True)  # çevresidir print ile yazdırabilirsın
"""
cv2.imshow("original",img)
cv2.imshow("gray",gray)
cv2.imshow("threshold",thresh)

"""

cv2.waitKey(0)
cv2.destroyAllWindows()