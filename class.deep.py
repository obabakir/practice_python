print("==== encapsulation ====")
# Encapsulation => public  __private  _protected


class Account ():
    # state
    description = "The class makes bank accounts"

    # constructor
    def __init__(self, owner, amount):
        self.__owner = owner
        self.__amount = amount

        # method

    def get_balance(self):
        print(f" the owner {self.__owner} has {self.__amount} usd")

    def deposit(self, amount):
        print("Deposited:", amount)
        self.__amount += amount
        print(f"Total amount: {self.__amount} usd")

    def withdraw(self, amount):
        print("Withdrawn:", amount)
        self.__amount -= amount
        print(f"Total amount: {self.__amount} usd")

    @property
    def holder(self):
        return self.__owner

    @holder.setter
    def holder(self, new_owner):
        self.__owner = new_owner
        print("changed ownership by hand from here:", self.__owner)

    def change_ownership(self, new_owner):
        self.__owner = new_owner
        print("changed ownership by hand from here:", self.__owner)


print("--------- -------- -------")
myAccount = Account("Brian", 1000)
myAccount.get_balance()

myAccount.deposit(3500)
myAccount.withdraw(400)

myAccount.get_balance()

print("--------- <--> -------")

# ==>> privatega otgandan keyin hech qanday ma'lumot ololmadik
# myAccount.amount = 1000000
# myAccount.owner = "Martin"
# myAccount.get_balance()
# print(myAccount.owner)
'''
 the owner Martin has 1000000 usd
 before encapsulation: Martin
'''

# ==== ==== ERROR  HANDLING ==== ====
# try:
#     result = myAccount.owner
#     print(result)
# except Exception as err:
#     print(f"No targer state is found {err}")

'''
# No targer state is found 'Account' object has no attribute 'owner'
'''

try:
    result = myAccount.__owner
    print(result)
except Exception as err:
    print(f"No targer state is found {err}")

'''
No targer state is found 'Account' object has no attribute '__owner'
'''
# state korinishida ===  getter  ====

# case === getter
print("owner before:",  myAccount.holder)  # state


# case === ruchnoy
# myAccount.change_ownership("Jhon")
# print("owner after:",  myAccount.holder)

'''
owner before: Brian
changed ownership by hand from here: Jhon
owner after: Jhon
'''

# case ==> setter  <==
myAccount.holder = "Alisher"
print("owner setter after:",  myAccount.holder)


'''
owner before: Brian
changed ownership by hand from here: Alisher
owner after: Alisher
'''
