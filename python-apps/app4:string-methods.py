website = "http://www.alperentavas.com"
kursAdi = "Python Dersleri: Sıfırdan İleri Seviye Python Programlama."

# 1- ' Hello World ' karakter dizisinin baş ve sondaki boşluk karakterlerini silin.
sonuc = ' Hello World '.strip()     #Baştaki ve sondaki boşlukları sildi
sonuc = ' Hello World '.lstrip()    #Soldaki boşluğu sildi
sonuc = ' Hello World '.rstrip()    #Sağdaki boşluğu sildi

sonuc = website.lstrip('/:pthw.')   #Soldaki belirtilen karakterleri siler.

# 2- 'www.alperentavas.com' içindeki alperentavas haricindeki her karakteri silin.
sonuc = "www.alperentavas.com".strip('w.moc')

# 3- 'kursAdi' karakter dizisinin tüm karakterlerini küçük harf yapın. 
sonuc = kursAdi.lower()

# 4- 'website' içinde kaç tane a karakteri vardır? (count('a'))
sonuc = website.count('a')
sonuc = website.count('www')
sonuc = website.count('www',9,15)

# 5- 'website' "www" ile başlayıp "com" ile bitiyor mu?
sonuc = website.startswith('www')
sonuc = website.endswith('com')

# 6- 'website' içinde '.com' ifadesi var mı?
sonuc = website.find('com')
sonuc = website.find('com',0,10)
sonuc = kursAdi.find('Python')
sonuc = kursAdi.rfind('Python')

sonuc = kursAdi.index('Python')
sonuc = kursAdi.rindex('Python')

# 7- 'kursAdi' içindeki karakterlerin hepsi alfabetik mi? (isalpha, isdigit)
sonuc = "abc1".isalpha()
sonuc = "123".isdigit()

# 8- 'Contents' ifadesini satırda 50 karakter içine yerleştirip sağ ve soluna * ekleyiniz.
sonuc = 'Contents'.center(50,'*')
sonuc = 'Contents'.ljust(50,'*')
sonuc = 'Contents'.rjust(50,'*')

# 9- 'kursAdi' karakter dizisindeki tüm boşluk karakterlerini '-' ile değiştirin.
sonuc = kursAdi.replace('','-')

# 10 - 'Hello World' karakter dizisinin 'World' ifadesini 'There' olarak değiştirin.
sonuc = 'Hello World'.replace('World','There')

# 11- 'kursAdi' karakter dizisini boşluk karakterlerinden ayırın.
kursAdi = kursAdi.lower().replace(':','')
sonuc = kursAdi.split()
print(sonuc)