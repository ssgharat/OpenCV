import cv2
cap = cv2.VideoCapture(0) # use the camera of the computer
width= int(cap.get(cv2.CAP_PROP_FRAME_WIDTH)) #get the width and height of the frame
height= int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT)) #get the width and height of the frame
output=cv2.VideoWriter('myvideo.mkv',cv2.VideoWriter_fourcc(*'DIVX'),20,(width,height))

while True:
    ret,frame= cap.read()

    #operations
    output.write(frame)

    #if you want grey frame
    #grey =cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    #cv2.imshow('frame,grey)
    cv2.imshow('frame',frame)

    if cv2.waitKey(5) & 0xFF == 27:
        break

cap.release()
output.release()
cv2.destroyAllWindows()