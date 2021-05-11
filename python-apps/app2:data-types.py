'''
    Daire Alanı   : πr²
    Daire Çevresi : 2πr²
    ** Yarı çapı verilen bir dairenin alan ve çevresini hesaplayınız. (π: 3.14)
'''

pi = 3.14

r = float(input("yarı çap: "))

alan = pi * (r ** 2)
cevre = 2 * pi * r

print("alan:", alan, "çevre:" ,cevre)


'''
    Bir aracaın km cinsinden gittiği yol bilgisini mil olarak yazdırınız.
    mil = km / 1.609344
'''

print("Kaç km yol gittiniz?")
mesafeKm = input()
mesafeMil = float(mesafeKm) / 1.609344
mesafeMil = round(mesafeMil, 2) #mil bilgisini, noktadan sonra 2 basamak göstermek için

print(mesafeKm, "km = ",mesafeMil, "mil")