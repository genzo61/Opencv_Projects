import cv2
import numpy as np 
import math
cap = cv2.VideoCapture(0)

def findmaxcounter(counters):
    max_i = 0
    max_Area = 0
    for i in range(len(counters)):
        area_hand = cv2.contourArea(counters[i])
        if max_Area < area_hand:
            max_Area = area_hand
            max_i = i
            try:
                c = counters[max_i]
            except:
                counters = [0]
                c = counters[0]

            return c

while True:
    ret,frame = cap.read()
    frame = cv2.flip(frame,1)
    roi = frame[50:250,200:400] # frame[y1:y2,x1:x2]
    cv2.rectangle(frame,(200,50),(400,250),(0,0,255),0)
    hsv = cv2.cvtColor(roi,cv2.COLOR_BGR2HSV)
    lower_color = np.array([0,45,79],dtype=np.uint8)
    upper_color = np.array([17,255,255],dtype=np.uint8)
    mask = cv2.inRange(hsv,lower_color,upper_color)
    kernel = np.ones((3,3),dtype=np.uint8)
    mask = cv2.dilate(mask,kernel,iterations=1)
    mask = cv2.medianBlur(mask,15)
    counters,_ = cv2.findContours(mask,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
    if len(counters) > 0:
        try:
            c = findmaxcounter(counters)
            exleft = tuple(c[c[:,:,0].argmin()][0])
            exright = tuple(c[c[:,:,0].argmax()][0])
            extop = tuple(c[c[:,:,1].argmin()][0])
            


            cv2.circle(roi,exleft,5,(0,255,0),2)
            cv2.circle(roi,exright,5,(0,255,0),2)
            cv2.circle(roi,extop,5,(0,255,0),2)
            

            cv2.line(roi,(exleft,extop),(0,0,255),2)
            cv2.line(roi,(extop,exright),(0,0,255),2)
            cv2.line(roi,(exright,exleft),(0,0,255),2)
            


            a = math.sqrt(exright[0]- extop[0] **2 + exright[1] - extop[1] ** 2)
            c = math.sqrt(extop[0]- exleft[0] **2 + extop[1] - exleft[1] ** 2)
            b = math.sqrt(exright[0]- exleft[0] **2 + exright[1] - exleft[1] ** 2)
            try:
                angle = int(math.acos((a **2 + b **2 - c**2 )/(2 * b* c)) * 57)
                cv2.putText(roi,str(angle),(exright[0]-100),(exright[1]),cv2.FONT_HERSHEY_COMPLEX,1,(0,0,255),2,cv2.LINE_AA)
            except:
                cv2.putText(roi," ? ",(exright[0]-100),(exright[1]),cv2.FONT_HERSHEY_COMPLEX,1,(0,0,255),2,cv2.LINE_AA)
        except:    
            pass
    cv2.imshow("frame",frame)
    cv2.imshow("roi",roi)
    cv2.imshow("Mask",mask)
    if cv2.waitKey(20) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()    