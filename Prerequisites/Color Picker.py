# -*- coding: utf-8 -*-
"""
Created on Sat Nov  6 14:11:23 2021

@author: laksh
"""

import cv2
import numpy as np

def empty(a):
    pass

cv2.namedWindow("Trackbars")
cv2.resizeWindow("Trackbars", 480, 640)
cv2.createTrackbar("H Min", "Trackbars", 0, 179, empty)
cv2.createTrackbar("S Min", "Trackbars", 0, 255, empty)
cv2.createTrackbar("V Min", "Trackbars", 0, 255, empty)
cv2.createTrackbar("H Max", "Trackbars", 0, 179, empty)
cv2.createTrackbar("S Max", "Trackbars", 0, 255, empty)
cv2.createTrackbar("V Max", "Trackbars", 0, 255, empty)

def findColor(img):
    imgHSV = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    
    hMin = cv2.getTrackbarPos("H Min", "Trackbars")
    sMin  = cv2.getTrackbarPos("S Min", "Trackbars")
    vMin = cv2.getTrackbarPos("V Min", "Trackbars")
    hMax = cv2.getTrackbarPos("H Max", "Trackbars")
    sMax = cv2.getTrackbarPos("S Max", "Trackbars")
    vMax = cv2.getTrackbarPos("V Max", "Trackbars")
    
    lower = np.array([hMin, sMin, vMin])
    upper = np.array([hMax, sMax, vMax])
    mask = cv2.inRange(imgHSV, lower, upper)
    
    return mask
    

vid = cv2.VideoCapture(0)
vid.set(10, 150)

while True:
    _, frame = vid.read()
    mask = findColor(frame)
    final = cv2.bitwise_and(frame, frame, mask = mask)
    mask = cv2.cvtColor(mask, cv2.COLOR_GRAY2BGR)
    result = np.hstack([frame, mask, final])
    
    cv2.imshow("Webcam", result)
    
    if cv2.waitKey(1) == ord('q'):
        break
    
vid.release()
cv2.destroyAllWindows()