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
