"""
www.patika.dev 
Python Temel eğitimi Proje ji olarak hazırlandı 
Özdemir Demiröz
"""

liste = [[1,'a',['cat'],2],[[[3]],'dog'],4,5]   #düzleşecek liste  

def flat(liste):
    x=0
    while True :                                #liste eleman sayısı artık artmayacak duruma kadar kaçışacak 
      liste_flat = []                           #düzleştirilmiş liste için boş liste oluşturuldu. elemanlar buna ekleecek
      for i in liste:                           #orjinal listedeki her bir eleman için döngü
        if type(i)==type(liste) :               #bakılan elemanın tipi list ise 
          for y in i:                           #bunun elemanlarını düzelşmişe ekle
            liste_flat.append(y)
        else:
          liste_flat.append(i)                  #bakılan eleman tipi list değilse bu bakılan elemanı flat a ekle
      liste=liste_flat.copy()                   #tekrar baştan kpntrol için , kontrol edilecek listeyi düzleşmişin kopyası yap
      x+=1                                      #döngüyü 1 arttır
      if x>len(liste):                          #eğer döngü sayısı listenin eleman sayısından fazla ise artık başka katman kalmamıştır , çık
        break
    return liste_flat

print(f"orjinal liste \t\t {liste}")
print(f"düzleştirilmiş liste {flat(liste)}")


liste2=[[1, 2], [3, 4], [5, 6, 7]]              #tersine çevrilecek liste
    
def ters(liste2):
  liste2.reverse()                              #listeyi ters çeviriyoruz
  for a in liste2:
    if  type(a)==list:                          #liste içindeki elemanlarda list  tipi varsa 
      a.reverse()                               #bunları da tersine çeviriyoruz 
  return liste2

print(f"orjinal liste \t\t {liste2}")
print(f"tersine liste \t\t {ters(liste2)}")