import cv2 as cv
cap = cv.VideoCapture(0)  # 0 used for live capture of the device camera

while True:
    ret,frame = cap.read()  # reading the videos
    cv.imshow('Live' , frame)

    if cv.waitKey(1) & 0xFF == ord('q'):
        break
cap.release()
cv.destroyAllWindows()