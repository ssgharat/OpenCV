import cv2
import numpy as np
import matplotlib.pyplot as plt
#matplotlib inline

eye_cascade=cv2.CascadeClassifier('haarcascade_eye.xml')
face_cascade=cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
image=cv2.imread('eye_face2.jpg')
#cv2.imshow('image',image)

width_ratio=0.5
height_ratio=0.5

img2=cv2.resize(image,(0,0),image,width_ratio,height_ratio)
cv2.imshow('small',img2)

# eye_rectangle= eye_Cascade.detectMultiScale(img2,1.5,5)
# # if eye_rectangle is():
# #     print('no faces found')
def detect_face(img2):
    face_rectangle = face_cascade.detectMultiScale(img2)

    for(x,y,w,h) in face_rectangle:
        cv2.rectangle(img2,(x,y),(x+w,y+h),(50,25,25),10)

    return img2
result=detect_face(img2)
cv2.imshow("face detection",img2)
def detect_eye(img2):
    eye_rectangle =eye_cascade.detectMultiScale(img2)

    for(x,y,w,h) in eye_rectangle:
        cv2.rectangle(img2,(x,y),(x+w,y+h),(50,25,25),1)

    return img2
result=detect_eye(img2)
cv2.imshow("eye detection",img2)
cv2.waitKey(0)
cv2.destroyAllWindows()