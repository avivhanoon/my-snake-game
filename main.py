from turtle import Screen
from Snake import Snake
from food import Food
from scoreboard import ScoreBoard
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("MY SNAKE GAME")
screen.tracer(0)
game_is_on = True
snake = Snake()
food = Food()
scoreboard = ScoreBoard()
screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.right, "Right")
screen.onkey(snake.left, "Left")
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    if snake.head.distance(food) < 15:
        print("num num num")
        food.refresh()
        scoreboard.score_up()
        snake.extends()

    #detect hitting the wall
    if (snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor()
            > 280 or snake.head.ycor() < -280):
        game_is_on = False
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            game_is_on = False
scoreboard.game_over()
screen.exitonclick()
