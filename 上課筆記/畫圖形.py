import cv2
import numpy as np

img = np.zeros((600, 600, 3), np.uint8)
cv2.line(img, (0, 0), (400, 300), (255, 0, 0), 2) #畫線 (檔案名, 起始座標, 終點座標, 顏色, 粗細)
cv2.line(img, (0, 0), (img.shape[1], img.shape[0]), (255, 0, 0), 2) #畫線 (從起始點到最右下角)
cv2.rectangle(img, (0, 0),(400, 300), (0, 0, 255), 2)   #畫方形 (粗度 cv2.FILLED = 填滿)
cv2.circle(img, (400,200), 100 , (255, 0, 0), cv2.FILLED)   #畫圓形
cv2.putText(img, 'hello world', (100, 500), cv2.FONT_HERSHEY_COMPLEX, 1, (70, 70, 70), 1) #顯示文字

cv2.imshow('img', img)

cv2.waitKey(0)