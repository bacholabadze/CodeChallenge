from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()
angle = 0


def move_forward():
    tim.forward(10)


def move_backward():
    tim.forward(-10)


def turn_right():
    global angle
    angle -= 10
    tim.setheading(angle)


def turn_left():
    global angle
    angle += 10
    tim.setheading(angle)


def clear_screen():
    tim.clear()
    tim.penup()
    tim.home()
    tim.pendown()

screen.listen()
screen.onkey(key='w', fun=move_forward)
screen.onkey(key='s', fun=move_backward)
screen.onkey(key='a', fun=turn_left)
screen.onkey(key='d', fun=turn_right)
screen.onkey(key='c', fun=clear_screen)


screen.exitonclick()
