from turtle import Turtle
import random


class Food(Turtle): #call and inherit from the turtle class, super class

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len = 0.5, stretch_wid = 0.5)
        self.color("blue")
        self.speed("fastest")
        # rand_x= random.randint(-280, 290)
        # rand_y = random.randint(-280, 290)
        # self.goto(rand_x, rand_y) but created a new method, calling this as it will refresh each time collided
        self.refresh()


    # def __init__(self):

    #     print("rendered as a small circle")
    #     print("once snake has eaten, :")
    #     print("moved to a new location")


    def refresh(self):
        rand_x= random.randint(-280, 290)
        rand_y = random.randint(-280, 290)
        self.goto(rand_x, rand_y)
