# -*- coding: utf-8 -*-
"""
Created on Sat Feb  5 12:39:15 2022

@author: Numan
"""

""" Resim içe aktarma"""


import cv2
import matplotlib.pyplot as plt


#cv2.imshow("resim",img1)

img2=cv2.imread("b.jpg")
img2=cv2.cvtColor(img2,cv2.COLOR_BGR2GRAY)


"""
print(img2.shape)
k=cv2.waitkey(0) & 0xff

if k==27:
    cv2.destroyallwindows()
elif k!=27:
    cv2.destroyallwindows()
"""
"""
plt.figure()
plt.imshow(img2,cmap="gray")
plt.axis("off")
plt.show()
"""
"""
# Eşikleme                                                          THRESH_BINARY_INV yaparsak tam tesri
_,thresh_image=cv2.threshold(img2, thresh=60, maxval=255, type=cv2.THRESH_BINARY)

plt.figure()
plt.imshow(thresh_image,cmap="gray")
plt.axis("off")
plt.show()
"""

# Uyarlamalı eşik

thresh_image2=cv2.adaptiveThreshold(img2, 255, cv2.ADAPTIVE_THRESH_MEAN_C,  cv2.THRESH_BINARY,11,8)


plt.figure()
plt.imshow(thresh_image2,cmap="gray")
plt.axis("off")
plt.show()






