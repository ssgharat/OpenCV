import numpy as np
import matplotlib.pyplot as plt
import cv2

#matplotlib inline

#from PIL import Image
img=cv2.imread('robo.jpg')
cv2.imshow('Image',img)
type(img)
shape=img.shape
print(shape)
#img_fix=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
#img_gray=cv2.imread('A_mountain.jpg')
#img_gray.shape
red=img.copy()
red[:,:,0]=0
red[:,:,1]=0
cv2.imshow('Image_r',red)

blue=img.copy()
blue[:,:,1]=0
blue[:,:,2]=0
cv2.imshow('Image_b',blue)

green=img.copy()
green[:,:,0]=0
green[:,:,2]=0
cv2.imshow('Image_g',green)

width_ratio=0.5
height_ratio=0.5

img2=cv2.resize(img,(0,0),img,width_ratio,height_ratio)
cv2.imshow('small',img2)
shape_img2=img2.shape


#flip on horizontal
img3=cv2.flip(img2,0)
cv2.imshow('hor_flip',img3)

#flip on vertical
img3=cv2.flip(img2,1)
cv2.imshow('ver_flip',img3)


#cv2.imshow('image',img)
cv2.waitKey(0)
cv2.destroyAllWindows()