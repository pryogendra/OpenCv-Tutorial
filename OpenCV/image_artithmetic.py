import cv2 as cv
import numpy as np

img=cv.imread("Images/img4.jpeg")
#cv.resize(img,dsize=None,fx=0.5,fy=0.5,interpolation=cv.INTER_CUBIC)
M=np.ones(img.shape,dtype='uint8')

brighter=cv.add(img,M)
darker=cv.subtract(img,M)

img2=np.hstack([img,brighter,darker])
cv.imshow("Image",img2)

cv.waitKey(0)
cv.destroyAllWindows()