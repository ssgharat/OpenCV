#import libraries
import cv2

#callback function for the mouse,rectangle
def draw_rectangle(event,x,y,flags,param):
    #write your global params.
    global pt1,pt2,top_left_clicked,bottom_right_clicked

    #create an event for left button down and assign it to event
    if event==cv2.EVENT_LBUTTONDOWN:
        #reset your rectangle
        if top_left_clicked==True and bottom_right_clicked==True:
            pt1=(0,0)
            pt2=(0,0)
        #give false values to your trackers
        top_left_clicked=False
        bottom_right_clicked=False
    #check the top left click if it is false
        if top_left_clicked==False:
            pt1=(x,y)
        top_left_clicked=True
    #check the bottom right click if it is false
        if bottom_right_clicked==False:
            pt1=(x,y)
        bottom_right_clicked=True

#pt1,pt2 Global variables
pt1=(0,0)
pt2=(0,0)

#trackers are false
top_left_clicked=False
bottom_right_clicked=False

#take a video
cap=cv2.VideoCapture(0)

#create a named window for tge connections
cv2.namedWindow('Test')

#set a mouse callback
cv2.setMouseCallback('Test',draw_rectangle)

while True:
    #capture the frame
    ret,frame=cap.read()

    #based on the global variable draw the frame
    if top_left_clicked==True:
        cv2.circle(frame,center=pt1,radius=5,color=(255,0,255),thickness=-1)
    #draw a rectangle on the frame
    if top_left_clicked==True and bottom_right_clicked== True:
        cv2.rectangle(frame,
                      pt1,
                      pt2, color=(255, 0, 255), thickness=-1)
    #show the frame
    cv2.imshow('frame',frame)

    if cv2.waitKey(3)& 0xFF==27:
        break

cap.release()
cv2.destroyAllWindows()


