import numpy as np
import cv2

img = cv2.resize(cv2.imread('assets/soccer_practice.jpeg', 0), (0, 0), fx=0.8, fy=0.8)
template = cv2.resize(cv2.imread('assets/ball.png', 0), (0, 0), fx=0.8, fy=0.8)



h , w = template.shape #only two for grayscale image


#different temlate matching

methods = [cv2.TM_CCOEFF, cv2.TM_CCOEFF_NORMED, cv2.TM_CCORR,
            cv2.TM_CCORR_NORMED, cv2.TM_SQDIFF, cv2.TM_SQDIFF_NORMED]

for method in methods:
    img2 = img.copy()

    result = cv2.matchTemplate(img2, template, method)

    min_val , max_val , min_loc , max_loc = cv2.minMaxLoc(result)

    if method in [cv2.TM_SQDIFF, cv2.TM_SQDIFF_NORMED]:
        location = min_loc
    else:
        location = max_loc

    bottom_right = (location[0] + w , location[1] + h)
    cv2.rectangle(img2, location, bottom_right, 255, 5)
    cv2.imshow('Match' , img2)
    cv2.waitKey(0)
    cv2.destroyAllWindows()





    # scans through the array and returns a result giving how likely it is to perform a case
    # (W - w+1 , H-h+1)
    # W-base image
    # w-template image

# [[255 , 255 , 255 , 255] ,
#  [255 , 255 , 255 , 255] ,
#  [255 , 255 , 255 , 255] ,
#  [255 , 255 , 255 , 255]
#  ]
#
# [[255 , 255],
#  [255 , 255]]

# and the result would be a 3 * 3 array
# [[0,0,0] ,
#  [0,1,0],
#  [0,0,0]]
# find the positions with 1 and find reverser engineer where it is in the original array and draw a template around it




