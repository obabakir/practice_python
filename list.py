''' LIST
    (1) Working with lists
    (2) List method
    (3)Lambda Function
    (4) Enumarte, map and filter
'''

print("=====================  (1) Working with lists ================================")
# Java/PHP/NodeJS array => Python list
# LIST 2 XIL USULDA QURILADI   (1)literal,   (2)constructor

# (1) literal

person = {"name": "JACK", "age": 25}  # dictionary, json object
people = ("Andrew", "John", "Leo")  # [tuple] literal usulda tash qilish
groups = ["MIT", "FLEX", "DEVEX", "MG"]  # literal uslubida list tash qilish
for team in groups:  # for orqali qolga olamiz
    print(f"the team: {team}")

# (2)constructor
result = list("Hello World!")
print(f"the result: {result} and size: {len(result)}")


print("-------")
fruits = ["apple", "orange", "lemon", "kiwi"]
a = fruits[0]
b = fruits[0:2]  # [0, 2] /// dan => gacha /// 2 kirmaydi
# 3 qadam sakraydi /// birinchi elementdan boshlab 3 qadamda sakraydi ///
c = fruits[::3]
d = fruits[::-1]  # teskari holat /// reverse process

print("a:", a)
print("b:", b)
print("c:", c)
print("d:", d)


print("=====================    (2) List method ================================")
# method > append() insert() pop() remove() clear() sort() mutable arrayga tasrkoratadi                         index() Immutable -tasr korsatmaydi

# Mutable
letters = ["a", "d", "b"]  # harfklardan iborat array

letters.append("c")  # add behing/to the end of the list
print(f"the append result: {letters}")

letters.insert(0, "z")  # add to front & to the specific index
print(f"the insert result: {letters}")

size = len(letters) - 1
result1 = letters.pop(size)  # pop the end of the list, default value is  -1
print(f"the pop result1: {result1} and letters {letters}")

result2 = letters.pop(0)  # pop the beginning of the list
print(f"the pop result2: {result2} and {letters}")
# letters.pop(1)  # pop the specific index

print("---------")
animals = ["dog", "cat", "capybara", "fish", "lion"]
print("animals:", animals)


animals.remove("lion")  # udalit qilish
print("animals remove:", animals)

# del operator
del animals[2:4]  # dan gachsa 2 va 3 indexni delete qiladi
print("animals delete:", animals)  # delete aytgan sonni

exist = animals.index("cat")  # nechinchi indexni topadi
print("cat exist", exist)

# animals.clear()  clear all the elements of the list
print("animals clear:", animals)


# in python you will get the element index of  vzlue error, so we used the if statement to check if the element exists in the list before trying to get its index, or can do it with try except block, we will learn it in the error handling section
if "cat" in animals:
    print("index of cat:", animals.index("cat"))
else:
    print("cat does not exist")


print("----sort------")  # tartiblab yozib beradi
numbers = [2, 20, 12, 8, 57]
numbers.sort()
# kichik qiymatdan kottaga qarab //from small to big
print("sort default:", numbers)
numbers.sort(reverse=True)
# kotta qiymatdan kichikga  qarab // from big to small
print("sort reverse=True:", numbers)


print("--- Immutable sorted function & index method --")
# Immutable > sorted  function & index() method
# if sometimes  we need to sort the elements of the list but we don't want to change the original list, we can use the sorted() function, it will return a new sorted list without changing the original list
numbs = [2, 20, 12, 100]
new_numbs = sorted(numbs)  # bunda yangi new_numbs ozgargan
print(f" the sorted numbs: {numbs} and new_numbs: {new_numbs}")
