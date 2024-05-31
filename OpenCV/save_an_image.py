import cv2 as cv

img=cv.imread('Images/img6.jpeg')
cv.imwrite('Images/temp.png', img) #saving image

cv.waitKey(0)
cv.destroyAllWindows()