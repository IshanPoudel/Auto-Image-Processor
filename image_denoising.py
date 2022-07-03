import cv2
import numpy as np

pic = cv2.imread('assets/soccer_practice.jpeg')

dst = cv2.fastNlMeansDenoisingColored(pic, None, 10, 10, 7, 15)
cv2.imshow('' ,dst)

cv2.waitKey(0)
cv2.destroyAllWindows()