import cv2 as cv
video=cv.VideoCapture('Videos/video.mp4')
while True:
    isTrue,frame=video.read()
    cv.imshow('Video',frame)

    if cv.waitKey(20) & 0xFF==ord('d'):
        break
video.release()
cv.destroyAllWindows()