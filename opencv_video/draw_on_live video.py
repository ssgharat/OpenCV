#import libraries
import cv2
#take a video , or '0' means use computer camera
cap= cv2.VideoCapture('myvideo.mkv')

#get the width and height of the video frame
width= int(cap.get(cv2.CAP_PROP_FRAME_WIDTH)) #get the width and height of the frame
height= int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT)) #get the width and height of the frame

#top left corner
# we divide with // the width and height of the frame
#in order to get an integer as a result
x=width//2
y=height//2

#rectangle width and height
#1/4 of the actual video screen
w=width//4
h=height//4
#bottom right corner== x+w, y+h

while True:
    ret,frame=cap.read()
    #rectangle formula
    cv2.rectangle(frame,(x,y),(x+w,y+h),color=(100,0,255),thickness=5)

    #show it
    #if ret==True:
    cv2.imshow('frame',frame)

    if cv2.waitKey(3) & 0xFF==27:
        break

cap.release()
cv2.destroyAllWindows()