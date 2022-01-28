#Pythonda kullanıcıdan girdi almamızı sağlayan input() fonksiyonudur.
print(input())                           #kullanıcıdan girdi almamızı sağlar
print(input("Bir sayı giriniz: "))       #fonksiyonun içine bir değerde gönderebiliriz

a = input("Lütfen bir sayı giriniz: ")   #kullanıcıdan alınan değeri bir değişkene eşitleyebiliriz
print("Kullanıcının girdiği değer: ",a)

b = input("Lütfen bir sayı giriniz: ")
print(b * 3)
print(type(b))                            #input() fonksiyonundan dönen değer her zaman bize string değer olarak döner

c = int(input("Lütfen bir sayı giriniz: "))
print(c * 3)
print(type(c))                             #input() değerini int değer almak için type dönüşümü yapılır