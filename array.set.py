'''
(1) Array. & Set
(2) Set 
(3) Specific operators with set
'''

from array import array
print("=====================    (1) Array. & Set ================================")
# Array - list, tuple, set, dictionary
# We need to import array

# Definition: it works with only one data type, it is more efficient than list, it is mutable, it is a collection of items stored at contiguous memory locations, it is used to store homogeneous data, it is faster than list, it is more memory efficient than list, it is used to store large data sets, it is used in scientific computing, it is used in machine learning, it is used in data analysis, it is used in data visualization.
# i - integer, f - float, d - double, u - unicode character

numbers = array("i", [1, 2, 3, 4, 5])  # array constructor
print(
    f"numbers (i): {numbers} and type: {type(numbers)}, length of numbers {len(numbers)}")

'''
numbers (i): array('i', [1, 2, 3, 4, 5]) and type: <class 'array.array'>, length of numbers 5
'''
numbers.append(100)  # add to the end of the array
numbers.insert(0, 14)  # add to the beginning of the array
print(f"numberes2: {numbers}")

numbers.remove(5)  # remove the first occurrence of 5
numbers.pop()  # remove the last element of the array
print(f"numberes3: {numbers}")

'''
numberes2: array('i', [14, 1, 2, 3, 4, 5, 100])
numberes3: array('i', [14, 1, 2, 3, 4])
'''

del numbers[0: 2]  # delete the first two elements of the array
print(f"numberes4: {numbers}")

'''
numberes4: array('i', [2, 3, 4])
'''

print(" =====================    (2) Set ================================")
# Set - it is a collection of unique items, it is unordered, it is mutable,

new_numbers = array("i", [1, 4, 7, 5, 7, 5, 7, 5, 4, 7, 8, 4, 41])
numbers_set = set(new_numbers)  # convert array to set
print(
    f"the numbers_set: {numbers_set} and type: {type(numbers_set)}, length of numbers_set {len(numbers_set)}")
''''
the numbers_set: {1, 4, 5, 7, 8, 41}  
length of numbers_set 6
and type: <class 'set'>, 
'''
# unique elementlarni saqlaydi, repeated numbers weren't added to the set

numbers_set.add(200)    # add to the set
print(f"the numbers_set(2) after add: {numbers_set}")
'''
the numbers_set(2) after add: {1, 4, 5, 7, 8, 41, 200}
'''

print("=====================    (3) Specific operators with set ================================")
# |, &, -, ^ operators with set

a = {10, 20, 50}
b = {20, 40}
result1 = a | b  # union of a and b
result2 = a & b  # intersection of a and b
result3 = a - b  # difference of a and b
result4 = a ^ b  # symmetric difference of a and b

print(f"result1: {result1}")  # result1: {50, 20, 40, 10}
print(f"result2: {result2}")  # result2: {20}
print(f"result3: {result3}")  # result3: {10, 50}
print(f"result4: {result4}")  # result4: {40, 10, 50}


#  | - union operator, it returns a new set that contains all the elements from both sets, it removes the duplicate elements
# & - intersection operator, itreturns only similar elements that are present in both sets
# - difference operator, it returns a new set that contains only the elements that are present in the first set but not in the second set
# ^ - symmetric difference operator, it returns a new set that contains only the elements that are present in either set but not in both sets
