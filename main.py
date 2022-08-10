# import colorgram
#
# colors = []
# colorgram = colorgram.extract("hirst_painting.jpg", 30)
#
# for color in colorgram:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color = (r, g, b)
#     colors.append(new_color)
#
# print(colors)

git config --global user.name "Nick Bukowitz"

import turtle as turtle_module
import random

color_list = [(134, 167, 191), (211, 156, 106), (197, 143, 166), (29, 110, 168), (234, 214, 86), (127, 74, 92),
              (187, 178, 19), (26, 136, 66), (55, 18, 26), (142, 20, 40), (38, 175, 113), (225, 170, 196),
              (116, 188, 144), (231, 77, 50), (172, 70, 46), (238, 218, 5), (37, 17, 16), (186, 91, 110), (9, 102, 52),
              (34, 167, 189), (20, 20, 28), (183, 185, 213), (234, 171, 159), (154, 215, 172), (142, 20, 16),
              (89, 124, 182)]

hirst = turtle_module.Turtle()
turtle_module.colormode(255)
hirst.speed("fastest")
hirst.penup()
hirst.hideturtle()

hirst.setheading(225)
hirst.forward(300)
hirst.setheading(0)

for row in range(10):
    for column in range(10):
        hirst.dot(20, random.choice(color_list))
        hirst.forward(50)
    hirst.left(90)
    hirst.forward(50)
    hirst.left(90)
    hirst.forward(500)
    hirst.setheading(0)

screen = turtle_module.Screen()
screen.exitonclick()
