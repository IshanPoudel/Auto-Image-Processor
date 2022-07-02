import numpy as np
import cv2

img = cv2.imread('assets/pic.jpeg' , -1)
gray = cv2.cvtColor(img , cv2.COLOR_BGR2GRAY)


#corners
#use grayscale to track the corners
corners = cv2.goodFeaturesToTrack(gray , 10 , 0.2 , 50 )
# (src , no_of_corners , minimum quality , minimum euclidean distance)

# corners return foating point values.
#convert to int
corners = np.int0(corners)

for corner in corners:
    #retunrs [x , y] which gives the keys
    # place into [x , y] into x , y
     x , y = corner.ravel()

     cv2.circle(img , (x , y) , 5 , (255 , 0 , 0) , -1)


#create a line
for i in range(len(corners)):
    for j in range(i+1 , len(corners)):
        corner1 = tuple(corners[i][0])
        corner2=tuple(corners[j][0])

        # 3 rand value between 0,  255
        # get 3 rgb values , convert it into int , then convert it into a tuple
        color = tuple(map(lambda x :int(x) , np.random.randint(0,255 , size=3)))

        cv2.line(img , corner1 , corner2 , color , 1)




cv2.imshow('Frame' , img)
cv2.waitKey(0)
cv2.destroyAllWindows()

#corners look different whichever direction you move them in unlike edges
#look for regions in images which have max variation when moved by a small amount
