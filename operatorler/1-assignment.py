# a = 5
# b = 10
# c = 20

a, b, c = 5, 10, 20

# a, b = b, a

a += 5       # a = a + 5
a -= 5       # a = a - 5
a *= 5       # a = a * 5
a /= 5       # a = a / 5
a %= 5       # a = a % 5
a **= 5      # a = a ** 5
a //= 5      # a = a // 5

values = (1, 2, 3, 4, 5, 6)

# a, b, c = values  --> too many hatasi
# a, b, *c = values --> 1 2 [3, 4, 5, 6]
# a, *b, c = values --> 1 [2, 3, 4, 5] 6
# *a, b, c = values --> [1, 2, 3, 4] 5 6

print(a,b,c)