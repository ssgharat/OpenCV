#import libraries
import cv2

#callback function for the mouse,Circle
def draw_circle(event,x,y,flags,param):
    global center,clicked
    #get the muse click down and up
    #and track the center
    if event == cv2.EVENT_LBUTTONDOWN:
        center=(x,y)
        clicked=False

    if event==cv2.EVENT_LBUTTONDOWN:
         clicked=True

#zero drawing of the circle
center=(0,0)
clicked=False

#take a video
cap=cv2.VideoCapture(0)

#create a Named Window for the Connections
cv2.namedWindow('Testing')

#bind our function with the Mouse clicks
cv2.setMouseCallback('Testing',draw_circle)

while True:
    #capture the frame
    ret,frame=cap.read()

    #check if clicked is True
    if clicked:
        cv2.circle(frame, center=center, radius=50, color=(255, 0, 255), thickness=-3)

    #display the frame
    cv2.imshow('Testing',frame)
    if cv2.waitKey(3)& 0xFF==27:
        break

cap.release()
cv2.destroyAllWindows()
