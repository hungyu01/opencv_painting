import cv2
import numpy as np

kernel = np.ones((7, 7), np.uint8)
kernel1 = np.ones((7, 7), np.uint8)

img = cv2.imread('7.png')
img = cv2.resize(img, (0, 0), fx=0.2, fy=0.2)

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) #灰階
blur = cv2.GaussianBlur(img, (7, 7), 0)      #模糊

canny = cv2.Canny(img, 150, 200)             #邊緣偵測
dilate = cv2.dilate(canny, kernel, iterations=1) #邊緣膨脹(iterations=膨脹次數)
erode = cv2.erode(dilate, kernel1, iterations=2) #邊緣侵蝕

# cv2.imshow('img', img)
# cv2.imshow('gray', gray)
# cv2.imshow('blur', blur)
cv2.imshow('canny', canny)
cv2.imshow('dilate', dilate)
cv2.imshow('erode', erode)


cv2.waitKey(0)