import cv2 as cv
import numpy as np

def trackbar(x):
    ret,img1=cv.threshold(img,x,255,cv.THRESH_BINARY)
    ret,img2=cv.threshold(img,x,255,cv.THRESH_BINARY_INV)
    cv.imshow('Window',np.hstack([img,img1,img2]))
    text=f'threshold={x},mode=Binary,Bimary_inv'
    cv.displayOverlay('Window',text,1000)

img=cv.imread('Images/img3.jpeg')
trackbar(100)
cv.createTrackbar('thresold','Window',100,255,trackbar)

cv.waitKey(0)
cv.destroyAllWindows()