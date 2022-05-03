# -*- coding: utf-8 -*-
"""
Created on Sat Feb  5 12:39:15 2022

@author: Numan
"""

""" Resim içe aktarma"""


import cv2
import matplotlib.pyplot as plt

img1=cv2.imread("a.jpg")
img1=cv2.cvtColor(img1,cv2.COLOR_BGR2RGB)
#cv2.imshow("resim",img1)

img2=cv2.imread("b.jpg")
img2=cv2.cvtColor(img2,cv2.COLOR_BGR2RGB)
#cv2.imshow("resim1",img2)


print(img1.shape)
print(img2.shape)

img1=cv2.resize(img1,(300,300))
img2=cv2.resize(img2,(300,300))
"""
k=cv2.waitkey(0) & 0xff

if k==27:
    cv2.destroyallwindows()
elif k!=27:
    cv2.destroyallwindows()
"""
plt.figure()
plt.imshow(img1)

plt.figure()
plt.imshow(img2)


# reim karıştırma
blended=cv2.addWeighted(src1=img1, alpha=0.5, src2=img2, beta=0.5, gamma=0)

plt.figure()
plt.imshow(blended)















