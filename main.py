import time
from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard


screen = Screen()
screen.setup(600, 600)
screen.bgcolor("black")
screen.title("My snake game")
screen.tracer(0)
snake = Snake()
food = Food()
scoreboard = Scoreboard()
scoreboard.write_new_score()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

game_is_on = True
while game_is_on:
    screen.update()
    snake.move()
    time.sleep(.4)


    if snake.head.distance(food) <= 10:
        print("hit hit")
        food.change_position()
        scoreboard.change_score()
        snake.add_segment()

    if abs(snake.head.xcor()) >= 300 or abs(snake.head.ycor()) >= 300:
        print("game over")
        game_is_on = False
        scoreboard.game_over()
        time.sleep(2)
        screen.bye()

    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            print("game over")
            game_is_on = False
            scoreboard.game_over()
            time.sleep(2)
            screen.bye()








screen.exitonclick()