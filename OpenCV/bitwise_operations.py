import cv2 as cv
import numpy as np

d=15
circle=rect=np.zeros((100,100),dtype='uint8')
cv.rectangle(rect,(d,d),(100-d,100-d),255,-1)
cv.circle(circle,(50,50),40,255,-1)

bit_and=cv.bitwise_and(rect,circle)
bit_or=cv.bitwise_or(rect,circle)
bit_xor=cv.bitwise_xor(rect,circle)

img=np.hstack([rect,circle,bit_and,bit_or,bit_xor])
cv.imshow("Bitwise",img)

cv.waitKey(0)
cv.destroyAllWindows()