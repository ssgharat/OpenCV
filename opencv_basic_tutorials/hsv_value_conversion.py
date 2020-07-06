import cv2
import numpy as np

red = np.uint8([[[255,0,0 ]]])
hsv_red = cv2.cvtColor(red,cv2.COLOR_BGR2HSV)
print (hsv_red)

green = np.uint8([[[0,255,0 ]]])
hsv_green = cv2.cvtColor(green,cv2.COLOR_BGR2HSV)
print (hsv_green)

blue = np.uint8([[[0,0,255 ]]])
hsv_blue  = cv2.cvtColor(blue ,cv2.COLOR_BGR2HSV)
print (hsv_blue )
#Now you take [H-10, 100,100] and [H+10, 255, 255] as lower bound and upper bound respectively.