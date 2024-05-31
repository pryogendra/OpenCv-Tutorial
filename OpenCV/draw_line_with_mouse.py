import cv2 as cv
import numpy as np

BLUE=(255,0,0)
p0,p1=(100,20),(400,90)
def drawLine(event,x,y,flags,param):
    global p0,p1
    if event==cv.EVENT_LBUTTONDOWN:
        p0=p1=(x,y)
    elif event==cv.EVENT_MOUSEMOVE and flags==1:
        p1=(x,y)
    elif event==cv.EVENT_LBUTTONUP:
        p1=(x,y)
    img[:]=0
    cv.line(img,p0,p1,BLUE,3)
    cv.imshow("Window",img)
    cv.displayOverlay('Window',f'(p0={p0},p1={p1}')

img=np.zeros((200,500,3),np.uint8)
cv.line(img,p0,p1,BLUE,3)
cv.imshow("Window",img)
cv.setMouseCallback('Window',drawLine)

cv.waitKey(0)
cv.destroyAllWindows()