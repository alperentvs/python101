sayilar = [1,5,8,9,3,45,77]
harfler = ['a','b','e','s','a','y']

sonuc = min(sayilar) #Listedeki elemanlar arasindan en kucuk elemanı sonuc degerine atar
sonuc = max(sayilar) #Listedeki elemanlar arasindan en buyuk elemanı sonuc degerine atar
sonuc = min(harfler) #Listedeki harfler arasindan alfabetik olarak en kucuk elemanı sonuc degerine atar  
sonuc = max(harfler) #Listedeki harfler arasindan alfabetik olarak en buyuk elemanı sonuc degerine atar

# EKLEME
sayilar.append(10) #Listenin sonuna 10 degerini listeye ekler
sayilar.insert(3,5) #Listenin 3 numarali indekse 5 degerini ekler
sayilar.insert(len(sayilar),150) #Listenin sonuna 150 degerini ekler

# SILME
sayilar.pop() #Listenin sonundan 1 eleman siler
sayilar.pop(3) #Listenin 3 numarali indeksindeki degeri siler
sayilar.remove(45) #Listedeki 45 degerini siler
harfler.remove('y') #Listedeki 'y' degerini siler

# SIRALAMA
sayilar.sort() #Listedeki elemanlari kucukten buyuge siralar
harfler.sort() #Listedeki elemanlari alfabetik siralar
sayilar.reverse() #Listedeki elemanlari ters cevirerek siralar

print(sayilar.count(5)) #Listede kac tane 5 degeri var?
print(harfler.count('a')) #Listede kac tane 'a' degeri var?
print(sayilar.index(5)) #Listede 5 degeri hangi indekste tutuluyor?
sayilar.clear() #Listedeki butun degerleri siler.

sonuc = sayilar
sonuc2 = harfler

print(sonuc)
print(sonuc2)