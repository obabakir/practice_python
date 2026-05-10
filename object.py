'''
---- OBJECTS -----
(1)What is object
(2)iretable objects & RANGE
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
