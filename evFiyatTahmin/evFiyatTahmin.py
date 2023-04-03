import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
import seaborn as sns
import matplotlib.pyplot as plt

# pandas ile csv den dataframe e atıyoruz . 
#normalde csv ler "," ile ayrılır fakat bunda ";" olduğundan sep=";" ile ayrımı belirtiyoruz
df=pd.read_csv("kendi-kendine/evFiyatTahmin/ev_fiyat_tahmini.csv",sep=";") 


#linner regresyon modeli x bağımsız değişkeni nin  y bağımlı değişkeni üzerindeki etkisini açıklayan bir doğrusal denklemdir. 
# verilerin doğru şekilde işlenebilmesi için LinearRegression() sütun kabul etmektedir. bu yüzden alttaki gibi veriler tek sütun vektörü olarak şeküllendirmek gerekiyor.
# .values --> pandas olan veriyi ( df ) tek sütun bir Numpy dizisine döndürür
# .reshape --> tekrar şekillendirir. -1 verdiğimiz için satır sayısı otomatik , sütun sayısı ise 1 olarak tanımlanır . tek sütunluk bir numpy dizisine dönüştü
#x ,y = df['MetreKare'].values.reshape((-1, 1)) , df['fiyatlar'].values.reshape((-1, 1)) #x değişkenimizi csv nin "MetreKare" kolonundan , y yi "fiyatlar" dan alıyoruz
x=df['MetreKare'].to_numpy().reshape((-1, 1))
y=df['fiyatlar'].to_numpy().reshape((-1, 1))
#-------------------------------------------------------------------------------------------------------------------------------------------------------------------

#tahmin modeli nesnesini LinearRegression() foksiyonundan oluşturup modeli eğitmek için  .fit() metodunu kullanıyoruz
tahminModeli = LinearRegression() 
tahminModeli.fit(x,y)


#plotları çizdiriyoruz , çizdirmesk de olur , zaten model bunlardan bağımsız olarak oluşturuldu . 
#cizdirmek bize görsel olarak bir çıktı veriyor ve veriyi görselleştirip anlamamızı sağlıyor .

sns.regplot(x="MetreKare", y="fiyatlar", data=df,line_kws={"color": "red"}) 
plt.xlabel("m" + "\u00B2")
plt.ylabel("Fiyat")
plt.show()

#predict() ile eğitilen model için tahmin alabiliyoruz.
M2 = int(input ("Fiyat tahmini istediğiniz m\u00B2 yi giriniz :  "))
tahminiFiyat = tahminModeli.predict([[M2]])[0][0]  # 2AD array istediği için  [[]] kullandık ve sonucu için ilk satırdaki ilk sütüundaki değeri aldık .
dogruluk = tahminModeli.score(x,y) # doğruluk skoru 
print(f"{M2} m\u00B2 için Fiyat %{dogruluk:.2f} doğruluk ile {tahminiFiyat:.2f} dir.")#  :.2f  virgülden sonra iki rakamı göstermek için 


