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
        self.high_score = 0
        self.write_new_score()

    def write_new_score(self):
        self.clear()
        argument = f"Score: {self.score} High Score: {self.high_score}"
        self.write(argument, False, "center", FONT)

    # def game_over(self):
    #     self.home()
    #     self.write("Game Over", False, "center", FONT)

    def reset_game(self):
        if self.score > self.high_score:
            self.high_score = self.score
        self.score = 0
        self.write_new_score()

    def change_score(self):
        self.score += 1
        self.write_new_score()
