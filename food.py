from turtle import Turtle
import random


class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(.5, .5)
        self.color("blue")
        self.speed("fastest")
        self.change_position()

    def change_position(self):
        rand_x = random.randint(-14, 14)*20
        rand_y = random.randint(-14, 14)*20
        self.goto(rand_x, rand_y)
