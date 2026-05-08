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


def great(a):
    print(f"how are you, {a}")


def greating(b):
    print("greating is exacuted ")
    return f"hello {b}"


# === Call (Argument) ===
result1 = great("Abubakir")
print(result1)
# how are you, Abubakir
# void === none

result2 = greating("Brian")
print(result2)
# greating is exacuted
# return === hello Brian
