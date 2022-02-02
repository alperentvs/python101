from re import I


sayilar = [1,5,14,15,35,57,72,75]

# 1- Sayilar listesindeki her bir elemani yazdirin.
# for i in sayilar:
#     print(i)

# 2- Sayilar listesindeki hangi sayilar 5'in katidir?
# for i in sayilar:
#     if (i % 5 == 0):
#         print(f"{i} sayisi 5'e tam bolunmektedir")

# 3- Sayilar listesindeki sayilarin toplami kactir?
# toplam = 0
# for i in sayilar:
#     toplam = toplam + i
# print("Sayilarin toplami: ", toplam)

# 4- Sayilar listesindeki cift sayilarin karesini aliniz.
# for i in sayilar:
#     if(i % 2 == 0):
#         print(i, i*i)

urunler = ['iphone 8','iphone X','iphone XR','samsung S10']
# 5- urunler listesindeki tum urunlerin 2. karakterlerini ekrana yazdirin.
# for i in urunler:
#     print(i[1])
    
# 6- Urunler listesinde icinde iphone gecen kac urun vardir? (index,find)
sayac = 0
for i in urunler:
    index = i.find('iphone')
    if (index>-1):
        sayac += 1
print(sayac)