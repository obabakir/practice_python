'''
CLASS deep learning:

-- Encapsulation
-- Inheritence
-- Polimorphysm
'''


print("==== Inheritence ====")
# PARANT > CHILD
# PARANT > CHILD (provides only public & protected properties)


class Animals:  # parent class

    description = "This class parent for animals"

    def __init__(self, voice):
        # only the parent class has this attribute
        self._status = "the animal is alive"
        self.voice = voice

    def make_voice(self):
        print(f"the animal make voice: {self.voice}")


print("--------- -------- -------")


class Dog(Animals):  # child class

    def __init__(self, name, sound, voice):
        super().__init__(voice)
        self.name = name
        self.sound = sound

    def introduce(self):
        print(f"{self.name} says: {self.sound} - {self.sound}")

    def protect(self):
        print("yes I can protect you!")


print("--------- -------- -------")


class Cat (Animals):  # child class

    def __init__(self, name, sound, voice):
        super().__init__(voice)
        self.name = name
        self.sound = sound

    def introduce(self):
        print(f"{self.name} says: {self.sound} - {self.sound}")

    def play(self):
        print("yes I can play with you!")


print("--------- -------- -------")


class Fish (Animals):  # child class

    def __init__(self, name, sound, voice):
        super().__init__(voice)
        self.name = name
        self.sound = sound

    def introduce(self):
        print(f"{self.name} says: {self.sound} - {self.sound}")

    def swim(self):
        print("yes I can swim!")


dog = Dog("Rex", "Woof", True)
cat = Cat("Tom", "Meow", True)
fish = Fish("Nemo", "ZzZ", False)

dog.introduce()
cat.introduce()
fish.introduce()

print("--------- <--> -------")

dog.make_voice()
cat.make_voice()
fish.make_voice()

print("<--------- <--> ------->")

print(Animals.description)
print(dog.description)
'''
This class parent for animals
This class parent for animals
'''
print(cat.voice, fish.voice, dog.voice)
'''
True False True
'''

print("--------- <--> -------")

print("dog.status: ", dog._status)
print("cat.status: ", cat._status)

'''
dog.status:  the animal is alive
cat.status:  the animal is alive
'''


# print("fish.status: ", fish.__status)

# ==== Error ==== (private properties can is not inheritable)
#  print("fish.status: ", fish.__status)

print("==== Polimorphysm ====")
