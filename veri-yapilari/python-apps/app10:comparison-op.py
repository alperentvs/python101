# 1- Girilen 2 sayıdan hangisi büyüktür?
sayi1 = int(input('sayı 1: '))
sayi2 = int(input('sayı 2: '))

sonuc = (sayi1 > sayi2) #True, False

print(f"{sayi1} {sayi2} den büyüktür: {sonuc}")

# 2- Girilen bir sayının tek mi çift mi olduğunu yazdırın.
sayi = int(input('sayı: '))

sonuc2 = (sayi % 2 == 0)
print(f"{sayi} çift sayıdır: {sonuc}")

# 3- Girilen bir sayının negatif pozitif durumunu yazdırın.
sayi3 = int(input('sayı: '))

sonuc3 = (sayi3 > 0)
print(f"girilen sayı pozitiftir: {sonuc}")

# 4- Kullanıcıdan 2 vize (%60) ve final (%40) notunu alıp ortalama hesaplayınız.
# Eğer ortalama 50 ve üstündeyse geçti, değilse kaldı yazdırın.
vize1 = float(input('ilk vize: '))
vize2 = float(input('ikinci vize: '))
final = float(input('final: '))

ortalama = (((vize1 + vize2) / 2) * 0.6) + (final * 0.4)
print(f"not ortalaması: {ortalama}")

# 5- Parola ve email bilgisini isteyip doğruluğunu kontrol ediniz.
# (email: info@alperentavas.com parola:12345)
_email = "info@alperentavas.com"
_password = "123456"

email = input("email: ")
password = input("password: ")

isMail = (email.lower().strip() == _email)      # lower() = büyük küçük harf önemseme
isPassword = (password.strip() == _password)    # strip() = boşluk karakterini önemseme

print(f"email doğruluğu {isMail} ve parola doğruluğu: {isPassword}")