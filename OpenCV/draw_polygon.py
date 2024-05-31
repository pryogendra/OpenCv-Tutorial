import cv2 as cv
import numpy as np

pts=[(20,20),(20,200),(200,100)]
GREEN=(0,255,0)

img=np.zeros((300,500,3),np.uint8)
cv.polylines(img,np.array([pts]),True,color=GREEN,thickness=2) #Drawing plygon
#cv.fillPoly(img,np.array([pts]),color=GREEN) #Fill Polygon
cv.imshow("Polygon",img)

cv.waitKey(0)
cv.destroyAllWindows()