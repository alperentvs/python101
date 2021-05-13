#Demetler veya İngilizce ismiyle tuplelar listelere oldukça benzer ancak farkları demetlerin değiştirilemez oluşudur.
#Bu yüzden programlarımızda değiştirilmesini istemediğimiz değerleri bir demet içinde depolayabiliriz.

#Tuple oluşturma
demet = (1,2,3,4,5,6,7,8,9)
print(demet)
print(type(demet))

#Tek elemanla:
demetTek = (1,)
print(demetTek)
print(type(demetTek))

#index metoduyla içine verdiğimiz elemanın hangi indekste olduğunu bulabiliriz.
demetiki = (1,2,3,"Mustafa","Mert")
print(demetiki.index("Mustafa"))

#count metoduyla içine verdiğimiz değerin demette kaç defa geçtiğini bulabiliriz.
demetuc = (1,3,5,75,342,24324,5646,1,1,3,1)
print(demetuc.count(1))

#Demetleri Ne Zaman Kullanalım?
#Aslında Python programcıları demetlerden ziyade listeleri daha çok kullanır.
#Ancak eğer programınızda değiştirilmesini istemediğiniz bilgiler varsa (Android uygulama sabitleri gibi) bunları demet içinde depolayabilirsiniz.
#Aynı zamanda, Read Only(Sadece Okuma) bir veritipi olduğu için listelere göre biraz daha hızlı çalışırlar.