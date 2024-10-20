import cv2
import numpy as np

canvas = np.zeros((512,512,3),dtype=np.uint8) + 255


cv2.putText(canvas,"A",(300,450),cv2.FONT_HERSHEY_SIMPLEX,5,(125,200,185),cv2.LINE_AA)




cv2.imshow("ekran",canvas)
cv2.waitKey(0)
cv2.destroyAllWindows()