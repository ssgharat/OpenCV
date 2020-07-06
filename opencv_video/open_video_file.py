import cv2

#open the video recorded earlier
cap=cv2.VideoCapture('myvideo.mkv')

#in case we write wrong path
if cap.isOpened()==False:
    print('Error! Check your file path')


while cap.isOpened():
    ret, frame = cap.read()

    if ret==True:
        cv2.imshow('frame', frame)

        if cv2.waitKey(15) & 0xFF == 27:
            break

cap.release()
cv2.destroyAllWindows()
