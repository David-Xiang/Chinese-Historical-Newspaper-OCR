import numpy as np
import cv2 as cv
import sys
from threshold import threshold
from showPic import showImg

def printDilationLines(name):
    img_sh = threshold(name + ".png")
    im2 = cv.dilate(img_sh, np.ones((15, 15), np.uint8), 1)
    lines = cv.HoughLinesP(im2-img_sh, 1, np.pi/180, 100, minLineLength=150, maxLineGap=10)
    flat = []
    for line in lines:
        x1, y1, x2, y2 = line[0]
        if getAbsTan(x1, y1, x2, y2) < 0.4:
            flat.append(line)

    print(str(len(flat))+" horizotal lines are found!")
    img = cv.imread(name + ".png")
    for line in flat:
        x1, y1, x2, y2 = line[0]
        cv.line(img, (x1, y1), (x2, y2), (0, 0, 255), 20)
    cv.imwrite(name+"_out.png", img)

def getAbsTan(x1, y1, x2, y2):
    tan = (y2 - y1) / (x2 - x1)
    if tan >= 0:
        return tan
    else:
        return -tan

for i in range(0, 8):
    print("img-00"+str(i))
    printDilationLines("img-00"+str(i))
