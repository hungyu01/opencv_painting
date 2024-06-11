import cv2

img = cv2.imread('cat_test.png')
img = cv2.resize(img, (0, 0), fx=0.5, fy=0.5)
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
faceCascade = cv2.CascadeClassifier('face_detect.xml')
faceRect = faceCascade.detectMultiScale(gray, 1.1, 3)  #轉灰階、縮小倍率、偵測次數
print(len(faceRect))

for (x, y, w, h) in faceRect:   #人臉用綠框框標註
    cv2.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0),2)

cv2.imshow('img', img)
cv2.waitKey(0)