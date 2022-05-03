import numpy as np
import cv2
import os 
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix
import seaborn as sns
import matplotlib.pyplot as plt
from keras.models import Sequential
from keras.layers import Dense, Conv2D, MaxPooling2D, Flatten, Dropout, BatchNormalization
from keras.preprocessing.image import ImageDataGenerator
from tensorflow.keras.utils import to_categorical
import pickle


path="Meyve"
liste=os.listdir(path)



images=[]
classNo=[]



    
for k in  range(len(liste)):
    print(liste[k]," hangi dosya")
    MeyveIsimList = os.listdir(path+"\\"+liste[k])
    for i in range(len(MeyveIsimList)):
        print(MeyveIsimList[i]+" hangi dosya")
        MeyveResimList = os.listdir(path+"\\"+liste[k]+"\\"+MeyveIsimList[i])
        for j in MeyveResimList:
            img = cv2.imread(path+"\\"+liste[k]+"\\"+MeyveIsimList[i]+"\\"+j)
            img = cv2.resize(img, (32,32))
            images.append(img)
            classNo.append(i)
    

images = np.array(images)
classNo = np.array(classNo)

x_train, x_test, y_train, y_test = train_test_split(images, classNo, test_size = 0.5, random_state = 42)
x_train, x_validation, y_train, y_validation = train_test_split(x_train, y_train, test_size = 0.2, random_state = 42)

print(images.shape)
print(x_train.shape)
print(x_test.shape)
print(x_validation.shape)


# vis 
"""
fig, axes = plt.subplots(3,1,figsize=(7,7))
fig.subplots_adjust(hspace = 0.5)
sns.countplot(y_train, ax = axes[0])
axes[0].set_title("y_train")

sns.countplot(y_test, ax = axes[1])
axes[1].set_title("y_test")

sns.countplot(y_validation, ax = axes[2])
axes[2].set_title("y_validation")
"""

def preProcess(img):
    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    img = cv2.equalizeHist(img)
    img = img /255
    
    return img

""" 
img=preProcess(x_train[100])
img=cv2.resize(img,(300,300))
cv2.imshow("fonksiyon",img)
"""
#preProcess her yere uygulicaz
x_train=np.array(list(map(preProcess,x_train)))
x_test=np.array(list(map(preProcess,x_test)))
x_validation=np.array(list(map(preProcess,x_validation)))

x_train = x_train.reshape(-1,32,32,1)
x_test = x_test.reshape(-1,32,32,1)
x_validation = x_validation.reshape(-1,32,32,1)

#yakınlaştırma uzaklaştırma
dataGen=ImageDataGenerator(width_shift_range=0.1,
                           height_shift_range=0.1,
                           zoom_range=0.1,
                           rotation_range=10)

dataGen.fit(x_train)

y_train=to_categorical(y_train,24)
y_test=to_categorical(y_test,24)
y_validation=to_categorical(y_validation,24)


#Model

model = Sequential()
model.add(Conv2D(input_shape = (32,32,1), filters = 8, kernel_size = (5,5), activation = "relu", padding = "same"))
model.add(MaxPooling2D(pool_size = (2,2)))

model.add(Conv2D( filters = 16, kernel_size = (3,3), activation = "relu", padding = "same"))
model.add(MaxPooling2D(pool_size = (2,2)))

model.add(Dropout(0.2))
model.add(Flatten())
model.add(Dense(units=256, activation = "relu" ))
model.add(Dropout(0.2))
model.add(Dense(units=24, activation = "softmax" ))

model.compile(loss = "categorical_crossentropy", optimizer=("Adam"), metrics = ["accuracy"])

batch_size = 250

hist = model.fit_generator(dataGen.flow(x_train, y_train, batch_size = batch_size), 
                                        validation_data = (x_validation, y_validation),
                                        epochs = 15,steps_per_epoch = x_train.shape[0]//batch_size, shuffle = 1)


open("model_new1.json","w").write(model.to_json())
model.save_weights("meyve_weight1_new.h5")    
# %% degerlendirme
hist.history.keys()


plt.figure()
plt.plot(hist.history["loss"], label = "Eğitim Loss")
plt.plot(hist.history["val_loss"], label = "Val Loss")
plt.legend()
plt.show()

plt.figure()
plt.plot(hist.history["accuracy"], label = "Eğitim accuracy")
plt.plot(hist.history["val_accuracy"], label = "Val accuracy")
plt.legend()
plt.show()


score = model.evaluate(x_test, y_test, verbose = 1)
print("Test loss: ", score[0])
print("Test accuracy: ", score[1])


y_pred = model.predict(x_validation)
y_pred_class = np.argmax(y_pred, axis = 1)
Y_true = np.argmax(y_validation, axis = 1)
cm = confusion_matrix(Y_true, y_pred_class)
f, ax = plt.subplots(figsize=(8,8))
sns.heatmap(cm, annot = True, linewidths = 0.01, cmap = "Greens", linecolor = "gray", fmt = ".1f", ax=ax)
plt.xlabel("predicted")
plt.ylabel("true")
plt.title("cm")
plt.show()
