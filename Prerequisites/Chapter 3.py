# -*- coding: utf-8 -*-
"""
Created on Fri Nov  5 11:50:12 2021

@author: laksh
"""

import cv2
import numpy as np

img = cv2.imread(".\download.png")

print(img.shape)
cv2.imshow("Image", img)

imgResize = cv2.resize(img, (300, 300))
imgCropped = img[:200, 200:500]
cv2.imshow("Resize", imgResize)
cv2.imshow("Cropped", imgCropped)

cv2.waitKey(0)
cv2.destroyAllWindows()