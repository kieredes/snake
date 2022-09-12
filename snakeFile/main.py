from turtle import Screen
#removed the turtle clas from the Main file, as its being picked up from the rest of the class
import time
from snake_class import Snake
from food_snake import Food
from scoreboard import Score


screen= Screen()
screen.setup(width = 600, height = 600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)


snake = Snake()
food = Food()
scoreboard = Score()



screen.listen()#to listen for the keystroke

screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")


game_on = True
while game_on:
    screen.update() 
    time.sleep(0.1) # the screen will update every1sec

    snake.move()

    #detect collision with food.
    #using distance from turtle
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        print("collided")
        scoreboard.add_score()

    #Detect collision with wall

    if snake.head.xcor() > 280 or snake.head.xcor() <- 280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        game_on = False
        scoreboard.game_over()

    for segment in snake.segment[1:]:
        # if segment == snake.head:
        #     pass, use slicing
        if snake.head.distance(segment) < 10:
            game_on = False
            scoreboard.game_over()







screen.exitonclick()