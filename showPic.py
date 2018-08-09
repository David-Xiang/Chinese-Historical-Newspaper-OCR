import numpy as np
import cv2 as cv
import sys

def showPic(path, para = 1):
    # para = 1: cv.IMREAD_COLOR
    # para = 0: cv.IMREAD_GRAYSCALE
    # para = -1: cv.IMREAD_UNCHANGED
    img = cv.imread(path, para)
    if img is None:
        return False
    showImg(img, path)
    return True
    
def showImg(img, name = "image"):
    cv.namedWindow(name, cv.WINDOW_NORMAL)
    cv.imshow(name, img)
    cv.waitKey(0)
    cv.destroyAllWindows()

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("usage: python showPic.py <name-of-input-pic>")
        raise(NameError)

    if showPic(sys.argv[1]) == False:
        print(sys.argv[1] + " is NOT a valid picture URI")
