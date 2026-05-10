print("=== Iterable objects & RANGE ====")
# Iterable === takrorlanish
# Iterable objects => string dict tuple list range map filter

range_obj = range(5)
print("range_obj: ", range_obj)

for ele in range_obj:
    print("range_obj elementi:", ele)

'''
range_obj:  range(0, 5)
range_obj elementi: 0
range_obj elementi: 1
range_obj elementi: 2
range_obj elementi: 3
range_obj elementi: 4 gacha bolgan qiymatlarni beradi
'''

# text = "MIT"
# for letter in text:
for letter in "MIT":
    print(f"the element: {letter}")
'''
the element: M
the element: I
the element: T
'''

print("=== DICTIONARY ===")
# DICTIONARY is Json Object!
#  2 types of FORMATION
person = {"name": "Justin", "age": "25", "singe": True}

person_obj = dict(name="Justin", age=25, single=True)

print(f"person: {person}")
print(f"person_obj: {person_obj}")

'''
person: {'name': 'Justin', 'age': '25', 'singe': True}
person_obj: {'name': 'Justin', 'age': 25, 'single': True}
'''

# Method === get()

nameTaking = person_obj["name"]
print(nameTaking)
# Justin

name = person_obj.get("name")
hobby = person_obj.get("hobby")
balance = person_obj.get("balance", 0)
# hobby ni qidirayapmiz, agar * nameTaking = person_obj["name"] * usulda qidirsak yoq valuni bizga terminal err beradi hendle qilishni organdik, object.py da qildik
# bu yerda agar balance bolmasa 0 qiyhmatni qaytarishi == ? ni organganmiz
print(f"the name is {name}, hobby: {hobby} and balance: {balance}")
'''
the name is Justin, hobby: None and balance: 0
'''

# delete qiladi shu valueni splice ga biroz oxshaydi
del person_obj["single"]
for key in person_obj:
    print(f" the key: {key} >> value {person_obj.get(key)}")

'''
the key: name >> value Justin
 the key: age >> value 25
'''
# singe is deleted
