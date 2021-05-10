#Print() Fonksiyonu
#Kodlarımızı dosyalara yazdığımızda, eğer ekrana bir değer bastırmak istersek print fonksiyonunu kullanırız. Kullanımı oldukça basittir ve değişik özelliklere sahiptir.
print(45)
print(3.14)

a = 4
b = 3
print(a+b)

#String, Türkçe'de metin diye adlandırılan veri tipidir. Bilgisayara giriş ve çıkışlar karekter dizileri biçimindedir.
#Python’da string değişkenleri tırnak (‘) karakteri yardımıyla oluşturulur. String oluşturmak için tek tırnak (‘ ‘) veya çift tırnak (” “) kullanılabilir.
print('Alperen Tavas')
print("Alperen Tavas")
print("Alperen","Tavas")

#\n karakteri: Eğer print() fonksiyonu stringlerde böyle bir karakterle karşılaşırsa alt satırdan ekrana yazdırma işlemine devam eder. 
print("Merhaba\nBen\nAlperen Tavas")

#\t karakteri: Eğer print() fonksiyonu stringlerde böyle bir karakterle karşılaşırsa bir tab boşluk bırakarak ekrana yazdırma işlemine devam eder.
print("Pazartesi\tSalı\tÇarşamba")

#type() fonksiyonu: İçine gönderilen değerin hangi veri tipinden olduğunu söyler.
c=45
print(type(a))

d="Alperen"
print(type(d))

#Yorum satırları programlarımıza açıklama olarak eklediğimiz satırlardır. Eğer bir programda yorum satırları kullanılmışsa bu satırlar Python tarafından görülmez ve çalıştırılmaz.
#Python dilinde yorum satırları '#' karakteriyle başlar.