from turtle import Turtle
ALIGMENT = "center"
FONT = ("Courier", 24, "normal")

class ScoreBoard (Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.penup()
        self.goto(x=0, y=250)
        self.hideturtle()
        self.update_scoreboard()
    def update_scoreboard(self):
        self.write(f"Score: {self.score}", align=ALIGMENT, font=FONT)
    def score_up(self):
        self.score += 1
        self.clear()
        self.update_scoreboard()
    def game_over(self):
        self.goto(0,0)
        self.write(f"game over. Final Score: {self.score}", align=ALIGMENT, font=FONT)