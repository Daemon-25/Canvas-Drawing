# -*- coding: utf-8 -*-
"""
Created on Sat Nov  6 11:47:13 2021

@author: laksh
"""

import cv2
import numpy as np

def empty(a):
    pass

myPoints = []                      #[x, y, colorID, size]
prev = 0
myColors = [[49, 56, 186, 110, 203, 255],   #blue
            [143, 107, 197, 179, 255, 255],     #pink
            [22, 45, 118, 67, 182, 255]]     #green
# alternate for blue
#[49, 56, 186, 110, 203, 255], [69, 56, 199, 119, 255, 255]

myColorValues = [[255, 0, 0],       #BGR
                 [255, 0, 255],
                 [102, 255, 178]]

def findColor(img, myColors, myColorValues):
    #Covert image to HSV
    imgHSV = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    
    #To keep the count of the colors
    count = 0
    newPoints = []
    
    #For iterating through all the ranges of the colors
    for clr in myColors:
        #Mask for each color
        lower = np.array(clr[0:3])
        upper = np.array(clr[3:6])
        mask = cv2.inRange(imgHSV, lower, upper)
        
        #cv2.imshow(str(color[0], mask))
        
        #Calling the function to draw contours and returning coordinates of the points of the tip
        x, y = getContours(mask)
        if x!=0 and y!=0:
            cv2.circle(frame, (x, y), cv2.getTrackbarPos("Size", 'Whiteboard'), myColorValues[count], cv2.FILLED)
            newPoints.append([x, y, count, cv2.getTrackbarPos("Size", 'Whiteboard')])
        count +=1
    return newPoints
        
#Function to get contours
def getContours(imgNew):
    #Finding contours
    contours, hierarchy = cv2.findContours(imgNew, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
    
    #Setting default values for the coordinates of the tip
    x,y,w,h = 0,0,0,0
    for cnt in contours:
        area = cv2.contourArea(cnt)
        
        if area>500:
            #cv2.drawContours(frame, cnt, -1, (255, 0, 0), 3)
            
            #Finding the Coordinates of the tip of the pen
            peri = cv2.arcLength(cnt, True)
            approx = cv2.approxPolyDP(cnt, 0.02*peri, True)
            x, y, w, h= cv2.boundingRect(approx)
    
    return x+w//2, y
    
#Function to draw on canvas
def drawOnCanvas(myPoints, myColorValues):
    for pt in myPoints:
        cv2.circle(result, (pt[0], pt[1]), pt[3], myColorValues[pt[2]], cv2.FILLED)

vid = cv2.VideoCapture(0)
vid.set(10, 150)

result = np.zeros([600, 800, 3], np.uint8)
cv2.namedWindow("Whiteboard")
cv2.createTrackbar("Size", "Whiteboard", 10, 500, empty)
cv2.createTrackbar("Clear", "Whiteboard", 0, 1, empty)
cv2.createTrackbar("Switch", 'Whiteboard', 0, 1, empty)

while True:
    _, frame = vid.read()
    
    #Flip the frame
    frame = cv2.flip(frame, 1)
    frame = cv2.resize(frame, (800, 600))
    
    #find the points of the tip of the pen
    newPoints = findColor(frame, myColors, myColorValues)
    
    #drawing on frame using circle function
    if len(newPoints)!=0:
        for newP in newPoints:
            myPoints.append(newP)
            
    if cv2.getTrackbarPos("Switch", "Whiteboard")==0:
        myPoints.clear()
        
    if len(myPoints)!=0:
        drawOnCanvas(myPoints, myColorValues)
        
    if cv2.getTrackbarPos("Clear", "Whiteboard")!=prev:
        result = np.zeros([600, 800, 3], np.uint8)
        myPoints.clear()
        prev = cv2.getTrackbarPos("Clear", "Whiteboard")

    cv2.imshow("WebCam", frame)
    cv2.imshow("Whiteboard", result)
    
    if cv2.waitKey(1) == ord('q'):
        break
    
vid.release()
cv2.destroyAllWindows()