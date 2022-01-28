#Listeler, tek bir değişkende birden çok öğeyi depolamak için kullanılır.
#Bir listede her veritipinden elemanı saklayabiliriz.
#Listeler köşeli parantez kullanılarak oluşturulur:
thislist = ["elma","armut",34,2.14]
print(thislist)

#Boş liste:
bos_liste = []
print(bos_liste)

bos_liste2 = list()
print(bos_liste2)

#len fonksiyonu listeler üstünde de kullanılabilir.
liste2 = [1,2,3,4,5,6,7]
print(len(liste2))

#Listeleri indeksleme ve parçalara ayırma:
liste3 = [5,21,543,65,567,234]
print(liste3[0])    # 0. eleman
print(liste3[3])    # 3. eleman (0 dan başladığı unutulmamalı..)
print(liste3[-1])   # En son elemanı gösterir
print(liste3[:4])   # Baştan 4. elemana kadar gösterir.
print(liste3[1:4])  # 1. değerden 4. değere kadar (dahil değil)
print(liste3[2:])   # 2. değer ve sonrası
print(liste3[::2])  # 2 değer atlayarak gösterir
print(liste3[::-1]) # Tersten sıralamaya başlar

#Listeler birbirleri ile toplanabilirler:
list_top = liste2 +liste3
print(list_top)

#Listelere eleman eklemek için: 
liste2 = liste2 + ["Sayilar"]
print(liste2)

#Liste elemanları doğrudan değiştirilebilir:
liste2[2] = "yeni eklenen değer" #Liste2'nin 2. indeksini değiştirdim. 
print(liste2)

#Listeleri tam sayılarla çarpabiliriz:
list_carp = liste3 * 2
print(list_carp)

#sort metodu küçükten büyüğe sıralama yapar:
print(sorted(liste3))

#İç içe listeler
list_icice = [liste2,liste3]
print(list_icice[1][0]) #liste3'ün ilk elemanı

#if blogu=> Koşul ifadeleri
if "elma" in thislist:
  print("deger listenin bir elemani")
  
#donguler=>listenin elemanlarini yazdirma
for x in thislist:
  print(x)
  
#Listeden veri silme
del thislist[1]
