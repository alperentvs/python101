# value types => string, number
x = 5
y= 25

x = y 

y = 10 #Burda y'nin yeni degeri x'i etkilemez

print(x,y)

# reference types => list
a = ["apple","banana"]
b = ["apple","banana"]

a = b

b[0] = "grape" #Burada a ve b liste üzerinde ayni adresi tasidiklari icin b'de yapilan degisiklik a'yi da etkiler

print(a,b) 

#Ozetle value types ile ilgilenirken verinin kendisiyle,
#Reference types ile ilgilenirken listenin adresiyle islem yapiyoruz