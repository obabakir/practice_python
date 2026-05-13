'''
OPERATORS & CONDITIONALS

(1) Operators: +, -, *, /, //(yaxlid hosila bolishdan namoyon bolgan), % (qoldiq), ** (daraja), =, ==, !=, >, <, >=, <=, and, or, not |||| is operator to compare reference in Python
(2) Conditionals:  
()Logical operators: 
 
'''

print(" ===== OPERATORS =====")
# + - > >= < <= * / // % **
# a = 19
# b = 5
# d = 2
# print("a + b =", a + b)  # 24
# print("a - b =", a - b)  # 14
# print("a * b =", a * b)  # 95
# print("a / b =", a / b)  # 3.8
# print("a // b =", a // b)  # 3 yaxlit hosilasi
# print("a % b =", a % b)  # 4 qoligi

# print("d ** 2 =", d ** 2)  # 4 kvadrat
# print("d **3 =", d ** 3)  # 8 kub

# #  =====  =====  =====
# result = a // b
# print("the result:", result)  # 3
# left = a % b
# print("the left:", left)  # 4
# print(f"the result: {result} and the left: {left}")  # the result: 3 and the left: 4

# a = a + 100
a = 19
a += 100
print("the result:", a)  # 119

print("=" * 6)  # ======

c = dict(name="Brian", age=29)
g = dict(name="Brian", age=29)
e = c
print("c == g:", c == g)  # True

print(id(c))  # 4345359296
print(id(g))  # 4345359360
print(id(e))  # 4345359296


print("c == g:", c == g)     # True |||||| only value in Python
# in JavaScript: c == g: false |||||| you compare reference in JavaScript

# to compare the objects reference in Python |||| is operator
print("c is g:", c is g)  # False
print("c is e:", c is e)  # True
