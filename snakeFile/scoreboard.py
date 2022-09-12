from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Arial", 10, "normal") #MAKE IT ACCESSIBLE TO CHANGE, SIMPLICITY AND ACCESIBILITY!




class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.scoreboard = 0
        self.color("white")
        self.penup()
        self.goto(0, 270)
        #self.write(f"Score: {self.scoreboard}", align = "center", font = ("Arial", 10, "normal"))
        self.hideturtle()
        self.update_score()

    def update_score(self):
        self.write(f"Score: {self.scoreboard}", align = ALIGNMENT, font = FONT)


    def game_over(self):
        self.goto(0,0)
        self.write("GAME OVER", align = ALIGNMENT, font = FONT)

    def add_score(self):
        self.scoreboard += 1
        #self.write(f"Score: {self.scoreboard}", align = "center", font = ("Arial", 10, "normal"))
        self.clear()
        self.update_score()
