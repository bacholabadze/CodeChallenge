import turtle as turtle_module
import random

turtle_module.colormode(255)
tim = turtle_module.Turtle()
color_list = [
    (49, 97, 138), (254, 216, 75), (107, 151, 188), (254, 240, 181), (187, 148, 0), (86, 133, 172),
    (216, 186, 70), (140, 119, 21), (217, 228, 238), (107, 85, 0), (56, 103, 96), (255, 255, 0),
    (0, 85, 85), (32, 64, 128), (169, 194, 216)
]
tim.penup()
tim.hideturtle()
tim.setheading(225)
tim.forward(300)
tim.setheading(0)
tim.speed('fastest')
number_of_dots = 100

for dot_count in range(1, number_of_dots + 1):
    tim.dot(20, random.choice(color_list))
    tim.forward(50)

    if dot_count % 10 == 0:
        tim.setheading(90)
        tim.forward(50)
        tim.setheading(180)
        tim.forward(500)
        tim.setheading(0)

for _ in range(10):
    tim.dot(20, random.choice(color_list))
    tim.forward(50)

screen = turtle_module.Screen()
screen.exitonclick()