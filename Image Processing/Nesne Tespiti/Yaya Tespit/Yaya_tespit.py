# -*- coding: utf-8 -*-
"""
Created on Sat Feb  5 12:39:15 2022

@author: Numan
"""

""" Resim içe aktarma"""


import cv2

import numpy as np

""" Resim içe aktarma"""
import cv2
import numpy as np
# resimi içe aktarma
img=cv2.imread("indir.jpg",0)
img=cv2.resize(img,(800,600))

#Resimdeki Kenaları tespit etme
edges=cv2.Canny(image=img, threshold1=200, threshold2=255)
cv2.imshow("Kenar",edges)

#Yüz tespiti
face_cascade=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

face_rect=face_cascade.detectMultiScale(img)
for (x,y,w,h ) in face_rect:
    rect=cv2.rectangle(img,(x,y),(x+w,y+h),(255,255,255),5)
cv2.imshow("Yuz tanima",rect)

# Yaya tespiti
hog=cv2.HOGDescriptor()
hog.setSVMDetector(cv2.HOGDescriptor_getDefaultPeopleDetector())
cv2.imshow("Yaya",img)
(rects,weights)=hog.detectMultiScale(img , padding =(8,8),scale=1.05)
cv2.imshow("Yaya",rects)

for (xA,yA,wA,hA) in rects:
    cv2.rectangle(rects, (xA,yA), (xA+wA,yA+hA),(0,0,255),5)

#cv2.imshow("Yaya",rects)