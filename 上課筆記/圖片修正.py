import cv2
import numpy as np
import random

img = cv2.imread('7.png')
img = cv2.resize(img, (0, 0), fx=0.2, fy=0.2)

newImg = img[:150,:200]
newImg2 = img[:150,200:400]


# print(img)
# print(img.shape) #三個維度的大小
# print(type(img)) #資料型態

# img = np.empty((300, 300, 3), np.uint8)

# for row in range(300):
#     for col in range(img.shape[1]):
#         img[row][col] = [random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)]

cv2.imshow('img', img)
cv2.imshow('newImg', newImg)
cv2.imshow('newImg2', newImg2)


cv2.waitKey(0)