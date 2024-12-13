import cv2
import pickle
import numpy as np

def preProcess(img):
    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    img = cv2.equalizeHist(img)
    img = img /255.0
    
    return img

cap = cv2.VideoCapture(0)
cap.set(3,480)
cap.set(4,480)

pickle_in = open("meyve_weight1_new.h5","rb")
model = pickle.load(pickle_in)


while True:
    
    success, frame = cap.read()
    
    img = np.asarray(frame)
    img = cv2.resize(img, (32,32))
    img = preProcess(img)
    
    img = img.reshape(1,32,32,1)
    
    # predict
    classIndex = int(model.predict_classes(img))
    
    predictions = model.predict(img)
    probVal = np.amax(predictions)
    print(classIndex, probVal)
 
    cv2.imshow("Rakam Siniflandirma",frame)

    if cv2.waitKey(1) & 0xFF == ord("q"): break    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    