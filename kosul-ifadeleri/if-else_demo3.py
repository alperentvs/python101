# 1- Kullanicidan isim, yaş ve eğitim bilgilerini isteyip ehliyet alabilme durumunu kontrol ediniz. 
# Ehliyet alma koşulu en az 18 ve eğitim durumu lise ya da üniversite olmalidir. 

isim = input('isim: ')
yas = int(input('yaş: '))
egitim = input('eğitim: ')

if (yas >= 18):
    if (egitim == 'lise' or egitim == 'üniversite'):
        print('ehliyet alabilirsiniz.')
    else:
        print(f'{isim} ehliyet alamazsiniz çünkü eğitim durumu yetersiz.')
else:
    print(f'{isim} ehliyet alamazsiniz çünkü yaşiniz tutmuyor.')


# 2- Bir öğrencinin 2 yazili bir sözlü notunu alip hesaplanan ortalamaya göre not araliğina karşilik 
# gelen not bilgisini yazdiriniz.
#    0 -24  => 0
#    25-44  => 1
#    45-54  => 2
#    55-69  => 3
#    70-84  => 4
#    85-100 => 5

yazili1 = float(input('1.yazili: '))
yazili2 = float(input('2.yazili: '))
sozlu = float(input('sözlü: '))

ortalama = (yazili1 + yazili2 + sozlu) / 3

if(ortalama >= 0) and (ortalama < 25):
    print(f'ortalamaniz: {ortalama} ve notunuz: 0')
elif (ortalama >= 25) and (ortalama<45):
    print(f'ortalamaniz: {ortalama} ve notunuz: 1')
elif (ortalama >= 45) and (ortalama<55):
    print(f'ortalamaniz: {ortalama} ve notunuz: 2')
elif (ortalama >= 55) and (ortalama<70):
    print(f'ortalamaniz: {ortalama} ve notunuz: 3')
elif (ortalama >= 70) and (ortalama<85):
    print(f'ortalamaniz: {ortalama} ve notunuz: 4')
elif (ortalama >= 85) and (ortalama<=100):
    print(f'ortalamaniz: {ortalama} ve notunuz: 5')
else:
    print('yanliş bilgi girdiniz.')



# 3- Trafiğe çikiş tarihi alinan bir aracin servis zamanini aşağidaki bilgilere göre hesaplayiniz.
#    1. Bakim => 1. yil     
#    2. Bakim => 2. yil      
#    3. Bakim => 3. yil     
#    ** Süre hesabini alinan gün, ay, yil bilgisine göre gün bazli hesaplayiniz..
#    *** datetime modülünü kullanmaniz gerekiyor.  
#    (simdi) - (2018/8/1) => gün

import datetime

tarih = input('araciniz hangi tarihte trafiğe çikti (2019/7/11)')
tarih = tarih.split('/') # Listeyi '/' ile ayırır

simdi = datetime.datetime.now()
trafigeCikis = datetime.datetime(int(tarih[0]),int(tarih[1]),int(tarih[2]))

fark = simdi - trafigeCikis
gun = fark.days

print(gun)

if (gun<= 365):
    print('1.servis bakimi.')
elif (gun>365) and (gun<=365*2):
    print('2.servis bakimi')
elif (gun>=365*2) and (gun<=365*3):
    print('3.servis bakimi')
else:
    print('hatali bilgi girdiniz.')