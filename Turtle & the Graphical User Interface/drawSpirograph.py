import random
from turtle import Turtle, Screen

screen = Screen()
tim = Turtle()

# colors = ["IndianRed", "CornflowerBlue", "DarkOrchid", "DeepSkyBlue", "wheat", "SeaGreen", "blue"]
# directions = [0, 90, 180, 270]
tim.pensize(2)
tim.speed('fastest')
screen.colormode(255)


def draw_spirograph(size_of_gap):
    for _ in range(int(360/size_of_gap)):
        colors = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
        tim.pencolor(colors)
        tim.circle(200)
        current_heading = tim.heading()
        tim.setheading(current_heading + size_of_gap)
        # tim.setheading(random.choice(directions))


draw_spirograph(10)

screen.exitonclick()
