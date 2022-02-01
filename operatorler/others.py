# Identity Operator: is

x = y = [1, 2, 3]
z = [1, 2, 3]

print(x==y) # Deger karsilastirmasi
print(x==z) # Deger karsilastirmasi
print(x is not y) # Adres karsilastirmasi
print(x is z) # Adres karsilastirmasi


# Membership Operator: in

x = ['apple', 'banana']
print('banana' in x) # x'in icinde banana var mi?

name = 'Cinar'
print('a' in name)
print('a' not in name)