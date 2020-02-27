# This is the problem for First technical round for the role of Computer Vision Engineer at Vectorly
# More details at https://www.linkedin.com/jobs/view/1629909785/
#
# Write a function which will segment and extract the text overlay "Bart & Homer's EXCELLENT Adventure" 
# Input image is at https://vectorly.io/demo/simpsons_frame0.png
# Output : Image with only the overlay visible and everything else white
# 
# Note that you don't need to extract the text, the output is an image with only 
# the overlay visible and everything else (background) white
#
# You can use the snipped below (in python) to get started if you like 
# Python is not required but is preferred. You are free to use any libraries or any language


#####################

import cv2
import numpy as np

def getTextOverlay(img):
    #output = np.zeros(input_image.shape, dtype=np.uint8)
     
    # Write your code here for output
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2LAB)[...,0]
    edges = cv2.Canny(gray, 10,30)    
    blurred = cv2.GaussianBlur(gray, (7, 7), 0)
    clahe = cv2.createCLAHE(clipLimit=5.0, tileGridSize=(32,32))
    contrast = clahe.apply(blurred)
    ret, thresh = cv2.threshold(contrast, 20, 255, cv2.THRESH_BINARY|cv2.THRESH_OTSU)
    cv2.imshow("result", thresh)
    #k = cv2.waitKey(30) & 0xff
    return thresh

if __name__ == '__main__':
    image = cv2.imread("./img.png", cv2.IMREAD_COLOR)
    output = getTextOverlay(image)
    cv2.imwrite('simpons_text.png', output)
