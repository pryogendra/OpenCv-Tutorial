import cv2 as cv

def mouse(event,x,y,flags,param):
    text=f'Mouse at ({x},{y}),flags={flags},param={param}'
    cv.displayOverlay('Window',text)
    if flags==1:
        img[y,x]=(0,0,255)
    cv.imshow("Window",img)
img=cv.imread('Images/img5.jpeg')
cv.imshow('Window',img)
cv.setMouseCallback('Window',mouse)

cv.waitKey(0)
cv.destroyAllWindows()