import cv2 as cv
import numpy as np

kernel=np.ones((5,5),'float32')/25

def trackbar(x):
    d=2*x+1
    kernel=np.ones((d,d),'float32')/(d**2)
    img1=cv.filter2D(img,-1,kernel)
    cv.imshow('Window',np.hstack([img,img1]))
    text=f'kernel=({d}x{d})'
    cv.displayOverlay('Window',text)

img=cv.imread('Images/img5.jpeg')
trackbar(2)
cv.createTrackbar('thresold','Window',2,7,trackbar)

cv.waitKey(0)
cv.destroyAllWindows()