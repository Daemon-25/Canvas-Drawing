# -*- coding: utf-8 -*-
"""
Created on Sun Nov  7 02:31:50 2021

@author: laksh
"""

import cv2
import numpy as np

##########
widthImg = 640
heightImg = 480
##########

vid = cv2.VideoCapture(0)
vid.set(10, 150)

def preProcessing(img):
    imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    imgBlur = cv2.GaussianBlur(imgGray, (5, 5), 1)
    imgCanny = cv2.Canny(imgBlur, 200, 200)
    
    kernel = np.ones((5, 5))
    
    imgDilate = cv2.dilate(imgCanny, kernel, iterations = 2)
    imgThreshold = cv2.erode(imgDilate, kernel, iterations = 1)
    
    return imgThreshold
    
def getContours(imgNew):
    biggest = np.array([])
    maxArea = 0
    contours, hierarchy = cv2.findContours(imgNew, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
    for cnt in contours:
        area = cv2.contourArea(cnt)
        
        if(area>500):
            #cv2.drawContours(imgContour, cnt, -1, (255, 0, 0), 3)
            peri = cv2.arcLength(cnt, True)
            approx = cv2.approxPolyDP(cnt, 0.02*peri, True)
            if area>maxArea and len(approx) ==4:
                biggest = approx
                maxArea = area
                
    cv2.drawContours(imgContour, biggest, -1, (255, 0, 0), 20)
                
    return biggest

def reorder(myPoints):
    if myPoints !=[]:
        myPoints = myPoints.reshape((4, 2))
        myPointsNew = np.zeros((4, 1, 2), np.int32)
        add = myPoints.sum(1)
        
        myPointsNew[0] = myPoints[np.argmin(add)]
        myPointsNew[3] = myPoints[np.argmax(add)]
        
        diff = np.diff(myPoints, axis = 1)
        myPointsNew[1] = myPoints[np.argmin(diff)]
        myPointsNew[2] = myPoints[np.argmax(diff)]
    
        return myPointsNew
    

def getWarp(img, biggest):
    biggest = reorder(biggest)
    
    pts1 = np.float32(biggest)
    pts2 = np.float32([[0, 0], [widthImg, 0], [0, heightImg], [widthImg, heightImg]])
    
    matrix = cv2.getPerspectiveTransform(pts1, pts2)
    imgOutput = cv2.warpPerspective(frame, matrix, (widthImg, heightImg))
    
    return imgOutput

while True:
    _, frame = vid.read()
    frame = frame[:, :320]
    frame = cv2.resize(frame, (widthImg, heightImg))
    imgContour = frame.copy()
    
    imgThres = preProcessing(frame)
    biggest = getContours(imgThres)
    
    #if biggest == [[], [], [], []]:
    #    biggest = [[0, 0], [widthImg, 0], [0, heightImg], [widthImg, heightImg]]
    imgWarped = getWarp(frame, biggest)
    
    cv2.imshow("Webcam", imgContour)
    
    if cv2.waitKey(1)==ord('q'):
        break
    
vid.release()
cv2.destroyAllWindows()