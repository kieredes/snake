from turtle import Screen, Turtle
import time

screen= Screen()

screen.setup(width = 600, height = 600)
screen.bgcolor("black")
screen.title("Snake Game")


#turning off tracer, for the animation
screen.tracer(0)

#creating snake body
starting_position = [(0,0), (-20, 0), (-40, 0)]


#to move the snake, start off as empty list
segment = []

for s in starting_position:
    # snake = Turtle(shape = "square")
    # snake.color("white")
    new_segment = Turtle("square")#create the turtle from centre position 1.
    new_segment.color("white")
    new_segment.penup()# to avoid creating line, while the snake move
    new_segment.goto(s) #2. go to this position
    segment.append(new_segment)

    # snake_1 = Turtle(shape = "square")
    # snake_1.color("white")
    # snake_1.goto(-20, 0) PLACED THE COMMENTED OBJECT TO A LOOP, TO SIMPLIFY THE CODE      

    # snake_2 = Turtle(shape = "square")
    # snake_2.color("white")
    # snake_2.goto(-40, 0)


#to turn on animiation, place it after the for loop of the creation of the turtle
#screen.update() commented the update and placed it inside the while loop

game_on = True

while game_on:
    screen.update() 
    time.sleep(0.1) #changed the sleep time to make it faster
    #for seg in segment: commented the for loop out to allow movements for the snake, on turning left and right
        #seg.forward(20)
        #screen.update() #commented but now, its inisde the while loop
        #time.sleep(1) # input of 1 sec delay, after each segment move, commeted to place it outside the for loop but inside the while loop
    for seg_num in range(len(segment) -1, 0, -1):
        new_x = segment[seg_num - 1].xcor()
        new_y = segment[seg_num - 1].ycor()
        segment[seg_num].goto(new_x, new_y)
    segment[0].forward(20)







screen.exitonclick()