import cv2 
import numpy as np

img = cv2.imread("klon.jpg")
# color = img[150,200] pikselleri görmek için böyle...
dimention = img.shape
print(dimention)

color = img[300,450]
print(color)

blue = img[300,450,0]
print(blue)

green = img[300,450,1]
print(green)

red = img[300,450,2]
print(red)


img[300,450,0] = 250
print("new blue : ",img[300,450,0])


blue1 = img.item(150,200,0)
print("blue1 : ",blue1)
img.itemset((150,200,0),172) # pikselin değeri değişmiştir.
print("new blue1 : ",img[150,200,0])


cv2.imshow("klon asker", img)

cv2.waitKey(0)
cv2.destroyAllWindows()