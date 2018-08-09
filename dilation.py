import numpy as np
import cv2 as cv
import sys
from threshold import threshold
from showPic import showImg

def getDilationLines(img, kernel=10, minlen=300, maxgap=10):
    im2 = cv.dilate(img, np.ones((kernel, kernel), np.uint8), 1)
    lines = cv.HoughLinesP(im2-img, 1, np.pi/180, 100, minLineLength=minlen, maxLineGap=maxgap)
    return lines

def printDilationLines(name):
    img_sh = threshold(name + ".png")
    lines = getDilationLines(img_sh, 10, 300, 10)
    print(len(lines))
    img = cv.imread(name + ".png")
    for line in lines:
        x1, y1, x2, y2 = line[0]
        cv.line(img, (x1, y1), (x2, y2), (0, 0, 255), 20)
    cv.imwrite(name+"_out.png", img)

if __name__=="__main__":
    for i in range(0, 8):
        print("img-00"+str(i))
        printDilationLines("img-00"+str(i))
