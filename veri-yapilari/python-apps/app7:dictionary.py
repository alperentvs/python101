# 1- 3 ürün bilgisini (id,ad,fiyat) kullanıcıdan aldığınız bilgilerle dictionary içinde saklayınız.

urunler = {}

id = input('id: ')
ad = input('ad: ')
fiyat = input('fiyat: ')

urunler[id] = {
    "ad": ad,
    "fiyat": fiyat
}

id = input('id: ')
ad = input('ad: ')
fiyat = input('fiyat: ')

urunler[id] = {
    "ad": ad,
    "fiyat": fiyat
}

id = input('id: ')
ad = input('ad: ')
fiyat = input('fiyat: ')

urunler[id] = {
    "ad": ad,
    "fiyat": fiyat
}

print(urunler)

# 2- Ürün id bilgisini kullanıcıdan alıp ilgili ürün bilgisini gösterin.

id = input('aramak istediğiniz ürün id: ')
urun = urunler[id]

print(urun)
