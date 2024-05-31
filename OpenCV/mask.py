import cv2 as cv
import numpy as np

img=cv.imread("Images/img5.jpeg")

mask=np.zeros(img.shape[:2],dtype='uint8')
cv.circle(mask,(300,100),50,255,-1)
masked=cv.bitwise_and(img,img,mask=mask)
#cv.imshow("null",masked)
img2=np.hstack([img,masked])
cv.imshow("Masked",img2)

cv.waitKey(0)
cv.destroyAllWindows()