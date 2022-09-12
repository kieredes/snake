from turtle import Screen, Turtle
import time

#use as constant, each time creating a constance, use a capital letters
START_POSITION = [(0,0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Snake:
    def __init__(self):
        self.segment = []
        self.create_snake()
        self.head = self.segment[0]

    def create_snake(self):
        for s in START_POSITION:
            # snake = Turtle(shape = "square")
            # snake.color("white")
            # new_segment = Turtle("square")#create the turtle from centre position 1.
            # new_segment.color("white")
            # new_segment.penup()# to avoid creating line, while the snake move
            # new_segment.goto(s) #2. go to this position
            # self.segment.append(new_segment) will place in add_segment method
            self.add_segment(s)


    def add_segment(self, position):
        new_segment = Turtle("square")#create the turtle from centre position 1.
        new_segment.color("white")
        new_segment.penup()# to avoid creating line, while the snake move
        new_segment.goto(position) #2. go to this position
        self.segment.append(new_segment)       

    def extend(self):
        self.add_segment(self.segments[-1].position())


    def move(self):
        for seg_num in range(len(self.segment) -1, 0, -1):
            new_x = self.segment[seg_num - 1].xcor()
            new_y = self.segment[seg_num - 1].ycor()
            self.segment[seg_num].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)

    
    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
          self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
           self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)




    
          
