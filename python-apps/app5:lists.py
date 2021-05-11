# 1- "Iphone6,Iphone7,Iphone8,Iphone11" elemanlarına sahip bir liste oluşturunuz.
telefonlar = ["Iphone6","Iphone7","Iphone8","Iphone11"]

# 2- Liste kaç elemanlıdır?
sonuc = len(telefonlar)

# 3- Listenin ilk ve son elemanı nedir?
sonuc = telefonlar[0]
sonuc = telefonlar[-1]

# 4- "Iphone7" değerini "Iphone7 Plus" ile değiştirin.
telefonlar[1] = "Iphone7 Plus"
sonuc = telefonlar

# 5- "Iphone6" listenin bir elemanı mıdır?
if "Iphone6" in telefonlar:
    print("Iphone6 liste içinde var")

# 6- Listenin -3 indeksindeki değer nedir?
sonuc = telefonlar[-3]

# 7- Listenin ilk 2 elamanını alın.
sonuc = telefonlar[:2]

# 8- Listenin son 2 elemanı yerine "IphoneXR" ve "Iphone12" değerlerini ekleyin.
telefonlar[-2:] = ["IphoneXR","Iphone12"]
sonuc = telefonlar

# 9- Listenin üzerine "Samsung S10" ve "Samsung Note10" ekleyin.
sonuc = telefonlar + ["Samsung10","Samsung Note10"]

# 10- Listenin son elemanını silin.
del telefonlar[-1]
sonuc = telefonlar

# 11- Liste elemanlarını tersten yazdırınız.
sonuc = telefonlar[::-1]

# 12- Aşağıdaki verileri bir liste içinde saklayınız.

        # kullaniciA: Yiğit Bilgi 2010, (70,60,70)
        # kullaniciB: Sena Turan  1999, (80,80,70)
        # kullaniciC: Ahmet Turan 1998, (80,70,90)

ogrenciA = ["Yiğit","Bilgi",2010,[70,60,70]]
ogrenciB = ["Sena","Turan",1999,[80,80,70]]
ogrenciC = ["Ahmet","Turan",1998,[80,70,90]]

ogrenciler = [ogrenciA,ogrenciB,ogrenciC]

for ogrenci in ogrenciler:
    print(ogrenci)

# 13- Liste elemanlarını ekrana yazdırın.
for a in telefonlar:
    print(a)

print(sonuc)