import cv2
import numpy as np

cap = cv2.VideoCapture(0)

# 定義藍筆HSV和紅筆HSV範圍
penColorHSV = [
    [100, 150, 116, 130, 255, 255],  # 藍色HSV範圍
    [170, 157, 98, 179, 255, 255]  # 紅色HSV範圍
]

# 定義藍筆和紅筆的BGR顏色
penColorBGR = [
    [255, 0, 0],  # 藍色
    [0, 0, 255]  # 紅色
]

# 存儲畫筆點的位置和顏色
drawPoints = []

def findPen(img):
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)  # 將顏色的 BGR 轉換成 HSV

    for i in range(len(penColorHSV)):
        lower = np.array(penColorHSV[i][:3])
        upper = np.array(penColorHSV[i][3:6])

        mask = cv2.inRange(hsv, lower, upper)
        penx, peny = findContour(mask)
        if penx != -1 and peny != -1:
            cv2.circle(imgContour, (penx, peny), 10, penColorBGR[i % len(penColorBGR)], cv2.FILLED)
            drawPoints.append([penx, peny, i % len(penColorBGR)])

def findContour(img):
    contours, hierarchy = cv2.findContours(img, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
    x, y, w, h = -1, -1, -1, -1
    for cnt in contours:
        area = cv2.contourArea(cnt)  # 過濾面積
        if area > 500:
            peri = cv2.arcLength(cnt, True)
            vertices = cv2.approxPolyDP(cnt, peri * 0.02, True)
            x, y, w, h = cv2.boundingRect(vertices)
    return x + w // 2, y

def draw(drawpoints):
    for point in drawpoints:
        cv2.circle(imgContour, (point[0], point[1]), 10, penColorBGR[point[2]], cv2.FILLED)

while True:
    ret, frame = cap.read()
    if ret:
        frame = cv2.flip(frame, 1)  # 水平翻轉影像
        imgContour = frame.copy()
        findPen(frame)
        draw(drawPoints)
        cv2.imshow('contour', imgContour)
    else:
        break
    if cv2.waitKey(1) == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
