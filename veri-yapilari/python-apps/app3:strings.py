website = "http://www.alperentavas.com"
kursAdi = "Python Dersleri: Sıfırdan İleri Seviye Python Programlama."

# 1- 'kursAdi' karakter dizisinde kaç karakter bulunmaktadır?
sonuc = len(website)
sonuc = len(kursAdi)

# 2- 'website' içinden www karakterlerini alın.
sonuc = website[7:10]
# 3- 'website' içinden com karakterini alın.
karakterSayisi = len(website)
sonuc = website[karakterSayisi-3:karakterSayisi]

# 4- 'kursAdi' içinden ilk 15 ve son 15 karakterlerini alın.
sonuc = kursAdi[0:15]
sonuc = kursAdi[:15]
sonuc = kursAdi[-15:]

# 5- 'kursAdi' içerisindeki karakterleri tersten yazdırın.
sonuc = kursAdi[::-1]

# 6- 'Hello world' ifadesindeki w harfini 'W' ile değiştirin.
s = 'Hello world'
s = s[0:6] + 'W' + s[-4:]
print(s)

# 7- 'abc' ifadesini yan yana 3 defa yazdırın.
print('abc ' * 3)


name, surname, age, job = 'Alperen', 'Tavas', 23, 'öğrenci'
# 8- Yukarıda verilen değişkelbker ile ekrana aşağıdaki ifadeyi yazdırın.
# 'Benim adım Alperen Tavas, Yaşım 23 ve mesleğim mühendis. '
sonuc = "Benim adım " + name + " " + surname + ", Yaşım " + str(age) + " ve mesleğim " + job + "."
sonuc = "Benim adım {0} {1}, Yaşım {2} ve mesleğim {3}".format(name,surname,age,job)
sonuc = f"Benim adım {name} {surname}, Yaşım {age} ve mesleğim {job}"
print(sonuc)