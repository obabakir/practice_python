'''
FUNCTIONS:
(1) Define vs Call
(2) Parameter vs Argument
(3) Keyword & Define argument
(4) Scope

'''
print("=== Define (Parameter) vs Call (Argument) ===")
# build in function =>> print(), type()
#  Functions reusable block of code!
# Instead of block {} in Java, Python uses indentation! (means spaceing ^tab^ or ^ ->| ^)

# === Define (parameter) ===

# Note: python alse has "void = None" and "return = value"


def great(a):
    print(f"how are you, {a}")


def greating(b):
    print("greating is exacuted ")
    return f"hello {b}"


# === Call (Argument) ===
result1 = great("Abubakir")
print("result1:", result1)
# how are you, Abubakir
# void ===result1: none

result2 = greating("Brian")
print("result2", result2)
# greating is exacuted
# return === result2: hello Brian


print("=== Keyword (Parameter ga) vs Default (Argument ga) ===")

# === Define (default value can be inserted) ===


def give_great(name, age=20):
    print(" give_great is exacuted")
    return f"Hi {name}, you are {age} years old"


# === Call (keywords can be inserted this is tyo make the function more specific) ===

result3 = give_great(name="Martin", age=30)
print("result3:", result3)
#  result3: Hi Martin, you are 30 years old


result4 = give_great(name="Jhon")
print("result4:", result4)
# result4: Hi Jhon, you are 20 years old


print("=== Scope ===")
# Scope === priority


# Define
b = 10
# 3


def calculating(a, b):
    # 2
    c = a * b
    # 1
    print(f"the value of is is {c}")


#   Call
calculating(15, 6)
