import cv2 as cv
import numpy as np

def translate(img,x,y):
    transMat=np.float32([[1,0,x],[0,1,y]])
    dimentions=(img.shape[1],img.shape[0])
    return cv.warpAffine(img,transMat,dimentions)

img=cv.imread('Images/img5.jpeg')
cv.imshow("Image",img)
translated=translate(img,10,100)
cv.imshow("Translated",translated)

cv.waitKey(0)
cv.destroyAllWindows()