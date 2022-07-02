import cv2

cap = cv2.VideoCapture(0)

while True:
    ret , frame = cap.read()
    width = int(cap.get(3))  #the 3rd poperty of the cap object is the width
    height = int(cap.get(4)) #the 4th property of the cap object is the height


    #frame is the numpy array
    #ret defines the status

    img =  cv2.line( frame ,(0,0) ,(width , height) , (255 , 0 , 0) , 10)
    img = cv2.line(img, (0, height), (width, 0), (0, 255, 0), 10)
    #cv2.line( src , starting , enfing , bgr value  , thickness)

    img = cv2.rectangle(img , (100 , 100) , (200 , 200) , (128 , 128 , 128) , 5)

    #draw text
    #need to create a font first,
    font = cv2.FONT_HERSHEY_SIMPLEX
    img = cv2.putText(img , 'Ishan is great!' , (200 , height  -10) , font ,  , (0 , 0 , 0) , 5 , cv2.LINE_AA)


    cv2.imshow('frame', img)

    if cv2.waitKey(1) == ord('q'): #ordinal cnnverts ascii to alphabet
        break

cap.release()
cv2.destroyAllWindows()
