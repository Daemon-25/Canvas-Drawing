# -*- coding: utf-8 -*-
"""
Created on Fri Nov  5 14:35:40 2021

@author: laksh
"""

import cv2
import numpy as np

img = cv2.imread("./download.png")

imgHor = np.hstack((img, img))
imgVer = np.vstack((imgHor, imgHor))

cv2.imshow("Images", imgVer)

cv2.waitKey(0)
cv2.destroyAllWindows()