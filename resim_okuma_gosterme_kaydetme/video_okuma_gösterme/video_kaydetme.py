import cv2
cap = cv2.VideoCapture(0)
filename = "C:\Users\aliha\OneDrive\Masaüstü\opencv\webcam_saving.avi"
codec = cv2.VideoWriter_fourcc('w','M','V','2')
framerate = 30
resolution = (640, 480)
videofileoutpute = cv2.VideoWriter(filename,codec,framerate,resolution)
while True:
    ret, frame = cap.read()
    frame = cv2.flip(frame,1)
    videofileoutpute.write(frame)
    cv2.imshow("webcam",frame)
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break
videofileoutpute.release()    
cap.release()
cv2.destroyAllWindows()    