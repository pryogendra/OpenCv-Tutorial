import cv2 as cv
import numpy as np

#img=cv.imread('Images/img3.jpeg',cv.IMREAD_GRAYSCALE)
img=cv.imread('/home/kali/Desktop/divya.jpeg',cv.IMREAD_GRAYSCALE)
img1=cv.Canny(img,100,70)
cv.imshow('Canny',np.hstack([img,img1]))

cv.waitKey(0)
cv.destroyAllWindows()