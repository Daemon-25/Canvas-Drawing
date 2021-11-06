# -*- coding: utf-8 -*-
"""
Created on Thu Nov  4 23:30:24 2021

@author: laksh
"""

import cv2
import numpy as np

img = cv2.imread(".\download.png")
kernel = np.ones((5, 5), np.uint8)

imgBlur = cv2.GaussianBlur(img, (7, 7), 0)
imgCanny = cv2.Canny(img, 150, 200)
imgDilation = cv2.dilate(imgCanny, kernel, iterations = 1)
imgEroded = cv2.erode(imgDilation, kernel, iterations = 1)


cv2.imshow("Image", img)
cv2.imshow("Blur", imgBlur)
cv2.imshow("Canny", imgCanny)
cv2.imshow("Dilation", imgDilation)
cv2.imshow("Eroded", imgEroded)

cv2.waitKey(0)
cv2.destroyAllWindows()