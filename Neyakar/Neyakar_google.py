import requests 
import polyline #koordinat noktalarını işleyebilmek için 
import tkinter as tk
from geopy.distance import distance #koordinat noktalarından toplam mesafe hesaplaması için 
import tkinter as tk
import tkintermapview #google haritaları göstermek için 

api_key = "" # BURAYA GOOGLE DAN ALINAN API KEY GİRİLECEK

root = tk.Tk()

hesap_label = tk.Label(root, text="Hesaplama")
hesap_label.pack()

map_widget = tkintermapview.TkinterMapView(root, width=800, height=600, corner_radius=0)
map_widget.pack()

nerden_label = tk.Label(root, text="Nerden : ")
nerden_label.pack()
nerden_box = tk.Entry(root)
nerden_box.pack()

nereye_label = tk.Label(root, text="Nereye : ")
nereye_label.pack()
nereye_box = tk.Entry(root,)
nereye_box.pack()

tuketim_label = tk.Label(root, text="Lt Tüketim/100km : ")
tuketim_label.pack()
tuketim_box = tk.Entry(root,)
tuketim_box.pack()

fiyat_label = tk.Label(root, text="Lt fitatı : ")
fiyat_label.pack()
fiyat_box = tk.Entry(root)
fiyat_box.pack()

#düğmeye basılınca bu fonk. çağırılacak
def hesapla_ciz():
    #hesaplama düğmesine basıldığında haritayı temizlemek için 
    map_widget.delete_all_path()

    nerden = str(nerden_box.get())
    nereye = str(nereye_box.get())
    tuketim100 = float(tuketim_box.get())
    yakıtLt= float(fiyat_box.get())

    #google dan alınan API key gerekli " Directions API "
    
    url = f"https://maps.googleapis.com/maps/api/directions/json?origin={nerden}&destination={nereye}&key={api_key}"

    response = requests.request("GET",url)
    data = response.json()
    rota = data["routes"][0]["overview_polyline"]["points"]
    koordinatlar = polyline.decode(rota)

    # yolun çizdirilmesi
    map_widget.set_path(koordinatlar)

    #gösterilecek harita için koordinatların belirlenmesi . koordinat listesindeki ilk (başlangıç ) ve son değer (varış) alınıyor
    lat1 = koordinatlar[0][0]
    long1 = koordinatlar[0][1]
    lat2 = koordinatlar[-1][0]
    long2 = koordinatlar[-1][1]

    condi1 =(lat2>lat1)and(long1>long2)
    condi2 = (lat2>lat1)and(long2>long1)
    condi3 = (lat1>lat2)and(long2>long1)
    condi4= (lat1>lat2)and(long1>long2)
    # haritanın bu yola göre gösterilmesi ,  herzaman  fit_bounding_box((solüst),(sağalt)) koordinatlar verilmeli
    # başlangıç bitiş noktasına göre if ler ile bu harita sol üst ve sağ alt koordinatları seçiliyor
    if condi1:
        map_widget.fit_bounding_box((lat2,long2),(lat1,long1))
    elif condi3:
        map_widget.fit_bounding_box((lat1,long1),(lat2,long2))
    elif condi2:
        map_widget.fit_bounding_box((lat2,long1),(lat1,long2))
    else:
        map_widget.fit_bounding_box((lat1,long2),(lat2,long1))

# mesafe hesaplama
    toplam_mesafe = 0
    
    for i in range(len(koordinatlar)-1):
        start = koordinatlar[i]
        end = koordinatlar[i+1]
        toplam_mesafe += distance(start, end).km
    
    toptuketim = (toplam_mesafe*tuketim100)/100
    yakmasrafi = toptuketim*yakıtLt

    hesap_label.config(text=f"Toplam mesafe: {toplam_mesafe:.2f} km \n Toplam tüketim: {toptuketim:.2f}lt \n Toplam Yakıt Masrafı:{yakmasrafi:.2f}  ")

# hesapla düğmesi
hesapla_button = tk.Button(root, text="hesapla", command=hesapla_ciz)
hesapla_button.pack()


root.mainloop()