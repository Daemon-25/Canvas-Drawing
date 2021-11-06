# -*- coding: utf-8 -*-
"""
Created on Fri Nov  5 12:12:24 2021

@author: laksh
"""

import cv2
import numpy as np

cap = cv2.VideoCapture(0)

while True:
    _, frame = cap.read()
    cv2.imshow("Video", frame)
    
    pts1 = np.float32([[0, 640], [480, 640], [480, 640], [0, 0]])
    pts2 = np.float32([[0, 0], [400, 0], [0, 640], [400, 640]])
    
    matrix = cv2.getPerspectiveTransform(pts1, pts2)
    newframe = cv2.warpPerspective(frame, matrix, (300, 300))
    
    cv2.imshow("Output", newframe)
    
    q = cv2.waitKey(1)
    if q==ord('q'):
        break
    
cap.release()    
cv2.destroyAllWindows() 