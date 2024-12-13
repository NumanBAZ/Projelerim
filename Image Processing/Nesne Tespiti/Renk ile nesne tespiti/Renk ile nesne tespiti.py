# -*- coding: utf-8 -*-
"""
Created on Sat Feb  5 12:39:15 2022

@author: Numan
"""

""" Resim içe aktarma"""


import cv2
from collections import deque
import numpy as np



buffer_size=16
pts=deque(maxlen=buffer_size)
#mavi renk aralığı

blueLower=(84,89,0)
blueUpper=(179,255,255)


# video aktarma

cap=cv2.VideoCapture(0)
cap.set(3, 960)
cap.set(4,480)

while True:
    
    
    success,imgOrjinal=cap.read()
   
    if success:
        
        #blur
          cv2.imshow("blu1r Image",imgOrjinal)
          blurred=cv2.GaussianBlur(imgOrjinal, (11,11), 0)
          #cv2.imshow("blur Image",blurred)
        
        #HSV convert
        
          hsv=cv2.cvtColor(blurred, cv2.COLOR_BGR2HSV)
          cv2.imshow("HVS img",hsv)
        
        
        #mavi için maske oluştur
        
          mask=cv2.inRange(hsv, blueLower, blueUpper)
          cv2.imshow("mask Image",mask)
        
        #maskenin ardında kalan gürültüleri sil
        
          mask = cv2.erode (mask,None,iterations=2)
          mask=cv2.dilate(mask,None,iterations=2)
          cv2.imshow("mask + erazyon ve genişleme Image",mask)
        
       # Contoure
          (_,contoure,_)=cv2.findContours(mask.copy(),cv2.RETR_CCOMP,cv2.CHAIN_APPROX_SIMPLE)
          center=None
          if len(contoure)>0:
              #en büyük kontürü al
              c=max(contoure,key=cv2.contourArea)
              
              #dikdörtgene çevir
              rect=cv2.minAreaRect(c)
              
              ((x,y),(width,height),rotation)=rect
            
              s="x: {}  ,y: {}, width: {}, height: {} rotation: {}".format(np.round(x),np.round(y),np.round(width),np.round(height),np.round(rotation))
              print(s)
              
              
              #kutucuk
              box=cv2.boxPoints(rect)
              box=np.int64(box)
              
              
              #moment
              M= cv2.moments(c)
              center=(int(M["m10"]/M["m00"]),int(M["m01"]/M["m00"]))
            
              #Kontur çizdir: sarı
              cv2.drawContours(imgOrjinal, [box],0, (0,255,255),2)
              
              #merkeze bir tane nokta 
              cv2.circle(imgOrjinal, center, 5,(255,0,255), -1)
              
          cv2.imshow("blu1rr Image",imgOrjinal)
              
    if cv2.waitKey(1)& 0xFF==ord('q'):break          
              
              
              
              
              
              
              
              
              
              
              
              
              
              
              
              
              
              
       
       
       
       
       
       
       
       
       
       
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        