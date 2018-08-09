import numpy as np
import cv2 as cv

img = cv.imread("test.png")
img_gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
ret, img_sh = cv.threshold(img_gray, 127, 255, cv.THRESH_BINARY_INV)
    
im2, contours, hierarchy = cv.findContours(img_sh, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)
#cv.drawContours(img, contours, -1, (0, 255, 0), 3)
#cv.imwrite("out.png", img)

#print(len(contours))

arr = []
cnt = 0
for contour in contours:
    x,y,w,h = cv.boundingRect(contour)
    if w > 50 and w < 200 and h > 50 and h < 200:
        arr.append(contour)
        cnt += 1

    im = img_sh[y:y+h, x:x+w]
    cv.imwrite("cut"+str(cnt)+".png", im)
