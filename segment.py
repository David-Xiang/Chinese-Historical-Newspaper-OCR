import numpy as np
import cv2 as cv
import sys
from threshold import threshold
from showPic import showImg
from dilation import getDilationLines
def getSegments(name):
    # according to detected lines, segment the whole image and wipe the lines

    img = cv.imread(name+".png")
    img_re = threshold(name+".png", reverse=True)
    img_sh = threshold(name+".png", reverse=False)
    lines = getDilationLines(img_re, 10, 400, 10)
    # the last 3 params are kernelSize, minLineLength and maxGapLength
    print(str(len(lines)) + " lines detected!")
    
    flat_lines = []
    vrt_lines = [] 
    # each line are defined as a duple:
    # flat line: (sum_y, number_of_lines)
    # vrt_line: (sum_x, number_of_lines)
    for line in lines:
        x1, y1, x2, y2 = line[0]
        tan = abstan(x1, y1, x2, y2)
        # 合并lines的过程后面可以用堆来优化

        if tan < 0.4:
            y = (y1 + y2) / 2
            found = False
            for i in range(len(flat_lines)):
                avg_y = flat_lines[i][0] / flat_lines[i][1]
                if avg_y - y < 200 and avg_y - y > -200:
                    found = True
                    flat_lines[i] = (flat_lines[i][0] + y, flat_lines[i][1] + 1)
                    break
            if found is False:
                flat_lines.append((y, 1))

        elif tan > 2.5:
            x = (x1 + x2) / 2
            found = False
            for i in range(len(vrt_lines)):
                avg_x = vrt_lines[i][0] / vrt_lines[i][1]
                if avg_x - x < 200 and avg_x - x > -200:
                    found = True
                    vrt_lines[i] = (vrt_lines[i][0] + x, vrt_lines[i][1] + 1)
                    break
            if found is False:
                vrt_lines.append((x, 1))
        else:
            print("A line is neither a flat line or a vertical line!")
    
    # find cordinates for segmentation
    anchor_x = [int(sum_x/nline + 0.5) for (sum_x, nline) in vrt_lines]
    anchor_y = [int(sum_y/nline + 0.5) for (sum_y, nline) in flat_lines]
    
    anchor_x.append(0)
    anchor_x.append(img.shape[1] - 1) # number of pixels in column
    anchor_y.append(0)
    anchor_y.append(img.shape[0] - 1) # number of pixels in row

    anchor_x.sort()
    anchor_y.sort()
    print(anchor_x)
    print(anchor_y)
    nx = len(anchor_x) - 1
    ny = len(anchor_y) - 1
    
    # wipe originally found lines with white pixels
    for line in lines:
        x1, y1, x2, y2 = line[0]
        cv.line(img_sh, (x1, y1), (x2, y2), 255, 30)

    # do segmentation in order -- from top to bottom & from right to left
    segments = []
    for i in range(nx * ny):
        ix = nx - 1 - int(i / ny)
        iy = i % ny
        print(str(anchor_y[iy])+","+str(anchor_x[ix]))
        segments.append(img_sh[anchor_y[iy]:anchor_y[iy+1], anchor_x[ix]:anchor_x[ix+1]])
    
    # export original image with split lines for DEBUGGING
    for x in anchor_x:
        cv.line(img, (x, 0), (x, img.shape[0] - 1), (255, 0, 0), 5)
    for y in anchor_y:
        cv.line(img, (0, y), (img.shape[1] - 1, y), (255, 0, 0), 5)
    cv.imwrite(name+"_seg.png", img)

    return segments

def abstan(x1, y1, x2, y2):
    if x1 == x2:
        return 1000
    tan = (y2 - y1) / (x2 - x1)
    if tan >= 0:
        return tan
    else:
        return -tan
    
  
if __name__=="__main__":
    segments = getSegments("test")
    for i in range(len(segments)):
        cv.imwrite("test_seg_"+str(i)+".png", segments[i])
