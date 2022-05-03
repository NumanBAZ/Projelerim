# -*- coding: utf-8 -*-
"""
Created on Sat Feb  5 12:39:15 2022

@author: Numan
"""

""" dosya yolu belirtme"""

dosya_yolu="klasör"+"\\"+"ismi"+"türü"

#%%Listeler
gunler= ["Pazartesi","Salı","Çarşamba","Perşembe","Cuma","Cumartesi","Pazar"]

print(gunler[-1])
print (len(gunler))
print (gunler[1:5])

gunler.append("Numan")#ekle
print(gunler)

gunler.remove("Numan")#sil
print(gunler)

gunler.reverse()#tersten
print(gunler)

gunler.sort()#küçükten büyüğe
print(gunler)

#%%Tuple


demet=(0,1,2,3,4,4,5,5,5,6)

print(demet.count(5))


nesne=(1,2,3)
x,y,z=nesne
print(x,y,z)

#%% deque

from collections import deque

dq=deque(maxlen=3)


#%% Dictionary

plaka={"İstabul":34,"İzmir":35}

print(plaka)
print(plaka.keys())
print(plaka.values())

#%% Numpy kütüphanesi


import numpy as np

dizi=np.array([1,2,3,4,5,6,7])

print(dizi.shape)


#%% Pandas Kütüphanesi



import pandas as pd

sozluk={"isim":["ali","numan"],
        "yaş":[16,20]
        }
veri=pd.DataFrame(sozluk)



#%% Matplotlib kütüphanesi

"""resimleri görseleştirmek için kullanılıyor
"""
import matplotlib.pyplot as plt
import numpy as np


x=np.array([1,2,3,4])
y=np.array([4,3,2,1])

plt.figure()
plt.plot(x,y)


