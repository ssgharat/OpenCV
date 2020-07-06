# import cv2
# import numpy as np
#
# img = cv2.imread('robo.jpg')
#
# res = cv2.resize(img,None,fx=2, fy=2, interpolation = cv2.INTER_CUBIC)
# cv2.imshow('Image1',img)
# #OR
#
# height, width = img.shape[:2]
# res = cv2.resize(img,(2*width, 2*height), interpolation = cv2.INTER_CUBIC)
# cv2.imshow('Image2',img)

#translation
import cv2
import numpy as np

# img = cv2.imread('robo.jpg',0)
# rows,cols = img.shape
#
# M = np.float32([[1,0,100],[0,1,50]])
# dst = cv2.warpAffine(img,M,(cols,rows))
#
# cv2.imshow('img',dst)

#rotation
img = cv2.imread('robo.jpg',0)
rows,cols = img.shape

M = cv2.getRotationMatrix2D((cols/2,rows/2),90,1)       #180,270,360
dst = cv2.warpAffine(img,M,(cols,rows))
cv2.imshow('img',dst)
cv2.waitKey(0)
cv2.destroyAllWindows()