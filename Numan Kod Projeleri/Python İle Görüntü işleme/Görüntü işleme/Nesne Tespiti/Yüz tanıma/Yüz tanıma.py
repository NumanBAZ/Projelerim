import cv2
import matplotlib.pyplot as plt

einstein=cv2.imread("1.png",0) 
plt.figure() , plt.imshow(einstein,cmap="gray"),plt.axis("off")


#sınıflandırma

face_cascade=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
face_rect=face_cascade.detectMultiScale(einstein)

for (x,y,w,h) in face_rect:
    cv2.rectangle(einstein, (x,y),(x+w,y+h) ,(255,255,255),5)
plt.figure() , plt.imshow(einstein,cmap="gray"),plt.axis("off")
    
      
                  

barca=cv2.imread("barca.jpg",0) 
plt.figure() , plt.imshow(barca,cmap="gray"),plt.axis("off")    
        
face_cascade=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
face_rect=face_cascade.detectMultiScale(barca,minNeighbors=10)

#minNeighbors komuşu karelerin sayısına göre yani daha dikkatli arama yapar


for (x,y,w,h) in face_rect:
    cv2.rectangle(barca, (x,y),(x+w,y+h) ,(255,255,255),5)
plt.figure() , plt.imshow(barca,cmap="gray"),plt.axis("off")
    
      
while True :
    ret ,frame =cap.read()
       if ret:
           face_rect=face_cascade.detectMultiScale(barca,minNeighbors=10)