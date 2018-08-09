import numpy as np
import cv2 as cv
import sys

def threshold(path, reverse=False):
    img = cv.imread(path)
    if img is None:
        return None

    img_gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    
    mod = cv.THRESH_BINARY
    if reverse == True:
        mod = cv.THRESH_BINARY_INV

    ret, img_sh = cv.threshold(img_gray, 100, 255, mod)
    return img_sh

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("usage: python threshold.py <input-pic> <output-pic>")
        raise(NameError)

    img = threshold(sys.argv[1], False)
    
    if img == None:
        print(sys.argv[1] + " is NOT a valid picture URI!")
        raise(NameError)

    cv.imwrite(sys.argv[2], img)
        
