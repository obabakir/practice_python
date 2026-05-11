'''
CLASS
(1) What is class
(2) Ordenary and Static class
(3) Special Methods
'''

print("=== What is class ===")

#  Class => Blueprint for object creation
# Structure => State || Constructure || Method


class Person():
    # state
    message = "static state property"
# bu stateni static state sifatida oldik

    # constructor
    def __init__(self, name, age):
        self.name = name
        self.age = age

    # method
    def introduce(self):
        print(f"{self.name} says: How do you do!")

    def say_age(self):
        print(f"{self.name} says I am {self.age}!")

    @classmethod
    def explain(cls):
        print("this static method is executed")


person1 = Person("Justin", 25)
person2 = Person("Martin", 35)
person3 = Person("John", 22)

# ordinary state
print("person1.name:", person1.name)

# ordinary method
person1.introduce()
person2.say_age()

print("===== Ordinary vs Static properties =====")

# static state
new_message = Person.message
print("new_message:", new_message)

# static method
Person.explain()


print("===== special/magic methods =====")

# Python's most common special methods are below:

'''

 __init__   ==>> constructor qismda
 ___new__  ==>> avtamatik class bn quriladi
 __str__ ==>> classni objectga tenglab shu qiymatni ozini print qilganda ishga tushuvchi method
 #
 
 __call__  ==>> classni objectga tenglab shu qiymatni ozini function sifatida chaqirganda
 
 #
 __getitem__  
 __eq__  
 __len__  
 and others.....

'''


class Car:

    # state
    description = "This class makes cars"

    # constructor

    # special method

    # def __new__(cls):    # *args ham bor lekin toxtalmaymiz
    #     print("* __new__ *")
    #     return super().__new__(cls)
    # kam ishlatiladi, va yozilmaydi chunki avtamatik ravishda ishga tushadi
    # clasni ojectga tenglaganimizdaela ishga tushadi
    # __new__ === new (java scriptdagi)
    # va u class yasaganimizda aftamatic ishga tushadi lekin yuqorida syntaxnini yozdik va tekshirdin qani birinch chiqarmikan den printda

    def __init__(self, name, year):
        self.name = name
        self.year = year

    # methods
    def start_engine(self):
        print(f"the {self.name} started engine!")

    def stop_engine(self):
        print(f"the {self.name} stopped engine!")


# CASE:   __str__
def __str__(self):
    return f"{self.name} was manifactured in {self.year} "


# CASE:   __call__

def __call__(self):
    print("the object is called like function ")
    return True


my_car = Car("Ferrari", 2025)
my_car.start_engine()
my_car.stop_engine()

print("------")

your_car = Car("Toyota", 2026)

# __new__ === new (java scriptdagi)
# va u class yasaganimizda aftamatic ishga tushadi lekin yuqorida syntaxnini yozdik va tekshirdin qani birinch chiqarmikan den printda
'''
* __new__ *
the Ferrari started engine!
the Ferrari stopped engine!
------
* __new__ *
'''
# print(" CASE:   __str__  ")
# strTest = your_car
# print("strTest", strTest)


# print(" CASE:   __call__ ")
# response = your_car()
# print("respoinse:", response)
