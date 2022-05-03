"""Kamera açma ve vide kaydetme"""

import cv2

cap=cv2.VideoCapture(0)#harici kamera açma

width=int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
height=int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

print(width,height)


writer=cv2.VideoWriter("Yeni_video.mp4",cv2.VideoWriter_fourcc(*"DVIX"),10,(width,height))

while True:
    ret,frame=cap.read()
    if ret==False:
        print("hata")
    cv2.imshow("Video",frame)
    writer.write(frame)
    
    if cv2.waitKey(1)& 0xFF ==ord('q'):break
    
    
    
    
    
cap.release()
writer.release()
cv2.destroyAllWindows()    

