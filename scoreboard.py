from turtle import Turtle
FONT = ("Courier", 14, "normal")

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.color("white")
        self.goto(0, 280)
        self.score = 0

    def write_new_score(self):
        argument = f"Score: {self.score}"
        self.write(argument, False, "center", FONT)

    def game_over(self):
        self.home()
        self.write("Game Over", False, "center", FONT)

    def change_score(self):
        self.clear()
        self.score += 1
        self.write_new_score()