import cv2 as cv
import numpy as np

img=cv.imread('Images/img5.jpeg')
cv.imshow("Image",img)
b,g,r=cv.split(img)
img2=np.hstack([b,g,r])
cv.imshow("Split",img2)

cv.waitKey(0)
cv.destroyAllWindows()