# -*- coding: utf-8 -*-
"""
Created on Sat Feb  5 12:39:15 2022

@author: Numan
"""


"""Video içe aktarma"""

import cv2
import time

video_name="Bumblebee"
cap=cv2.VideoCapture(video_name)

print("Genişlik",cap.get(3))
print("Yükseklik",cap.get(4))

if cap.isOpened()==False:
    print("Hata")
    
while True:
   ret,frame=cap.read()

   if ret==True:
       time.sleep(0.001)
       cv2.imshow("Video",frame)
   else: break

   if cv2.waitKey(1)&0xFF==ord('q'):
       break

    
cap.release()
cv2.destroyAllWindows