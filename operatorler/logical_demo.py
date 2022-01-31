# 1- Girilen bir sayının 50-100 arasında olup olmadigini kontrol ediniz.

sayi = (int)(input("Sayiyi giriniz: "))
sonuc = (sayi > 50) and (sayi <=100)
print(f"{sayi} sayisi 50 ile 100 arasindadir: {sonuc}")

# 2- Girilen sayinin pozitif mi tek mi olup olmadigini kontrol ediniz.
sayi = int(input('sayi: '))
sonuc = (sayi > 0) and (sayi %2 == 1)
print('girilen sayi pozitif tek sayidir: ', sonuc)

# 3- Username ve parola bilgileri ile giris kontrolu yapınız.
_username = "alperentvs"
_password = "1234"

girilenUsername = input('username: ')
girilenPassword = input('parola: ')

sonuc = (girilenUsername == _username) and (girilenPassword == _password)
print('girilen username ve parola dogru: ', sonuc)

# 4- Girilen 3 sayiyi buyukluk olarak karsilastiriniz.
x = int(input('x: '))
y = int(input('y: '))
z = int(input('z: '))

sonuc = (x>y) and (x>z) # x en buyuk
print("x en buyuk sayi: ", sonuc)

sonuc = (y>x) and (y>z) # y en buyuk
print("y en buyuk sayi: ", sonuc)

sonuc = (z>x) and (z>y) # z en buyuk
print("z en buyuk sayi: ", sonuc)

# 5- Kullanicidan 2 vize (%60) ve final (%40) notunu alip ortalama hesaplayiniz.
#    Eger ortalama 50 ve ustundeyse gecti, degilse kaldi yazdirin
#    a-) Ortalama 50 olsa bile final notu en az 50 olmalidir
#    b-) Finalden 70 alindiginda ortalamanin onemi olmasin

vize1 = float(input('vize 1: '))
vize2 = float(input('vize 2: '))
final = float(input('final: '))

ortalama = (((vize1 + vize2) / 2) * 0.4) + (final * 0.6)
sonuc = ortalama>=50
sonuc = (ortalama >= 50) or (final>=50)

print(f"ogrencinin not ortalamasi {ortalama} ve gecme durumu: {sonuc}")

# 6- Kisinin ad, kilo ve boy bilgilerini alip kilo indekslerini hesaplayiniz.
#    Formul: (Kilo / boy uzunlugunun karesi)
#    Asagidaki tabloya göre kisi hangi gruba girmektedir
#    0-18.4     => Zayif
#    18.5-24.9  => Normal
#    25.0-29.9  => Fazla Kilolu
#    30.0-34.9  => Sisman (Obez)

ad = input('adiniz: ')
kg = float(input('kilonuz: '))
hg = float(input('boyunuz: '))

kiloIndeks = kg / (hg ** 2)

zayif = (kiloIndeks >= 0) and (kiloIndeks <=18.4)
normal = (kiloIndeks >= 18.4) and (kiloIndeks <=24.9)
kilolu = (kiloIndeks >= 24.9) and (kiloIndeks <=29.9)
obez = (kiloIndeks >= 29.9) and (kiloIndeks <=34.9)

print(f"{ad} kilo indeksin: {kiloIndeks} ve kilo degerlendirmen zayif: {zayif}")
print(f"{ad} kilo indeksin: {kiloIndeks} ve kilo degerlendirmen normal: {normal}")
print(f"{ad} kilo indeksin: {kiloIndeks} ve kilo degerlendirmen kilolu: {kilolu}")
print(f"{ad} kilo indeksin: {kiloIndeks} ve kilo degerlendirmen obez: {obez}")