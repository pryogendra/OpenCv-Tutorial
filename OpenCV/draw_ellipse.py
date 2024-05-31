import cv2 as cv
import numpy as np

RED=(0,0,255)
img=np.zeros((300,500,3),np.uint8)
cv.ellipse(img,(200,200),(100,20),90,0,360,RED,3)
cv.imshow("Ellipse",img)

cv.waitKey(0)
cv.destroyAllWindows()