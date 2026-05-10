'''
---- OBJECTS -----
(1)What is object
(2)Iterable objects & RANGE
(3) DICTIONARY
(4)Error hendling system
'''

import array  # packasge / module
import math  # package(objeckt package)

# if you want to get only spesific method(s):
from math import ceil
from math import asin, degrees

print(" ==== What is object ====")

# An object has state and methos
# Every thing is object in Python

print(type("Hello World"))
print(type(100))
print(type(True))
print(type(math))
print(type(array))

# Paradigm  => Functional programming & OOP
# OOP 4 Concepts => Abstruction | Encapsulation |  Inheritance | Polimorphism
result1 = math.ceil(97.7)
print("result1:", result1)

result2 = ceil(98.8)
print("result2:", result2)

'''
<class 'str'>
<class 'int'>
<class 'bool'>
<class 'module'>
<class 'module'>
result1: 98  ==>> yaxlitlash un ishlatiladi || import qilingan package ichidan 1 ta method ni tanlab oldik ||
result2: 99 ==>  yaxlitlash un ishlatiladi || import qilingan yolgiz method dan foydalandik ||
'''
print("=== Error hendling system ===")
car_dict = dict(name="Tayota", year=2026, electric=True)

# case 1 try bu data ni tekshiradi yoq bsa exceptga otadi jarayon shunga faqat print ishladi
try:
    print("passed here")
    result = car_dict["orign"]
    print("result:", result)

except KeyError as err:
    print("no origin state is found:", err)

'''
passed here
no origin state is found: 'orign'
'''

# case 2

try:
    print("passed here")
    result = car_dict["name"]
    print("result:", result)

except KeyError as err:
    print("no name state is found:", err)

'''
passed here
result: Tayota
'''
# case 2 try bu data ni tekshiradi va jarayonni yakunladi


# case 3
try:
    print("passed here")
    result = car_dict["color"]
    print("result:", result)

except KeyError as err:
    print("no color state is found:", err)

else:
    print("exacuted succesfully")

finally:
    print("final closing logic")

'''
passed here
no color state is found: 'color'
final closing logic
'''
# agar javob topilganda else method ishlardi

try:
    print("passed here")
    a = car_dict.speed
    print("result:", result)

except KeyError as err:
    print("no color state is found:", err)

except AttributeError as err:
    print("no speed is found:", err)
else:
    print("exacuted succesfully")

finally:
    print("final closing logic")

'''
passed here
no speed is found: 'dict' object has no attribute 'speed'
final closing logic

'''
