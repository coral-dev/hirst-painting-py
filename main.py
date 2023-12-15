import random

import colorgram
import turtle as turtle_module

rgb_colors = []
colors = colorgram.extract('painting.jpg', 30)

for color in colors:
    r = color.rgb.r
    g = color.rgb.g
    b = color.rgb.b
    rgb_color = (r, g, b)
    rgb_colors.append(rgb_color)

rgb_colors.remove(rgb_colors[0])
rgb_colors.remove(rgb_colors[1])

number_of_dots = 100
turtle_module.colormode(255)
tim = turtle_module.Turtle()
tim.speed('fastest')
tim.penup()
tim.hideturtle()
tim.setheading(225)
tim.forward(300)
tim.setheading(0)

for dot_count in range(1, number_of_dots + 1):
    tim.forward(50)
    tim.dot(20, random.choice(rgb_colors))
    if dot_count % 10 == 0:
        tim.setheading(90)
        tim.forward(50)
        tim.setheading(180)
        tim.forward(500)
        tim.setheading(0)

screen = turtle_module.Screen()
screen.exitonclick()