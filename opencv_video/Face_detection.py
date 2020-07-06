import cv2
import numpy as np
import matplotlib.pyplot as plt
#matplotlib inline

face_cascade=cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
#face_cascade=cv2.CascadeClassifier('haarcascade_smile.xml')
#cap=cv2.VideoCapture('myvideo.mkv')
cap=cv2.VideoCapture(0)  #computer camera

while True:
    ret, frame = cap.read()

    face_rectangle= face_cascade.detectMultiScale(frame)  #,200 for smile 

    for(x,y,w,h) in face_rectangle:
        cv2.rectangle(frame,(x,y),(x+w,y+h),(75,150,200),10)


    cv2.imshow('frame',frame)
    if cv2.waitKey(3) & 0xFF == 27:
        break

cap.release()
cv2.destroyAllWindows()
