import cv2

#get the png values in it
bgr = cv2.imread('assets/picture_one.png')

lab = cv2.cvtColor(bgr, cv2.COLOR_BGR2LAB)

l , a , b = cv2.split(lab)

clahe = cv2.createCLAHE(clipLimit=2.0,tileGridSize=(8,8))

l = clahe.apply(l)

lab = cv2.merge((l,a,b))

bgr = cv2.cvtColor(lab, cv2.COLOR_LAB2BGR)

cv2.imshow('Match' , bgr)
cv2.waitKey(0)
cv2.destroyAllWindows()