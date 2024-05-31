import cv2 as cv

def mouse(event,x,y,flags,param):
    text=f'Mouse ar ({x},{y}),flags={flags},param={param}'
    cv.displayOverlay("Mouse",text)
img=cv.imread('Images/img3.jpeg')
cv.imshow('Mouse',img)
cv.setMouseCallback('Mouse',mouse)

cv.waitKey(0)
cv.destroyAllWindows()