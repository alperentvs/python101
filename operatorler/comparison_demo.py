# 1- Girilen 2 sayıdan hangisi büyüktür?
sayi1 = int(input("sayi 1:"))
sayi2 = int(input("sayi 2:"))

sonuc = (sayi1 > sayi2) # True, False

print(f"{sayi1} {sayi2} den buyuktur: {sonuc}")

# 2- Girilen bir sayinin tek mi cift mi oldugunu yazdirin
sayi = int(input("sayi:"))

sonuc = (sayi %2 == 0)
print(f"{sayi} cift sayidir: {sonuc}")

# 3- Girilen bir sayinin negatif pozitif durumunu yazdirin
sayi = int(input("sayi:"))

sonuc = (sayi > 0)
print(f"{sayi} pozitif sayidir: {sonuc}")

# 4- Kullanicidan 2 vize (%60) ve final (%40) notunu alip ortalama hesaplayiniz.
#   Eger ortalama 50 ve ustundeyse gecti degilse kaldi yazdirin.
vize1 = float(input("vize 1: "))
vize2 = float(input("vize 2: "))
final = float(input("final: "))

ortalama = (((vize1 + vize2) /2) * 0.6) + (final * 0.4)
print(f"not ortalamaniz: {ortalama} ve dersten gecme durumunuz: {ortalama>=50}")


# 5- Parola ve email bilgisini isteyip dogrulugunu kontrol ediniz.
#    (email: alperentavas45@gmail.com parola:12345)

_email = "alperentavas45@gmail.com"
_password = "12345"

email = input("email: ")
password = input('password: ')

isEmail = (email.lower().strip() == _email)
isPassword = (password.strip() == _password)

print(f"email dogrulugu: {isEmail} ve parola dogrulugu: {isPassword}")