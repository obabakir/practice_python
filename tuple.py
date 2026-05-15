'''
TUPLE:
(1) What is a tuple?
(2) Unpacking arguments
(3) Zip
'''

print("===== What is a tuple? =====")
# Java/PHP/Node.JS array => Python da bu list

# LITERAL
numbs = [3, 5, 1, 2]
# car_dict = {"brand": "BMW", "model": "X5", "year": 2020}

# CONSTRUCTOR
letters = list("MIT, Enginx")
# person_dict = dict(name="Brian", age=30, city="NY")

fruits = ["apple", "banana", "orange", "grape"]
print("before fruits:", fruits)


fruits[2] = "kiwi"
print("after fruits:", fruits)

'''
before fruits: ['apple', 'banana', 'orange', 'grape']
after fruits: ['apple', 'banana', 'kiwi', 'grape']
'''

print("===== tuple formation =====")
# fruits.append("kiwi")  python  & javascript # === fruits.push("kiwi")

# tuple formation => (1, 2, 3, 4) => tuple() constructor, we cannot change the values

animals = ("cat", "dog", "rabbit", "hamster")

tuple_obj = ("MIT", 100, True,  None)

print("the animarls 2 index:", animals[2])
print("the tuple object:", tuple_obj)

'''
the animarls 2 index: rabbit
the tuple object: ('MIT', 100, True, None)
'''
# can't be changed => immutable
# animals[2] = "turtle"  # TypeError: 'tuple' object does not support item assignment

# try void these
# might be tuple, but not recommended
people = "Andrew", "Sarah", "David", "Emily"
animal = "cat",  # this is a tuple with one element,

print("==== unpacking arguments ====")

# "Facebook" ==== checking mistake
groups = ["MIT", "Enginx", "Google", "Amazon",]
(x, y, z, a) = groups
print(f"the x: {x}, and the y: {y}, ")

#   (x, y, z, a) = groups
# ^^^^^^^^^^^^
# ValueError: too many values to unpack (expected 4, got 5)
'''
the x: MIT, and the y: Enginx, 
'''
# if we have more elements than variables, we can use * to unpack the remaining elements into a list
(x, y, *rest) = groups
print(f"the x: {x}, and the y: {y}, ")
print(f"and the rest: {rest}")
''''
the x: MIT, and the y: Enginx, 
and the rest: ['Google', 'Amazon']
'''

# ========== ========== =======
#                    *args > tuple unpacking =>
#  *args => variable length arguments => we can pass any number of arguments to a function

# Call


def calculation(*args):
    print("the args:", args)
    total = 1
    for x in args:
        total *= x
    # print(f"the totals arg (value): {type(args)}")
    # the totals arg (value): <class 'tuple'>
    print("the total value:", total)
    return total


# Define
calculation(2, 3, 4)
# the args: (2, 3, 4)
# the total value: 24

print("----- -------")
calculation(0, 2, 300)

# the args: (0, 2, 300)
# the total value: 0
print("----- -------")
calculation(5, 7)
# the args: (5, 7)
# the total value: 35


# ========== ========== =======
# *kwarg > dictionary
#                    **kwargs > tuple unpacking =>
#  **kwargs => keyword arguments => we can pass any number of keyword arguments to a function

# DEFINE
def introduce(**kwargs):
    print(f"the type(**kwargs): {type(kwargs)}")
    print(f"Hi, I am {kwargs['name']}, I am {kwargs['age']} years old.")

    # CALL
introduce(name="Brian", age=30)
introduce(name="Sarah", age=25, single=True)

'''
the type(**kwargs): <class 'dict'>
Hi, I am Brian, I am 30 years old.
the type(**kwargs): <class 'dict'>
Hi, I am Sarah, I am 25 years old.
'''


def greeting(*args, **kwargs):  # *args => arguments, **kwargs => keyword and arguments
    print(f"the args: {args}")
    print(f"the kwargs: {kwargs}")


    # CALL
greeting("reading", "swimming", True, 10, name="Brian", age=30)

'''
the args: ('reading', 'swimming', True, 10)
the kwargs: {'name': 'Brian', 'age': 30}
'''

print("==== Zip ====")
tuple1 = (1, 2, 3, 4)
tuple2 = ("a", "b", "c", "d")

zipped = zip(tuple1, tuple2)
print(" zipped :", zipped)
#  zipped : <zip object at 0x1012d7b80>
# Note that the zip function returns a zip object,

result = list(zipped)
print("the zipped list, result:", result)
# the zipped list, result: [(1, 'a'), (2, 'b'), (3, 'c'), (4, 'd')]
