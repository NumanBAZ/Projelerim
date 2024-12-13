# -*- coding: utf-8 -*-
"""
Created on Sat Feb  5 12:39:15 2022

@author: Numan
"""

""" Resim içe aktarma"""


import cv2
import matplotlib.pyplot as plt
import numpy as np

# resim içe aktarma

img = cv2.imread("sdoku.png", 0)
img = np.float32(img)
print(img.shape)
plt.figure()
plt.imshow(img,cmap="gray")
plt.axis("off")
# Köşe tespiti

dst=cv2.cornerHarris(img, blockSize=2, ksize=3, k=0.04)
plt.figure()
plt.imshow(dst,cmap="gray")
plt.axis("off")

dst2=cv2.dilate(dst,None)
img[dst>0.2*dst.max()]=1
plt.figure()
plt.imshow(dst2,cmap="gray")
plt.axis("off")
