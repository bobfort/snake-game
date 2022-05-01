from turtle import Turtle

ALIGNMENT = 'Center'
FONT = ('Courier', 20, 'normal')


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.color('white')
        self.penup()
        self.score = 0
        self.speed('fastest')
        self.goto(0, 260)

    def show_score(self):
        self.clear()
        self.write(f"score: {self.score} ", False, align=ALIGNMENT, font=FONT)

    def add_score(self):
        self.score += 1

    def game_over(self):
        self.goto(0, 0)
        self.write("game over :(", False, align=ALIGNMENT, font=FONT)
