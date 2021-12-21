import cv2
import numpy as np

def select_roi():
    # Read image
    im = cv2.imread("pic.png")
    # im = cv2.imread("image.jpg")

    # Select ROI
    r = cv2.selectROI(im)
    print(r)
    # Crop image
    imCrop = im[int(r[1]):int(r[1]+r[3]), int(r[0]):int(r[0]+r[2])]
 
    # Display cropped image
    cv2.imshow("Image", imCrop)
    cv2.waitKey(0)
    
if __name__ == '__main__'
    select_roi()
