import cv2 as cv
video=cv.VideoCapture('Videos/video.mp4')
def resize_frame(frame,scale=0.75):
    width=int(frame.shape[1]*scale)
    height=int(frame.shape[0]*scale)

    dimentions=(width,height)
    return cv.resize(frame,dimentions,interpolation=cv.INTER_AREA)

while True:
    isTrue,frame=video.read()
    resized_video=resize_frame(frame,scale=0.2)
    cv.imshow('Resized Video',resized_video)

    if cv.waitKey(20) & 0xFF==ord('d'):
        break
video.release()
cv.destroyAllWindows()