''' Packages and Debugging
(1) Python package & Core Package 
(2) Package Manager & External Packages 
(3) Debugging

'''
# from PIL import Image
import turtle
print("====  Python package & Core Package ====")
#  Python Packages / Modules: Core, File, External
# Core packages => http://docs.python.org/3/library

# # Core Packages:
# t = turtle.Turtle()
# t.shape("turtle")
# t.color("brown")
# t.speed(2)
# t.circle(150)
# turtle.done()
# print("====")

# Screen setup
# screen = turtle.Screen()
# screen.bgcolor("white")
# screen.title("Pizza using Turtle Module")

# # Create turtle
# pizza = turtle.Turtle()
# pizza.speed(3)

# # ----------------------
# # Pizza base
# # ----------------------
# pizza.penup()
# pizza.goto(0, -150)
# pizza.pendown()

# pizza.color("orange")
# pizza.begin_fill()
# pizza.circle(150)
# pizza.end_fill()

# # ----------------------
# # Cheese layer
# # ----------------------
# pizza.penup()
# pizza.goto(0, -130)
# pizza.pendown()

# pizza.color("yellow")
# pizza.begin_fill()
# pizza.circle(130)
# pizza.end_fill()

# # ----------------------
# # Pepperoni function
# # ----------------------


# def pepperoni(x, y):
#     pizza.penup()
#     pizza.goto(x, y)
#     pizza.pendown()

#     pizza.color("red")
#     pizza.begin_fill()
#     pizza.circle(15)
#     pizza.end_fill()


# # Add pepperoni toppings
# pepperoni(-50, 20)
# pepperoni(40, 60)
# pepperoni(-80, -40)
# pepperoni(70, -20)
# pepperoni(0, 0)
# pepperoni(90, 40)
# pepperoni(-20, 90)

# # ----------------------
# # Pizza slice lines
# # ----------------------
# pizza.color("brown")
# pizza.pensize(2)

# for angle in [0, 45, 90, 135]:
#     pizza.penup()
#     pizza.goto(0, 0)
#     pizza.setheading(angle)
#     pizza.pendown()
#     pizza.forward(130)

# pizza.hideturtle()

# # Keep window open
# screen.mainloop()


# open ==>> orqalik filene ulash huddi linkka oxshaydi

my_file = open("material/message.txt", "r")

# r ==>> means ==> read
# doim fileni yopishinh kerak

# A vesrion
try:
    content = my_file.read()
    print("content:", content)
finally:
    my_file.close()
'''
content: "hello world"
"new way is waiting"
'''

# B version

with open("material/message.txt", "r") as your_file:
    your_content = your_file.read()
    print("your_content:",    your_content)

print("passed here")
'''
 your_content: "hello world"
"new way is waiting"
passed here
'''

print("=== Package Manager & External Packages ===")


''' Package Managers: pip pipenv yarn composer brew '''
# External Packages ==>> https://pypi.org/

# with Image.open("material/logo.png") as img_obj:
#     resized_img = img_obj.resize((200, 200))
#     resized_img.show()
#     resized_img.save("material/sample.png")

print(" ===== Debugging =====")


def get_summary(*args):
    amount = 5

    for a in args:
        amount += a

    return amount


result = get_summary(1, 2, 3, 4, 5)
print("result:", result)
# result: 20
