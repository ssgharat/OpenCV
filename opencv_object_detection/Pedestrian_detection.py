import cv2
import numpy as np
import matplotlib.pyplot as plt
#matplotlib inline

body_cascade=cv2.CascadeClassifier('haarcascade_fullbody.xml')
cap=cv2.VideoCapture('people_walking2.mp4')


while True:
    ret, frame = cap.read()

    body_rectangle= body_cascade.detectMultiScale(frame)
    if ret==True:
        for(x,y,w,h) in body_rectangle:
            cv2.rectangle(frame,(x,y),(x+w,y+h),(255,255,255),10)


    cv2.imshow('Pedestrians',frame)
    if cv2.waitKey(3) & 0xFF == 27:
        break

cap.release()
cv2.destroyAllWindows()
