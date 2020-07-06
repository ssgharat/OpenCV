#import libraries
import cv2
import numpy as np

img=cv2.imread('robo.jpg')

#function
#x,y,flags,param are fed from opencv automatically
def draw_circle(event,x,y,flags,param):
    if event==cv2.EVENT_LBUTTONDOWN:
        cv2.circle(img,(x,y),70,(35,69,78),-1)

#connect the function with the callback
cv2.namedWindow(winname='my_drawing')

#callback
cv2.setMouseCallback('my_drawing',draw_circle)

#using opencv to show image
img=np.zeros((512,512,3),np.int8)

while True:
    cv2.imshow('my_drawing',img)

    if cv2.waitKey(15) & 0xFF == 27:
        break

cv2.waitKey(0)
cv2.destroyAllWindows()