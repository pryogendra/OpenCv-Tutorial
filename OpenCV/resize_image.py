import cv2 as cv
def resize_frame(frame,scale=0.75):
    width=int(frame.shape[1]*scale)
    height=int(frame.shape[0]*scale)

    dimentions=(width,height)
    return cv.resize(frame,dimentions,interpolation=cv.INTER_AREA)

img=cv.imread('Images/img2.jpeg')
resized_img=resize_frame(img,0.1)
cv.imshow('Resized Image',resized_img)

cv.waitKey(0)