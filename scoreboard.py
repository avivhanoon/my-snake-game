from turtle import Turtle
ALIGMENT = "center"
FONT = ("Courier", 24, "normal")

class ScoreBoard (Turtle):
    def __init__(self):
        super().__init__()
        with open("data.txt") as data:
            self.highscore = int(data.read())
        self.score = 0
        self.color("white")
        self.penup()
        self.goto(x=0, y=250)
        self.hideturtle()
        self.update_scoreboard()
    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score} High Score: {self.highscore}", align=ALIGMENT, font=FONT)
    def score_up(self):
        self.score += 1
        self.update_scoreboard()
    def reset(self):
        if self.score > self.highscore:
            self.highscore = self.score
        with open("data.txt", "w") as data:
            data.write(f"{self.highscore}")
        self.score = 0
        self.update_scoreboard()
