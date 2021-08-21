from turtle import Turtle

class Padle(Turtle):

    def __init__(self, x):
        super(). __init__()
        self.speed("fastest")
        self.penup()
        self.shape("square")
        self.shapesize(1, 5, 1)
        self.color("white")
        self.goto(x, 0)
        self.setheading(90)
        
    def move_up(self):
        self.forward(20)

    def move_down(self):
        self.backward(20)
