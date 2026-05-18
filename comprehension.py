''' Comprehension
(1) What is  comprehension $ list comprehension
(2) Set and dictionary comprehension
'''
print("=====================    (1) What is  comprehension $ list comprehension ================================")
# comprehension acts like spread operator!

# Comprehension - it is a concise way to create a new list,
# set, or dictionary from an iterable, it is more readable and faster than traditional for loop,
# it is used to create a new list, set, or dictionary by applying an expression to each item in an iterable,

''' Comprexension general syntax:
a) *iterable
b) <expression> for iterm in iterable
c) <expression> for iterm in iterable if <condition>
'''
# list comprehension
numbers = [1, 2, 4, 2, 1, 20]
list_numbers = [*numbers]  # version a

print("numbers:", numbers)
print("list_number:", list_numbers)

'''
numbers: [1, 2, 4, 2, 1, 20]
list_number: [1, 2, 4, 2, 1, 20]
'''

# False, because they are different objects in memory
print(numbers is list_numbers)
print(numbers == list_numbers)  # True, because they have the same values
print(id(numbers))  # 4309718656
print(id(list_numbers))  # 4309911744

print("---------")
# version b
people = [("Robert", 20), ("Steve", 19), ("Joseph", 25)]
list_people = [person[0] for person in people]

print("people:", people)
print("list_people:", list_people)

'''
people: [('Robert', 20), ('Steve', 19), ('Joseph', 25)]
list_people: ['Robert', 'Steve', 'Joseph']
'''

# huddi shunday, lekin yoshlarni olish uchun
list_people2 = [a[1] for a in people]
print("list_people2:", list_people2)

'''
list_people2: [20, 19, 25]
'''
# we can replace the variable name with any name, it doesn't matter, but it is a good practice to use meaningful variable names
# people => person
# cars => car
# numbers => number


print("---------")
# version c
cars = [
    ("BMW", 2020),
    ("Mercedes", 2019),
    ("Audi", 2021),
    ("Toyota", 2018),
    ("Kia", 2022)
]

# with if condition
new_cars = [car[0] for car in cars if car[1] > 2019]
print("new_cars:", new_cars)
# new_cars: ['BMW', 'Audi', 'Kia']

new_cars2 = [car for car in cars if car[1] > 2020]
print("new_cars2:", new_cars2)
# new_cars2: [('Audi', 2021), ('Kia', 2022)]

print("=====================    (2) Set and dictionary comprehension ================================")
# set comprehension (a version )
numbs = [1, 2, 3, 4, 5, 5, 4, 3, 2, 1]
print("numbs:", numbs)
# numbs: [1, 2, 3, 4, 5, 5, 4, 3, 2, 1]


set_numbs = {*numbs}
print("set_numbs:", set_numbs)
# set_numbs: {1, 2, 3, 4, 5}


citizens = [("Robert", 20), ("Steve", 19), ("Joseph", 25), ("Brian", 29)]
list_citizens = [person[0] for person in citizens]

print("list_citizens:", list_citizens)
# list_citizens: ['Robert', 'Steve', 'Joseph', 'Brian']

# agar a[0] o'rniga a ni qoysak ham yosh ham ism olamiz
list_citizens2 = [a[0] for a in citizens if a[1] > 20]
print("list_citizens2:", list_citizens2)
# list_citizens2: ['Joseph', 'Brian']


# (<expression> for item in iterable) generic === less used
