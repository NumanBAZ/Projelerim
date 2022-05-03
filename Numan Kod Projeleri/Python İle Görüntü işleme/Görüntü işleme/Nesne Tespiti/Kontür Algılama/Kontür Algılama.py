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

img=cv2.imread("Kontur.png",0)
              
plt.figure(),plt.imshow(img,cmap="gray"),plt.axis("off")
# Kontur uygulama

image, contours ,hierarch = cv2.findContours (img, cv2.RETR_CCOMP,cv2.CHAIN_APPROX_SIMPLE)

external_contour=np.zeros(img.shape)
internal_contour=np.zeros(img.shape)




for i in range(len(contours)):
    if hierarch[0][i][3]==-1:
        cv2.drawContours(external_contour,contours,i,255,-1)
    else:
        cv2.drawContours(internal_contour, contours,i,255,-1)

plt.figure(),plt.imshow(external_contour,cmap="gray"),plt.axis("off")
plt.figure(),plt.imshow(internal_contour,cmap="gray"),plt.axis("off")        
