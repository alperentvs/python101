# sets => indekslenemez, siralanamazlar ve guncellenemezler ama yeni bilgi ekleyebiliriz.
# Sirasi bizim icin önemli degilse, indeksleme onemli degilse, uzerine bir eleman eklemek istiyorsak
# fakat var olani degistermek istemiyorsak bu durumda setleri kullanabiliriz
# Tuple ile farkı eleman eklemektir 

meyveler = {"elma","kiraz","kavun","uzum"}
sebzeler = {"bezelye","sogan"}

# sonuc = meyveler[0] #Indekslenemedigi icin hata aliriz

sonuc = "elma" in meyveler #meyveler icinde elma var mi? 
meyveler.add("karpuz") #karpuz ogesini ekledik
meyveler.update(["visne","muz"]) #birden fazla oge eklemek istersek

sonuc = len(meyveler) #uzunlugunu bulabiliriz
meyveler.remove("karpuz") #karpuz ogesini silebiliriz

sonuc = meyveler.union(sebzeler) #Liste elemanlari birlestirilir
sonuc = meyveler

for x in meyveler:
    print(x)

print(sonuc)