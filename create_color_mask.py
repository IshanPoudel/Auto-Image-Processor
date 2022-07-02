#extract color from an image

import numpy as np
import cv2

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    width = int(cap.get(3))  # the 3rd poperty of the cap object is the width
    height = int(cap.get(4))

    hsv = cv2.cvtColor(frame , cv2.COLOR_BGR2HSV)

    lower_blue = np.array([110,50,50])
    upper_blue =np.array([130,255,255])

    #create a mask

    mask = cv2.inRange(hsv , lower_blue , upper_blue)  #any pictures in that range of blue are passed in

    result = cv2.bitwise_and(frame , frame , mask=mask)
    #bitwise_ands frame and mask , and stores in frame. We only get similar values


    cv2.imshow('frame', result)

    if cv2.waitKey(1) == ord('q'):  # ordinal cnnverts ascii to alphabet
        break

cap.release()
cv2.destroyAllWindows()


#convert bgr to hac

# BGR_color = np.array([[[255 , 0 , 0]]]) 1 row , 1 coliumn 1 pixel blue color