import cv2
import os


# resim içe aktarma

file=os.listdir();
print(file)

img_list=[]
for f in file:
    if f.endswith(".jpg"):
        img_list.append(f)
print(img_list)


for j in img_list:
    image=cv2.imread(j)
    gray=cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
    detector=cv2.CascadeClassifier("haarcascade_frontalcatface.xml")
    rects=detector.detectMultiScale(image,scaleFactor=1.045,minNeighbors=2)
    
    for (i,(x,y,w,h)) in enumerate(rects):
        cv2.rectangle(image,(x,y),(x+w,y+h),(0,255,255),2)
        cv2.putText(image,"Kedi{}".format(i+1),(x,y-10),cv2.FONT_HERSHEY_SIMPLEX,0.5,(0,255,255),2)
        
    
    
    
    cv2.imshow(j,image)
    if cv2.waitKey(0) & 0xFF ==ord('q'): continue