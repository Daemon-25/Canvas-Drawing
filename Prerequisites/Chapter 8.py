# -*- coding: utf-8 -*-
"""
Created on Fri Nov  5 15:47:12 2021

@author: laksh
"""

import cv2
import numpy as np

def getContours(imgNew):
    contours, hierarchy = cv2.findContours(imgNew, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
    for cnt in contours:
        area = cv2.contourArea(cnt)
        print(area)
        
        if(area>500):
            cv2.drawContours(img, cnt, -1, (255, 0, 0), 3)
            peri = cv2.arcLength(cnt, True)
            print(peri)
            approx = cv2.approxPolyDP(cnt, 0.02*peri, True)
            print(len(approx))
            objCor = len(approx)
            x, y, w, h= cv2.boundingRect(approx)
            
            cv2.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), 2)
            
            if objCor ==3:
                objType = "Triangle"
            elif objCor==4:
                aspRation = w/float(h)
                if aspRation > 0.95 and aspRation <1.05:
                    objType = "Square"
                else:
                    objType = "Rectangle"
            elif objCor>4:
                objType = "Circle"
            else:  
                objType = "None"
            cv2.putText(img, objType, (x + (w//2)-10, y +(h//2)-10), cv2.FONT_HERSHEY_COMPLEX, 0.5, (0, 255, 0), 2)

img = cv2.imread("./shapes.png")

imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
imgBlur = cv2.GaussianBlur(imgGray, (7, 7), 1)
imgCanny = cv2.Canny(imgBlur, 50, 50)

getContours(imgCanny)

cv2.imshow("Result", imgCanny)
cv2.imshow("Contours", img)

cv2.waitKey(0)
cv2.destroyAllWindows()