# -*- coding: utf-8 -*-
"""
Created on Sat Feb  5 12:39:15 2022

@author: Numan
"""

""" Resim içe aktarma"""


import cv2


img=cv2.imread("a.jpg",0)

cv2.imshow("resim",img)

k=cv2.waitKey(0) & 0xFF

if k==27:
    cv2.destroyAllWindows()
elif ord('s'):
    cv2.imwrite("Ironman_gray.png",img)
    cv2.destroyAllWindows()
    