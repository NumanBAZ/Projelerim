# -*- coding: utf-8 -*-
"""
Created on Sat Feb  5 12:39:15 2022

@author: Numan
"""

""" dosya yolu belirtme"""


import cv2
import numpy as np

img=cv2.imread("kupa1.jpg")
cv2.imshow("Ters resim",img)

width=472
height=680

pts1=np.float32([[42,174],[42,646],[722,174],[722,646]])
pts2=np.float32([[0,height],[width,height],[0,0],[472,0]])


matrix=cv2.getPerspectiveTransform(pts1,pts2)
print(matrix)


imout=cv2.warpPerspective(img,matrix,(width,height))
cv2.imshow("Ters resim",imout)



k=cv2.waitKey(0) & 0xFF
if k==27:
    cv2.destroyAllWindows()
    
elif k!=27:
    cv2.destroyAllWindows()
