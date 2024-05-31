import cv2 as cv

file='Images/img5.jpeg'
img=cv.imread(file)
cv.imshow("Image",img)
cv.displayOverlay('Image',f'file_name={file}\n shape={img.shape}')
cv.waitKey(0)
cv.destroyAllWindows()