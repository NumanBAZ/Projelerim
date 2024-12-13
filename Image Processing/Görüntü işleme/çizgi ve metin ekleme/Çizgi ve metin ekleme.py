# -*- coding: utf-8 -*-
"""
Created on Sat Feb  5 12:39:15 2022

@author: Numan
"""

""" dosya yolu belirtme"""
import cv2
import numpy as np



#resim oluşturma
img=np.zeros((512,512,3),np.uint8)
cv2.imshow("Resim",img)


#Çizgi ekleme
#(resim,başlangıç,bitiş,renk,kalınlık)  BGR(0,0,0)
cv2.line(img,(0,0),(512,512),(225,0,0),3)
cv2.imshow("Cizgi",img)


#cv2.FILLED içinin doluluk oranı

#Kare ekleme
cv2.rectangle(img,(0,0),(100,100),(0,0,225),cv2.FILLED)
cv2.imshow("Cizgi",img)


# Çember ekleme
cv2.circle(img,(300,300),30,(0,225,0),cv2.FILLED)
cv2.imshow("Cizgi",img)


#Metin ekleme
cv2.putText(img,"Resim",(200,200),cv2.FONT_HERSHEY_COMPLEX,1,(255,255,255))
cv2.imshow("Cizgi",img)





k=cv2.waitKey(0) & 0xFF
if k==27:
    cv2.destroyAllWindows()
    
elif k!=27:
    cv2.destroyAllWindows()
    