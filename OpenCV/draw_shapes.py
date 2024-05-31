import cv2 as cv
import numpy as np

#blank Page
blank=np.zeros((500,500,3),dtype='uint8')
#cv.imshow("Blank",blank)

#fill with a color
#blank[:]=0,0,255 #Fill with red color
#cv.imshow("Red",blank)

#fill in range
#blank[100:300]=0,255,0  #Fill with green color in range
#cv.imshow("Green",blank)

#draw a reactangle
#cv.rectangle(blank,(100,500),(300,200),(0,255,0),thickness=3,)
#cv.imshow("Rectangle",blank)

#Draw a circle
#cv.circle(blank,(200,200),90,(255,0,0),thickness=-1) #solid fill with blue color
#cv.circle(blank,(200,200),90,(255,0,0),thickness=cv.FILLED) #Solid fill
#cv.imshow("Circle",blank)

#draw a line
#cv.line(blank,(100,30),(200,200),(255,0,0),thickness=4)
#cv.imshow("Line",blank)

#Write a text on img
cv.putText(blank,"Hello World",(100,100),cv.FONT_HERSHEY_TRIPLEX,1,(255,0,0),thickness=2)
cv.imshow("Text",blank)

cv.waitKey(0)