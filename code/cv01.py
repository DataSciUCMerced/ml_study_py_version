#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 23 09:13:21 2017

@author: haiyangwang
"""

import cv2
import numpy as np

img = cv2.imread('../images/Lenna.png', 0)

rows, cols = img.shape

M = np.float32([[1, 0 , 100], [0, 1, 50]])


dst = cv2.warpAffine(img, M, (cols, rows))

cv2. imshow('img', dst)

cv2.waitKey(0)

cv2.destroyAllWindows()
