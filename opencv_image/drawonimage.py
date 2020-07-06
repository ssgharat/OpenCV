import numpy as np
import matplotlib.pyplot as plt
import cv2

#matplotlib inline
black_img=np.zeros((512,512,3))
shape=black_img.shape
#cv2.imshow('black',black_img)

#circle
cv2.circle(img=black_img,center=(400,100),radius=50,color=(255,0,0),thickness=8)
#cv2.imshow('black_cir',black_img)

#filled circle
cv2.circle(img=black_img,center=(50,100),radius=25,color=(255,0,0),thickness=-1)
#cv2.imshow('black_cir',black_img)

#rectangle
cv2.rectangle(img=black_img,pt1=(200,200),pt2=(300,300),color=(255,200,100),thickness=5)
#cv2.imshow('black_rec',black_img)

#filled rectangle
cv2.rectangle(img=black_img,pt1=(100,100),pt2=(200,200),color=(0,50,100),thickness=-1)
#cv2.imshow('black_rec',black_img)

#triangle
vertices=np.array([[10,450],[110,350],[180,450]],np.int32)
pts=vertices.reshape(-1,1,2)
cv2.polylines(black_img,[pts],isClosed=True,color=(0,0,255),thickness=3)
#cv2.imshow("triang",black_img)

#filled triangle
vertices_filled=np.array([[500,450],[300,350],[150,350]],np.int32)
pts_filled=vertices_filled.reshape(-1,1,2)
cv2.fillPoly(black_img,[pts_filled],color=(50,0,155))
#cv2.imshow("triang",black_img)

#drawline
cv2.line(img=black_img,pt1=(150,100),pt2=(500,200),color=(255,255,100),thickness=1)
#cv2.imshow("line",black_img)

#font
font=cv2.FONT_HERSHEY_SIMPLEX
cv2.putText(black_img,text='RHYME',org=(210,500),fontFace=font,fontScale=3,color=(255,255,0),thickness=3,lineType=cv2.LINE_AA)
cv2.imshow("text",black_img)
cv2.waitKey(0)
cv2.destroyAllWindows()