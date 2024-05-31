import cv2 as cv
import numpy as np

RED=(0,0,255)
pts=[]

def draw (event, x, y, flags, param):
    global img0
    if event==cv.EVENT_LBUTTONUP:
        cv.polylines(img,np.array([pts]),0,RED,3)
        cv.imshow('Window',img)

    elif event==cv.EVENT_LBUTTONDOWN:
        pts.append((x,y))

img=np.zeros((300,500,3),np.uint8)
cv.imshow("Window",img)
#img0[:]=img
cv.setMouseCallback("Window",draw)

cv.waitKey(0)
cv.destroyAllWindows()
