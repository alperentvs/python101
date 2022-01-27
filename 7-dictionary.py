#Sözlükler aynı gerçek hayattaki gibi davranan veritipidir. Sözlüğün içindeki her bir eleman indeks ile değil, anahtar(key), değer(value) olarak tutulur. 

#Sözlük oluşturmak: 
sozluk1 = {"sıfır":0,"bir":1,"iki":2}
a = {"bir" : [1,2,3,4], "iki": [[1,2],[3,4],[5,6]],"üç" : 15}
b = {"sayılar":{"bir":1,"iki":2,"üç":3},"meyveler":{"kiraz":"yaz","portakal":"kış","erik":"yaz"}}
print(sozluk1,a,b)

#Boş sözlük:
sozluk2 = {}
sozluk2 = dict()

#Sözlük Değerlerine Erişmek ve Sçzlüğe Değer Eklemek:
sozluk1["bir"]
print(sozluk1["bir"])    #"bir" anahtarına karşılık gelen değer

sozluk1["beş"] = 5
print(sozluk1["beş"])    #yeni değer eklemek

print(a["iki"])
print(a["iki"][1][1])
print(b["meyveler"]["kiraz"])

#Temel Sözlük Metodları:
yeni_sozluk = {"bir":1,"iki":2,"üç":3}

print(yeni_sozluk.values())    #values() metodu sözlüğün değerlerini bir liste olarak döner
print(yeni_sozluk.keys())      #keys() metodu sözlüğün anahtarlarını bir liste olarak döner 
print(yeni_sozluk.items())     #items() metodu sözlüğün anahtar ve değerlerini bir liste içinde demet olarak döner

# ORNEK (JSON FORMAT)
ogrenciler = {
    100: {
        "ad": "Cinar",
        "soyad": "Bilgi",
        "yas": 5,
        "notlar": [70,80,95]
    },
    101: {
        "ad": "Ada",
        "soyad": "Turan",
        "yas": 10
    }
}

sonuc = ogrenciler[100]
sonuc = ogrenciler[100]["ad"]
sonuc = ogrenciler[100]["notlar"][0]

print(sonuc)