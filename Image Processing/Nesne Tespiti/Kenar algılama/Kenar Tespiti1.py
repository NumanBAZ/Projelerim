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

img=cv2.imread("res.jpg",0)
plt.figure()
plt.imshow(img,"gray")
plt.axis("off")
plt.show()

# Kenar Tespiti

edges=cv2.Canny(img, threshold1=0, threshold2=255)
plt.figure(),plt.imshow(edges,"gray"),plt.axis("off"),plt.show()

med_val=np.median(img)
print(med_val)

ort_val=np.mean(img)
print(ort_val)






low=int(max(0, (1 - 0.33)*med_val))
high =int(min(255,(1 + 0.33)*med_val))

print(low)
print(high)

edges2=cv2.Canny(img, threshold1=low, threshold2=high)
plt.figure(),plt.imshow(edges2,"gray"),plt.axis("off"),plt.show() 



# suyu saha az belirgin yapmak için blur

blur_img=cv2.blur(img, ksize=(3,3))                 
plt.figure(),plt.imshow(blur_img,"gray"),plt.axis("off"),plt.show() 

med_val1=np.median(blur_img)
print(med_val1)

low1=int(max(0, (1 - 0.33)*med_val))
high1 =int(min(255,(1 + 0.33)*med_val))

print(low1)
print(high1)


edges_blur=cv2.Canny(blur_img, threshold1=low1, threshold2=high1)
plt.figure(),plt.imshow(edges_blur,"gray"),plt.axis("off"),plt.show() 

