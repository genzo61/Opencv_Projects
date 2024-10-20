import cv2 
import numpy as np

canvas = np.zeros((512,512,3), dtype=np.uint8) + 255

# çizgi çekmek için --> cv2.line(tuval,(baş,baş),(bit,bit),(renk,renk,renk),thickness = kalınlık )
cv2.line(canvas,(0,0),(512,512),(0,255,0),thickness=3)

# dikdörtgen çizmek için --> cv2.rectangle(tuval, (solüstkoşe,same),(sağaltköşe,same),(renk,renk,renk),thickness = kalınlık)
cv2.rectangle(canvas,(0,0),(315,315),(255,0,0),thickness=5) #kalınlığı -1 yaparsan dikdörtgenin içi dolu olur.

#çember çizme --> cv2.circle(tuval, (merkez,noktası),yarıçap,(renk,renk,renk),thickness = kalınlık)
cv2.circle(canvas,(125,125),100,(95,100,200),thickness=-1) #kalınlığı -1 yap çemberin içini doldur

#üçgen çizmek için 3 tane çizgi çizebilirsin.
p1 = (250,300)
p2 = (50,100)
p3 = (300,500)
cv2.line(canvas,p1,p2,(0,0,0),10)
cv2.line(canvas,p2,p3,(0,0,0),10)
cv2.line(canvas,p1,p3,(0,0,0),10)

# çokggenleri oluşturmak için --> cv2.polylines() kullan.





cv2.imshow("tuval",canvas)
cv2.waitKey(0)
cv2.destroyAllWindows()