import cv2

img = cv2.imread('7.png')

img = cv2.resize(img, (0, 0), fx=0.2, fy=0.2)
cv2.imshow('frame', img)

cv2.waitKey(0) #每多少毫秒