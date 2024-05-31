import cv2 as cv
import numpy as np

img=np.zeros((300,500,3),np.uint8)
cv.putText(img,'OpenCV',(10,150),fontFace=cv.FONT_HERSHEY_TRIPLEX,fontScale=4,color=(0,255,0),thickness=3,lineType=cv.LINE_AA)
cv.imshow("Window",img)

cv.waitKey(0)
cv.destroyAllWindows()