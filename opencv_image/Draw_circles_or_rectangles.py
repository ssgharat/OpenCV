#import libraries
import cv2
import numpy as np



#function
#x,y,flags,param are fed from opencv automatically
def draw_circle(event,x,y,flags,param):
    if event==cv2.EVENT_LBUTTONDOWN:
        cv2.circle(img,(x,y),70,(35,69,78),-1)
    elif event == cv2.EVENT_RBUTTONDOWN:
        cv2.circle(img, (x, y),20,color=(255, 255, 255), thickness=-1)

drawing=False
ex=-1
ey=-1

# def drawing_rectangle(event,x,y,flags,param):
#
#     global ex,ey,drawing
#     if event==cv2.EVENT_LBUTTONDOWN:
#         drawing=True
#         ex,ey=x,y
#     elif event==cv2.EVENT_MOUSEMOVE:
#         if drawing==True:
#             cv2.rectangle(img, (ex, ey),(x,y),color=(255, 0, 255), thickness=-1)
#
#     elif event == cv2.EVENT_LBUTTONUP:
#         drawing=False
#         cv2.rectangle(img, (ex, ey),(x,y),color=(255, 0, 255), thickness=-1)

#connect the function with the callback
cv2.namedWindow(winname='my_drawing')
#cv2.namedWindow(winname='my_drawing2')

#callback
cv2.setMouseCallback('my_drawing',draw_circle)
#cv2.setMouseCallback('my_drawing2',drawing_rectangle)

#using opencv to show image
img=np.zeros((512,512,3),np.int8)

while True:
    cv2.imshow('my_drawing',img)
    #cv2.imshow('my_drawing2', img)

    if cv2.waitKey(15) & 0xFF == 27:
        break

cv2.waitKey(0)
cv2.destroyAllWindows()