_import cv2

cap=cv2.VideoCapture(0)
ret,frame=cap.read()

if ret == False:
    print("Uyarı!")


#detection
face_cascade=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")    
face_rect=face.detectMultiScale(frame)

(face_x,face_y,w,h)=tuple[face_rect[0]]
track_window
    