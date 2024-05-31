import cv2 as cv
import numpy as np

RED=(0,0,255)
po,p1=(100,30),(400,90)

def tracebar(x):
    x=max(1,x)
    cv.displayOverlay('Window',f'Thickness={x}')
    img[:]=0 #Clear the image
    cv.line(img,po,p1,RED,x) #draw a line
    cv.imshow("Window",img)

img=np.zeros((300,500,3),np.uint8)
cv.line(img,po,p1,RED,2) #drawing a line
cv.imshow("Window",img)
cv.createTrackbar('Thickness','Window',2,20,tracebar)

cv.waitKey(0)
cv.destroyAllWindows()
