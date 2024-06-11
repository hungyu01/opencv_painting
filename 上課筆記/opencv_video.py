import cv2

mp4 = cv2.VideoCapture('opencv.mp4')
#mp4 = cv2.VideoCapture(1) #預設攝影鏡頭

while True:
    ret, frame = mp4.read()
    frame = cv2.resize(frame, (0, 0), fx=0.5, fy=0.5)
    if ret:    
        cv2.imshow('video', frame)
    else:
        break

    if cv2.waitKey(10) == ord('q'):
        break