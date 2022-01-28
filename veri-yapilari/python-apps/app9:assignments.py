a, b, c, = 2, 5, 10

# 1- Kullanıcıdan aldığınız 2 sayının carpımı ile a,b,c toplamının farkı nedir?
x = int(input("x: "))
y = int(input("y: "))

sonuc = (x * y) - (a+b+c)
print(sonuc)

# 2- c'nin b'ye kalansız bölümünü hesaplayınız.
sonuc2 = c // b
print(sonuc2)
# 3- (a,b,c) toplamının mod 3'ü nedir?
sonuc3 = (a+b+c) % 3
print(sonuc3)

# 4- b'nin a. kuvvetini hesaplayınız.
sonuc4 = b ** a
print(sonuc4)

# sayilar = 1,5,7,10,3
# 5- a, *b, c = sayilar işlemine göre c'nin küpü kaçtır?
sayilar = 1,5,7,10,3
a, *b, c = sayilar
print(c ** 3)

# 6- a, *b, c sayilar işlemine göre b nin değerleri toplamı kaçtır?
a, *b,c = sayilar 
print(b[0] + b[1] + b[2])