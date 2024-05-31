import cv2 as cv
import numpy as np

def rgb(x):
    r=cv.getTrackbarPos('Red','Window')
    g=cv.getTrackbarPos('Green','Window')
    b=cv.getTrackbarPos('Blue','Window')
    img[:]=[r,g,b]
    cv.displayOverlay('Window',f'Red={r}\nGreen={g}\nBlue={b}')
    cv.imshow('Window',img)
img=np.zeros((200,600,3),'uint8')
cv.imshow("Window",img)
cv.createTrackbar("Red",'Window',200,255,rgb)
cv.createTrackbar("Green",'Window',50,255,rgb)
cv.createTrackbar("Blue",'Window',100,255,rgb)
rgb(0)

cv.waitKey(0)
cv.destroyAllWindows()
