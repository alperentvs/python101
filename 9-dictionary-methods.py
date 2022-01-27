opelObj = {
    "marka": "Opel",
    "model": "Corsa",
    "yil": 2021
}

sonuc = opelObj["marka"]
sonuc = opelObj.get("marka") #Yukaridaki tanımlamayla ayni isi yapar.

# for x in opelObj:
#     print(x)

# for x in opelObj:
#     print(opelObj[x])

# for x in opelObj.values(): #Objeleri cagirir
#     print(x)

for x,y in opelObj.items(): #Objeleri ve degerleri cagirir
    print(x,y)

sonuc = "marka" in opelObj #Aradigimiz model dictionary icinde var mi?

sonuc = len(opelObj) #Kac elemanli?

opelObj["renk"] = "kirmizi" #Deger eklemek istersek

opelObj.pop("renk") #Renk bilgisini siler --> ya da del opelObj["renk"]

opelObj.popitem() #Rastgele item siler

del opelObj #opelObj ogesini tamamen siler 

opelObj.clear() #Icerindeki butun elemanlari siler

obj = opelObj #obj icerisine opelObj'yi referens olarak kopyalar
obj["marka"]= "Mazda" #Burada yapmış oldugum degisiklikler opelObj'yi de etkiler. Cunku ayni referans numarasina sahipler
obj = opelObj.copy() #Yapilan degisikliklerden opelObj etkilenmez

opelObj.update({
    "marka": "BMW",
    "renk": "Kirmizi"
})  #Update islemi yapabiliriz

# print(sonuc)
print(opelObj)