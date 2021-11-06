# -*- coding: utf-8 -*-
"""
Created on Fri Nov  5 14:44:20 2021

@author: laksh
"""

def empty(a):
    pass

import cv2
import numpy as np

cv2.namedWindow("Trackbars")
cv2.resizeWindow("Trackbars", 640, 240)
cv2.createTrackbar("H Min", "Trackbars", 58, 179, empty)
cv2.createTrackbar("S Min", "Trackbars", 95, 255, empty)
cv2.createTrackbar("V Min", "Trackbars", 29, 255, empty)

cv2.createTrackbar("H Max", "Trackbars", 116, 179, empty)
cv2.createTrackbar("S Max", "Trackbars", 255, 255, empty)
cv2.createTrackbar("V Max", "Trackbars", 255, 255, empty)

img = cv2.imread("./lambo.jpeg")
imgHSV = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    
while True:
    
    hMin = cv2.getTrackbarPos("H Min", "Trackbars")
    sMin  = cv2.getTrackbarPos("S Min", "Trackbars")
    vMin = cv2.getTrackbarPos("V Min", "Trackbars")
    hMax = cv2.getTrackbarPos("H Max", "Trackbars")
    sMax = cv2.getTrackbarPos("S Max", "Trackbars")
    vMax = cv2.getTrackbarPos("V Max", "Trackbars")
    
    lower = np.array([hMin, sMin, vMin])
    upper = np.array([hMax, sMax, vMax])
    mask = cv2.inRange(imgHSV, lower, upper)
    
    imgResult = cv2.bitwise_and(img, img, mask=mask)
    cv2.imshow("Result", imgResult)
    cv2.waitKey(1)


#cv2.imshow("Original", img)
#cv2.imshow("HSV", imgHSV)

cv2.waitKey(0)
cv2.destroyAllWindows()