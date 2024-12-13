# -*- coding: utf-8 -*-
"""
Created on Sat Feb  5 12:39:15 2022

@author: Numan
"""

""" Resim içe aktarma"""


import cv2
import matplotlib.pyplot as plt

img=cv2.imread("indir.png",0)
plt.figure()
plt.imshow(img,cmap="gray")
plt.axis("off")
plt.show()

sobelx=cv2.Sobel(img, ddepth=cv2.CV_16S, dx=0, dy=1, ksize=5)
plt.figure()
plt.imshow(sobelx,cmap="gray")
plt.axis("off")
plt.show()

laplacian=cv2.Laplacian(img, ddepth=cv2.CV_16S)
plt.figure()
plt.imshow(laplacian,cmap="gray")
plt.axis("off")
plt.show()
