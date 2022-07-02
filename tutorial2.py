import cv2
import random

img = cv2.imread('assets/pic.jpeg' , -1)

print(img.shape) #height width and channel ,channel is color space. Blue green and red
# [0,0,0] blue , green , red

#look at the first row

# print(img[0][45])   #first row , column 45 has b g r values of 70 , 75 , 78



# for i in range(100):
#     for j in range(img.shape[1]):
#         #gives us row , columns , channels at space 1
#         img[i][j] = [random.randint(0,255) , random.randint(0,255) , random.randint(0,255) ]



#copy one part

tag = img[500:700 , 600:900] #copy rows from 500 to 700 , column 600 to 900
img[200:400 , 650:950 ] = tag

cv2.imshow('Image' , img)
cv2.waitKey(0)
cv2.destroyAllWindows()