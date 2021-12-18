import time
from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard

WIDTH = 600
HEIGHT = 800

screen = Screen()
screen.setup(width=WIDTH, height=HEIGHT)
screen.bgcolor("black")
screen.title("The Amazing Snake")
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    # Detect collision with food
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        scoreboard.score_up()

    # Detect collision with wall
    if snake.head.xcor() > WIDTH/2 - 20 or snake.head.xcor() < -WIDTH/2 + 20\
            or snake.head.ycor() > HEIGHT/2 - 20 or snake.head.ycor() < -HEIGHT/2+20:
        scoreboard.reset()
        snake.reset()

    # Detect collision with tail
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 15:
            scoreboard.reset()
            snake.reset()


screen.exitonclick()
