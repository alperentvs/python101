# email, password => database

# email == 'alperentavas45@gmail.com'
# password == '12345'

from re import I
from tkinter.tix import Tree


a, b, c, d = 5, 5, 20, 4
username = "alperentavas"
password = "12345"

sonuc = (a == b) # True
sonuc = (a != b) # False
sonuc = (a == c) # False
sonuc = (username == 'alperentavas') # True
sonuc = (username != 'alperntavas')  # True
sonuc = (a > c) # False
sonuc = (c > a) # True
sonuc = (a >= b) # True
sonuc = (a < c) # True
sonuc = (a <= b) # True
sonuc = (True == 1) # True
sonuc = (False == 0) # True

print(sonuc)
print(int(True)) # 1