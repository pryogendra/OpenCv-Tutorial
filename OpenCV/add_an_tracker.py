import cv2 as cv

def trackbar(x):
    text=f'Trackbar:{x}'
    cv.displayOverlay('window',text,1000) # display overlay
    cv.imshow('window',img)
img=cv.imread('Images/img3.jpeg')
cv.imshow('window',img)
cv.createTrackbar('x','window',100,255,trackbar) # creating trackbar
cv.waitKey(0)
cv.destroyAllWindows()