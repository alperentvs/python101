#int: Tam sayıları ifade eder 32 bit,± 2147483647 örnek olarak 105 tam sayısını gösterebiliriz.
#float: veri tipi ondalıklı bir gerçek sayıyı ifade eder. 64 bit uzunluğa ve hassasiyete sahiptir. Örnek olarak 3.14159 rakamını paylaşabiliriz.

#Toplama İşlemi(+)
print(3+9)

#Çıkarma İşlemi(-)
print(9-3)

#Çarpma İşlemi(*)
print(9*3)

#Bölme İşlemi(/)
print(9/3)

#Tam Sayı Bölmesi(//)
print(22//3)

#Kalan Bulma(%)
print(18%5)

#Üs Bulma(**)
print(2**3)

#Değişkenler ve Değişken Tanımlama: Değişkenler aslında bir veri tipinden değer tutan birimlerdir.
pi = 3.14
print(pi)

a=3
b=5
c=a+2*b
print(c)

#1.Değişken isimleri bir sayı ile başlayamaz.
#2. Değişken ismi kelimelerden oluşuyorsa aralarında boşluk olamaz.
#3. :'",<>/?|\()!@#$%^&*~-+ Buradaki semboller değişken ismi içinde kullanılamaz.(Sadece "_" sembolü kullanılabilir)
#4. Pythonda tanımlı anahtar kelimeler değişken ismi olarak kullanılamaz.(while, not vs.)

#Python'da iki değişkenin değerini birbiriyle değiştirmek için pratik bir yöntem bulunmaktadır.
d=1
e=2
d,e=e,d
print(d,e)

#Pratik:
f=2
f += 1
print(f)