from turtle import Turtle
import time
STARTING_POSITION = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DIST = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake():

    def __init__(self):
        self.segments = []
        self.segments_xcor_list = []
        self.create_snake()
        self.head = self.segments[0]


    def create_snake(self):
        for position in STARTING_POSITION:
            new_seg = Turtle(shape="square")
            new_seg.penup()
            new_seg.color("white")
            new_seg.goto(position)
            self.segments.append(new_seg)


    def move(self):
        for seg_num in range(len(self.segments) - 1, 0, -1):
            x_to_go = self.segments[seg_num - 1].xcor()
            y_to_go = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(x_to_go, y_to_go)
        self.head.forward(MOVE_DIST)

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

    def add_segment(self):
        seg_position = self.segments[-1].position()
        new_seg = Turtle(shape="square")
        new_seg.penup()
        new_seg.color("white")
        new_seg.goto(seg_position)
        self.segments.append(new_seg)

    def reset_snake(self):
        time.sleep(1)
        for seg in self.segments:
            seg.goto(1000, 1000)

        self.segments.clear()
        self.create_snake()
        self.head = self.segments[0]







