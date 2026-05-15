'''
LOOOP operators
(1) for
(2) while
(3) break/else
'''

print(" ===== foer operator ======")
# iterable objects => list, tuple, dict, string map, range, filter

text = "MIT"
numbs = [10, 7, 3, 4]
car_obj = dict(brand="BMW", model="X5", year=2020)
range_obj = range(5)  # (0,5) => 0,1,2,3,4

for letter in text:
    print(" the letter:", letter)

print("----- -------")

for num in numbs:
    print(" the number:", num)

print("----- -------")

for key in car_obj:
    print(f" the key: {key} => value: {car_obj[key]}")

print("----- -------")

for i in range_obj:
    print(f"the i => {i}")

print("----- -------")

for x in range(1, 20, 5):  # (start, stop, step), the x => 1, the x => 6, the x => 11the x => 16
    print(f"the x => {x}")

print("===== break/else ======")

for f in range(1, 20, 5):
    print(f"the f => {f}")
    if f > 10:
        print("reached the break point")
        break
else:
    print("Exacuted successfully")

'''
the f => 1
the f => 6
the f => 11
reached the break point
'''

for g in range(1, 20, 5):
    print(f"the g => {g}")
    if g > 100:
        break
else:
    print("Exacuted successfully")

'''
the g => 1
the g => 6
the g => 11
the g => 16
Exacuted successfully
'''

print("===== while operator ======")
numb = 40
while numb > 0:
    # print(f"the numb => {numb}")
    numb -= 10
    print(f"the numb => {numb}")
'''
the numb => 30
the numb => 20
the numb => 10
the numb => 0
'''
# the numb => 40
# the numb => 30
# the numb => 20
# the numb => 10
print("----- -------")
count = 0
while True:
    count += 1
    w = int(input("Find the number: "))
    if w == 41:
        print("Congratulations! You found the number in", count, "attempts.")
        break
    else:
        print("wrong, please find the number again")


'''
Find the number: 10
wrong, please find the number again
Find the number: 32
wrong, please find the number again
Find the number: 41
Congratulations! You found the number in 3 attempts.
'''
