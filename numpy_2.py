import pandas as pd
import numpy as np
pd.Series([10, 20, 30, 40, 50]) # verilen liste ile bir seri oluşturuldu

data = np.array([10, 20, 30, 40, 50]) #numpy ile bir array oluşturuldu 
seri = pd.Series(data)                  #pandas daki seri oluşturmak için bu array kullanıldı
print(f"seri : \n{seri}\n")

# data = np.array([10, 20, 30, 40, 50])
seri = pd.Series(data, index = [100, 101, 102, 103, 104]) # pandas seriyi oluştururken hangi indekslere koyacağımızı seçebiliyoruz
print(f"seri : \n{seri}\n")

data = {'a': 0, 'b': 1, 'c': 2}
seri = pd.Series(data)                  #data dixtionry olarak verildi 
print(f"seri : \n{seri}\n")

print(seri[0]) #seri deki index=0 ı göster

print(seri[0:2])#index=0 dan başla iki eleman göster

print(seri['b']) # dictionary deki 'b' key ine düşen değeri gösterir

seri['a'] = 90 #a key ine düşen değeri 90 a eşitlerik
print(seri)

print(seri.sum()) #serideki değerleri topladık 

print(seri.max()) #serideki max değeri gösterdik

print(seri.mean()) #değerlerin ortalaması

print(seri.median()) #medyan bulundu (orta değer)