# -*- coding: utf-8 -*-
"""
Created on Sat Feb  5 12:39:15 2022

@author: Numan
"""

""" dosya yolu belirtme"""
import cv2
import matplotlib.pyplot as plt
import numpy as np
import warnings


warnings.filterwarnings("ignore")


img=cv2.imread("peter.jpeg")
img=cv2.cvtColor(img,cv2.COLOR_BGR2RGB)

plt.figure()
plt.imshow(img)
plt.axis("off")
plt.title("Orjinal")
plt.show()

#resim bulanıklaştırma
""" 
ortalaması alınarak yapılan bulnıklaştırma
"""

dst2=cv2.blur(img, ksize=(3,3))
plt.figure()
plt.imshow(dst2)
plt.axis("off")
plt.title("bulanık")
plt.show()