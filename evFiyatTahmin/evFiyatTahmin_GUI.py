import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
import seaborn as sns
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
from matplotlib.figure import Figure
from sklearn.preprocessing import normalize


import tkinter
import tkinter.messagebox

# pandas ile csv den dataframe e atıyoruz . 
#normalde csv ler "," ile ayrılır fakat bunda ";" olduğundan sep=";" ile ayrımı belirtiyoruz
df=pd.read_csv("kendi-kendine/evFiyatTahmin/ev_fiyat_tahmini.csv",sep=";") 
#-------------------------------------------------------------------------------------------------------------------------------------------------------------------

#linner regresyon modeli x bağımsız değişkeni nin  y bağımlı değişkeni üzerindeki etkisini açıklayan bir doğrusal denklemdir. 
# verilerin doğru şekilde işlenebilmesi için LinearRegression() sütun kabul etmektedir. bu yüzden alttaki gibi veriler tek sütun vektörü olarak şeküllendirmek gerekiyor.
# # values yerine to_numpy() metodunun kullanılması öneriliyor.veriyi ( df ) tek satırlık bir Numpy dizisine döndürür.
# .reshape --> tekrar şekillendirir. -1 verdiğimiz için satır sayısı otomatik , sütun sayısı ise 1 olarak tanımlanır . tek satırlık bir diziden , tek sütun bir numpy dizisine dönüştü
#x değişkenimizi csv nin "MetreKare" kolonundan , y yi "fiyatlar" dan alıyoruz
x ,y =df['MetreKare'].to_numpy().reshape((-1,1)) ,df['fiyatlar'].to_numpy().reshape((-1,1))
#-------------------------------------------------------------------------------------------------------------------------------------------------------------------

#tahmin modeli nesnesini LinearRegression() foksiyonundan oluşturup modeli eğitmek için  .fit() metodunu kullanıyoruz
tahminModeli = LinearRegression() 
tahminModeli.fit(x,y)
#-------------------------------------------------------------------------------------------------------------------------------------------------------------------

#predict() ile eğitilen model için tahmin alabiliyoruz.
def predict_price(value):
    return tahminModeli.predict([[value]])[0][0]# 2D array istediği için  [[]] kullandık ve sonucu için ilk satırdaki ilk sütüundaki değeri aldık .
#-------------------------------------------------------------------------------------------------------------------------------------------------------------------

#GUI deki düğme ile slider ın değeri alınıyor ve predict() için kullanılıyor
#tahmin edilen fiyat ve doğruluk oranı GUI deki labela yazdırılıyor
def on_button_click():
    value = slider.get()
    price = predict_price(value)
    tkinter.Label(text=f"Metrekare Fiyatı = {price:.2f} \n doğruluk oranı = {tahminModeli.score(x,y):.3f}").pack()
#-------------------------------------------------------------------------------------------------------------------------------------------------------------------

#Tkinter kısımları( pencerenin oluşturulması , düğme, slider ve grafik alanının belirlenmesi)
Anapencere = tkinter.Tk()
Anapencere.title("metrekare fiyat tahmini")

#plotları çizdiriyoruz , çizdirmesk de olur , zaten model bunlardan bağımsız olarak oluşturuldu . 
#cizdirmek bize görsel olarak bir çıktı veriyor ve veriyi görselleştirip anlamamızı sağlıyor .
grafik = sns.regplot(x="MetreKare", y="fiyatlar", color="green" , data=df,line_kws={"color": "blue"})
canvas = FigureCanvasTkAgg( grafik.figure , master=Anapencere)
canvas.draw()
canvas.get_tk_widget().pack()

slider = tkinter.Scale(Anapencere, from_=10, to=600, orient=tkinter.HORIZONTAL, length=200, resolution=5)
slider.pack()

tkinter.Button(Anapencere, text='hesapla',command=on_button_click).pack()

Anapencere.mainloop()
                     

