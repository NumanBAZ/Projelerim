# -*- coding: utf-8 -*-
"""
Created on Sat Feb  5 12:39:15 2022

@author: Numan
"""

""" dosya yolu belirtme"""


import cv2



# Resim boyutu değiştirme
img=cv2.imread("peter.jpeg",0)
print("Resim boyutu",img.shape)
cv2.imshow("Orjinal",img)


img2=cv2.resize(img,(500,700))
print("Yeni boyut",img2.shape)
cv2.imshow("Yeni boyutu",img2)


#Resim Kırpma

img3=img[:100,:300]
print("Kırpık boyutu",img3.shape)
cv2.imshow("Kirpik hali",img3)


k=cv2.waitKey(0) & 0xFF
if k==27:
    cv2.destroyAllWindows()

