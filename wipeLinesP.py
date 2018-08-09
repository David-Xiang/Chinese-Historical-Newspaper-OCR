import numpy as np
import cv2 as cv
import sys
from threshold import threshold
from showPic import showImg

img_sh = threshold(sys.argv[1]+".png")
im2 = cv.dilate(img_sh, np.ones((10, 10)), 2)
lines = cv.HoughLinesP(im2-img_sh, 1, np.pi/180, 100, minLineLength=400, maxLineGap=10)
print(len(lines))

img = cv.imread(sys.argv[1]+".png")
for line in lines:
    x1, y1, x2, y2 = line[0]
    cv.line(img, (x1, y1), (x2, y2), (0, 0, 255), 20)

cv.imwrite(sys.argv[1]+".png", img)
