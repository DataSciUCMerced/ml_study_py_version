#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov  8 14:45:23 2017

@author: haiyangwang

Color Quantization is the process of reducing number of colors in an image. 
One reason to do so is to reduce the memory. Sometimes, 
some devices may have limitation such that it can produce o
nly limited number of colors. In those cases also, 
color quantization is performed. 
Here we use k-means clustering for color quantization.

There is nothing new to be explained here. There are 3 features, 
say, R,G,B. So we need to reshape the image to an array of Mx3 size 
(M is number of pixels in image). And after the clustering, 
we apply centroid values (it is also R,G,B) to all pixels, 
such that resulting image will have specified number of colors. 
And again we need to reshape it back to the shape of original image. 

"""

import numpy as np
import cv2

img = cv2.imread('./images/home.jpg')
#cv2.imshow('ori', img)
Z = img.reshape((-1,3))

# convert to np.float32
Z = np.float32(Z)

# define criteria, number of clusters(K) and apply kmeans()
criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 10, 1.0)
K = 8
ret,label,center=cv2.kmeans(Z,K,None,criteria,10,cv2.KMEANS_RANDOM_CENTERS)

# Now convert back into uint8, and make original image
center = np.uint8(center)
res = center[label.flatten()]
res2 = res.reshape((img.shape))

cv2.imshow('res2',res2)
cv2.destroyAllWindows()
cv2.waitKey(0)




