import cv2

img=cv2.imread('robo.jpg')
cv2.imshow('original Image',img)
# width_ratio=0.5
# height_ratio=0.5
img2=cv2.cvtColor(img,cv2.COLOR_BGR2HSV_FULL)
cv2.imshow('Image',img2)

cv2.waitKey(0)
cv2.destroyAllWindows()