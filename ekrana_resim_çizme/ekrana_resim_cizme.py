import cv2
import numpy as np
from collections import deque
cap = cv2.VideoCapture(0)
lower_blue = np.array([100,60,60])
upper_blue = np.array([140,255,255])

blue_points = [deque(maxlen=512)]
green_points = [deque(maxlen=512)]
red_points = [deque(maxlen=512)]
yellow_points = [deque(maxlen=512)]

blue_index = 0
green_index = 0
red_index = 0
yellow_index = 0

colors = [(255,0,0),(0,255,0),(0,0,255),(0,255,255)]
color_index = 0
paintwindow = np.zeros((471,636,3)) + 255

paintwindow = cv2.rectangle(paintwindow,(40,1),(140,65),(0,0,0),2)
paintwindow = cv2.rectangle(paintwindow,(160,1),(255,65),colors[0],-1)
paintwindow = cv2.rectangle(paintwindow,(275,1),(375,65),colors[1],-1)
paintwindow = cv2.rectangle(paintwindow,(390,1),(485,65),colors[2],-1)
paintwindow = cv2.rectangle(paintwindow,(505,1),(600,65),colors[3],-1)
font = cv2.FONT_HERSHEY_PLAIN
cv2.putText(paintwindow,"CLEAR ALL",(49,33),font,0.5,(0,0,0),2,cv2.LINE_AA)
cv2.putText(paintwindow,"BLUE",(185,33),font,0.5,(255,255,255),2,cv2.LINE_AA)
cv2.putText(paintwindow,"GREEN",(298,33),font,0.5,(255,255,255),2,cv2.LINE_AA)
cv2.putText(paintwindow,"RED",(420,33),font,0.5,(255,255,255),2,cv2.LINE_AA)
cv2.putText(paintwindow,"YELLOW",(520,33),font,0.5,(255,255,255),2,cv2.LINE_AA)

cv2.namedWindow("Paint")


while (1):
    ret,frame = cap.read()
    frame = cv2.flip(frame,1)
    hsv = cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
    frame = cv2.rectangle(frame,(40,1),(140,65),(0,0,0),2)
    frame = cv2.rectangle(frame,(160,1),(255,65),colors[0],-1)
    frame = cv2.rectangle(frame,(275,1),(375,65),colors[1],-1)
    frame = cv2.rectangle(frame,(390,1),(485,65),colors[2],-1)
    frame = cv2.rectangle(frame,(505,1),(600,65),colors[3],-1)
    font = cv2.FONT_HERSHEY_PLAIN
    cv2.putText(paintwindow,"CLEAR ALL",(49,33),font,0.5,(0,0,0),2,cv2.LINE_AA)
    cv2.putText(paintwindow,"BLUE",(185,33),font,0.5,(255,255,255),2,cv2.LINE_AA)
    cv2.putText(paintwindow,"GREEN",(298,33),font,0.5,(255,255,255),2,cv2.LINE_AA)
    cv2.putText(paintwindow,"RED",(420,33),font,0.5,(255,255,255),2,cv2.LINE_AA)
    cv2.putText(paintwindow,"YELLOW",(520,33),font,0.5,(255,255,255),2,cv2.LINE_AA)

    if ret is False:
        break
    mask = cv2.inRange(hsv,lower_blue,upper_blue)
    mask = cv2.erode(mask,(5,5),iterations=2)
    mask = cv2.morphologyEx(mask,cv2.MORPH_OPEN,(5,5))
    mask = cv2.dilate(mask,(5,5),iterations=1)

    counters,_ = cv2.findContours(mask,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
    center = None
    if len(counters)>0:     
        max_cnt = sorted(counters,key=cv2.contourArea,reverse=True)[0]
        ((x,y),radius)= cv2.minEnclosingCircle(max_cnt)
        cv2.circle(frame,(int(x),int(y)),int(radius),(255,67,120),3)

        M = cv2.moments(max_cnt)
        center = (int(M["m10"]/M["m00"]),int(M["m01"]/M["m00"]))
        if center[1]<65:
            if 40<=center[0]<=140:
                blue_points = [deque(maxlen=512)]
                green_points = [deque(maxlen=512)]
                red_points = [deque(maxlen=512)]
                yellow_points = [deque(maxlen=512)]

                blue_index = 0
                green_index = 0
                red_index = 0
                yellow_index = 0

                paintwindow[67:,:,:] = 255
            elif 160<=center[0]<=255:
                color_index = 0
            elif 275<=center[0]<=300:
                color_index = 1    
            elif 390<=center[0]<=485:
                color_index = 2
            elif 505<=center[0]<=600:
                color_index = 3   
        else:
            if color_index == 0:
                blue_points[blue_index].appendleft(center)   
            elif color_index == 1:
                green_points[green_index].appendleft(center)  
            elif color_index == 2:
                red_points[red_index].appendleft(center)  
            elif color_index == 3:
                yellow_points[yellow_index].appendleft(center)        
    else:
        blue_points.append(deque(maxlen=512))  
        blue_index +=1   
        green_points.append(deque(maxlen=512))  
        green_index +=1   
        red_points.append(deque(maxlen=512))  
        red_index +=1   
        yellow_points.append(deque(maxlen=512))  
        yellow_index +=1      

    points = [blue_points,green_points,red_points,yellow_points]  
    for i in range(len(points)):  
        for j in range(len(points[i])):
            for k in range(len(points[i][j])):
                if  points[i][j][k-1] is None or points[i][j][k] is None:
                    continue
                cv2.line(frame,points[i][j][k-1],points[i][j][k],colors[i],2)
                cv2.line(paintwindow,points[i][j][k-1],points[i][j][k],colors[i],2)
    cv2.imshow("frame",frame)
    cv2.imshow("paintwindow",paintwindow)
    if cv2.waitKey(3) & 0xFF == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()    