import cv2 as cv

#reading image
img=cv.imread("Images/img5.jpeg")
#img=cv.imread("Images/img5.jpeg",cv.IMREAD_COLOR)
cv.imshow('Image',img)

#Converting to greyscale
grey=cv.cvtColor(img,cv.COLOR_BGR2GRAY)
#cv.imshow("Grey",grey)

#Blur
blur=cv.blur(img,(7,7),cv.BORDER_DEFAULT)
#cv.imshow("Blur",blur)

#Edge Cascade
canny=cv.Canny(img,90,90) #paramenete are cascading ranges
#cv.imshow("Canny",canny)

#Eroding the image
erode=cv.erode(img,(3,3),iterations=20)
#cv.imshow("Erode",erode)

#Resize Image
resized=cv.resize(img,(500,400))
#cv.imshow("resized",resized)

#Cropping Image
cropped=img[50:200,10:200]
#cv.imshow("Cropped",cropped)

#Flipping/Mirroring a Image
flip=cv.flip(img,0)  # 0->Vertical  1->Horizontal  -1->both axis
cv.imshow("Flipped",flip)

cv.waitKey(0)
cv.destroyAllWindows()