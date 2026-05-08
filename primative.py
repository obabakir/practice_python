print("===  numbers  ===")
# in Java: variable is a name of storage location
# in Python: variable is named referance

count = 100
type_count = type(count)
print(f"the count: {count} and the type of count: {type_count}")

result1 = count.bit_count()  # => method
result2 = count.numerator  # => state
print(result1, result2)


print("===  string  ===")
# MOTHODS: upper(), lower(), title(), find(), replace()

course = "AI Python FulStack"
result = type(course)
print(f"the result (1): {result}")
# shows it is type


result = course.title()
print(f"the result (2): {result}")
# => capital case style:


result = course.upper()
print(f"the result (3): {result}")
# => uppercase style

result = course.replace("FulStack", "Master")
print(f"the result (4): {result}")
# => biz course ga tenglangan result qiymatni ozgartirayapmis shunga  asl coursre.value ozgarmadi
print(course)


# course = course.replace("FulStack", "Master")
# print(f"the result (4): {result}")
# # => biz course ga tenglangan result qiymatni ozgartirayapmis shunga  asl coursre.value ozgarmadi
# print(f"new_course.value: {course}")

print("===  booolean  ===")
# Functions:
'''
type() => finds type of object value
input() => terminalga kiritilgan valueni qiymatini bertadi
bool() => Truthy = true, 100, -100, "MIT" 
       => Falsy = false, 0, " ",  
       => None
str() => changes number to string
int() => changes string to number
'''

y = input("give your value for y:")
print(f"y: {y}")
# >>>>   give your value for y:30
# >>>>   y: 30

# test_falsy = ""
# Note: in javascript + node.js da operatorlardan :
# && → AND
# || → OR
# ?? → Nullish coalescing
# ?. → Optional chaining
# Pythonda bu < or >
test_falsy = "" or 0 or 100
# true qatdi chunki 1 ta 100 holatda true ligi uchun
print("test_falsy", bool(test_falsy))

# test_truthy = "MIT group"
test_truthy = "MIT group" and 100
# and 0 ni qoshsak False olamiz
# true qatdi chunki 1 ta 100 holatda true ligi uchun
print("test_truthy", bool(test_truthy))
