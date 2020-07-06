import cv2
import numpy as np
import matplotlib.pyplot as plt
#matplotlib inline

car_cascade=cv2.CascadeClassifier('haarcascade_russian_plate_number.xml')
cap=cv2.VideoCapture('vehicle3.mp4')


while True:
    ret, frame = cap.read()

    car_rectangle= car_cascade.detectMultiScale(frame,1.3,2)
    if ret==True:
        for(x,y,w,h) in car_rectangle:
            cv2.rectangle(frame,(x,y),(x+w,y+h),(255,255,255),10)


    cv2.imshow('vehicles',frame)
    if cv2.waitKey(3) & 0xFF == 27:
        break

cap.release()
cv2.destroyAllWindows()
