isimler = ['Ada','Yiğit','Hasan','Beril']
yaslar = [1998, 2000, 1998, 1987]

# 1- "Cenk" ismini listenin sonuna ekleyiniz.
isimler.append('Cenk')

# 2- "Sena" ismini listenin başına ekleyiniz.
isimler.insert(0,"Sena")

# 3- "Hasan" ismini listeden siliniz.
isimler.remove("Hasan")

'''
isimler.pop()  --> En son elemanı siler
isimler.pop(0) --> Verilen indeksi siler
'''

# 4- "Yiğit" isminin indeksi nedir?
index = isimler.index('Yiğit')
isimler.pop(index)
print(index)

# 5- "Beril" listenin bir elemanı mıdır?
sonuc = "Beril" in isimler

# 6- Liste elemanlarını ters çevirin.
isimler.reverse()
yaslar.reverse()

# 7- Liste elemanlarını alfabetik olarak sıralayın.
isimler.sort()

# 8- yaslar listesini büyükten küçüğe sıralayın.
yaslar.sort()

# 9- str = "Iphone X, Iphone XR" karakter dizisini listeye çevirin.
s = "Iphone X, Iphone XR"
sonuc = s.split(',')

# 10- yaslar dizisinin en büyük ve en küçük elemanı nedir?
print(min(yaslar))
print(max(yaslar))

# 11- yaslar dizisinde kaç tane 1998 değeri vardır?
print(yaslar.count(1998))

# 12- yaslar dizisinin bütün elemanlarını siliniz.
yaslar.clear()

# 13- Kullanıcıdan alacağınız 3 tane marka bilgisini bir listede saklayınız.

markalar = []

marka = input("marka: ")
markalar.append(marka)

marka = input("marka: ")
markalar.append(marka)

marka = input("marka: ")
markalar.append(marka)

print(markalar)

print(isimler)
print(yaslar)