# -*- coding: utf-8 -*-
"""
Created on Sat Feb  5 12:39:15 2022

@author: Numan
"""

""" dosya yolu belirtme"""

import cv2 
import numpy as np

img=cv2.imread("b.jpg",)
cv2.imshow("Resim",img)


hor=np.hstack((img,img))
cv2.imshow("yeni resim",hor)


ver=np.vstack((img,img))
cv2.imshow("yeni resim 2",ver)


k=cv2.waitKey(0) & 0xFF
if k==27:
    cv2.destroyAllWindows()
    
elif k!=27:
    cv2.destroyAllWindows()
    