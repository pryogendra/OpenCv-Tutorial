import cv2 as cv

def rotate(img,angle,rotPoint=None):
    (height,width)=img.shape[:2]
    if rotPoint is None:
        rotPoint=(width//2,height//2)
    rotMat=cv.getRotationMatrix2D(rotPoint,angle,1)
    dimentions=(width,height)
    return cv.warpAffine(img,rotMat,dimentions)

img=cv.imread('Images/img5.jpeg')
cv.imshow("Image",img)
rotated=rotate(img,45)
cv.imshow("Rotated",rotated)

cv.waitKey(0)
cv.destroyAllWindows()