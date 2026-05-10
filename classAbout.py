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
