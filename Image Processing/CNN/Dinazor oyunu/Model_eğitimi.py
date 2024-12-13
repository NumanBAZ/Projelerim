import glob
import os
import numpy as np
from keras.models import Sequential
from keras.layers import Dense,Dropout,Flatten,Conv2D,MaxPool2D
from PIL import Image
from sklearn.preprocessing import LabelEncoder,OneHotEncoder
from sklearn.model_selection import train_test_split
import seaborn as sns


#Dense Tam bağlantı katmanları, Dropout= seyreltme ,Flatten= düzleştirme,
#Conv2D=evrişim ağı, MaxPool2D=piksel ekleme
#LabelEncoder=verileri etiketler,OneHotEncoder=keras sa verileri eğittri
   
import warnings
warnings.filterwarnings("ignore")     
        
imgs=glob.glob("./img/*.png")
width=125
height=50

X=[]        
Y=[]

for img in imgs:
    
    filename=os.path.basename(img)
    label=filename.split("_")[0]
    im = np.array(Image.open(img).convert("L").resize((width,height)))
    im=im / 255
    X.append(im)# Resimler X'e
    Y.append(label)#etiketler Y'ye yani down up right 

X=np.array(X)
X=X.reshape(X.shape[0],width,height,1)
        
#sns.countplot(Y)

# onehot_labels 0,1,2 diye değerler verir

def onehot_labels(values):
    label_encoder=LabelEncoder()
    integer_encoded=label_encoder.fit_transform(values)
    onehot_encoder=OneHotEncoder(sparse=False)
    integer_encoded=integer_encoded.reshape(len(integer_encoded),1)
    onehot_encoded=onehot_encoder.fit_transform(integer_encoded)
    return onehot_encoded
    
Y=onehot_labels(Y)
train_X,test_x,train_Y,test_y=train_test_split(X,Y,test_size=0.25,random_state=2)

model=Sequential()
model.add(Conv2D(32,kernel_size=(3,3),activation="relu",input_shape=(width,height,1)))
model.add(Conv2D(64,kernel_size=(3,3),activation="relu"))
model.add(MaxPool2D(pool_size=(2,2)))
model.add(Dropout(0.25))
model.add(Flatten())
model.add(Dense(128,activation="relu"))

model.add(Dropout(0.4))
model.add(Dense(3,activation="softmax"))


  
model.compile(loss = "categorical_crossentropy", optimizer = "Adam", metrics = ["accuracy"])

#training 
model.fit(train_X,train_Y, epochs=35, batch_size=64)

score_train=model.evaluate(train_X,train_Y)
print("eğitim doğruluğu :%",score_train[1])


score_test=model.evaluate(test_x,test_y)
print("Test doğruluğu :%",score_test[1]*100)

open("model_new1.json","w").write(model.to_json())
model.save_weights("trex_weight1_new.h5")    



