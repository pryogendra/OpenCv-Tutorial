from matplotlib import pyplot as plt
import cv2 as cv

img=cv.imread('Images/img6.jpeg')
#cv.imshow('Window',img)
grey=cv.cvtColor(img,cv.COLOR_BGR2GRAY)
hist=cv.calcHist([grey],[0],None,[256],[0,256])
plt.figure()
plt.title('Gray Scale Histogram')
plt.xlabel('Bins')
plt.ylabel('# of pixels')
plt.plot(hist)
plt.xlim([0,256])
plt.ylim([0,2000])
plt.show()

cv.waitKey(0)
