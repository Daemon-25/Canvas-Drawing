# -*- coding: utf-8 -*-
"""
Created on Sat Nov  6 11:34:11 2021

@author: laksh
"""

import cv2
import numpy as np

faceCascade = cv2.CascadeClassifier(".\haarcascade_frontalface_default.xml")

vid = cv2.VideoCapture(0)

while True:
    _,img = vid.read()
    imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    
    faces = faceCascade.detectMultiScale(imgGray, 1.1, 4)
    for(x, y, w, h) in faces:
        cv2.rectangle(img, (x, y), (x+w, y+h), (0, 0, 255), 2)
    cv2.imshow("Result", img)
    
    q = cv2.waitKey(1)
    if q==ord('q'):
        break

vid.release()
cv2.destroyAllWindows()