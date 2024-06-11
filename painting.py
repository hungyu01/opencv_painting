import cv2
import numpy as np
cap = cv2.VideoCapture(0) #預設攝影鏡頭

penColorHSV = [[0, 134, 97, 179, 209, 255],     #藍筆HSV
               [124, 179, 150, 255, 54, 255]]   #紅筆HSV

#找到畫筆顏色
def findPen(img):
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)  #將顏色的 BGR 轉換成 HSV

    for i in range(len(penColorHSV)):
        lower = np.array(penColorHSV[i][:3])
        upper = np.array(penColorHSV[i][3:6])

        mask = cv2.inRange(hsv, lower, upper)
        result = cv2.bitwise_and(img, img, mask=mask)
        penx, peny = findContour(mask)
        cv2.circle(imgContour,(penx, peny),10, (255,0,0), cv2.FILLED)
    # cv2.imshow('result', result)

#找到畫筆輪廓
def findContour(img):
    contours, hierarchy = cv2.findContours(img, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
    x, y, w, h=-1, -1, -1, -1
    for cnt in contours:
        # cv2.drawContours(imgContour, cnt, -1, (255,0,0), 4) #顯示出輪廓
        area = cv2.contourArea(cnt)     #過濾面積
        if area > 500:
            peri = cv2.arcLength(cnt, True)
            vertices = cv2.approxPolyDP(cnt, peri*0.02, True) #近似多邊形(邊長、近似值、是否為閉合)
            x, y, w, h = cv2.boundingRect(vertices)

#找出筆尖(書寫點)
    return x+w//2, y

#顯示
while True:
    ret, frame = cap.read()
    if ret:
        imgContour = frame.copy()   
        cv2.imshow('video', frame)
        findPen(frame)
        cv2.imshow('contour', imgContour)
    else:
        break

    if cv2.waitKey(10) == ord('q'):
        break