from turtle import Turtle

class Scoreboard(Turtle):

    def __init__(self):
        super(). __init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.goto(0, 250)
        self.write("0-0", align="center", font=("Arial", 28, "normal"))

    def score_point(self, x, y):
        self.clear()
        self.write(f"{x}-{y}", align="center", font=("Arial", 28, "normal"))