#load images  , track images .
import cv2


img = cv2.imread('assets/pic.jpeg' , 0 )
img = cv2.resize (img , (0 , 0) , fx=0.5 , fy = 0.5)
img = cv2.rotate(img , cv2.ROTATE_90_CLOCKWISE)

cv2.imwrite('new_pic.jpg' , img)
#by default loads into blue green red ,
#we can load it in greyscale , original , or transparenct

# cv2.IMREAD_COLOR
# CV2.IMREAD_GRAYSCALE


cv2.imshow('Image' , img)
cv2.waitKey(0)
cv2.destroyAllWindows()
