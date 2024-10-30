from turtle import Turtle
FONT = ("Courier", 15, "normal")
SCORE_BOARD_POSITION = (-150, 270)


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.player_score = 0
        with open("data.txt") as data:
            self.high_score = int(data.read())
        self.penup()
        self.hideturtle()
        self.goto(SCORE_BOARD_POSITION)
        self.write(f"Score: {self.player_score} High Score: {self.high_score}", font=FONT,)

    def update_score(self):
        self.clear()
        self.player_score += 1
        self.goto(SCORE_BOARD_POSITION)
        self.write(f"Score: {self.player_score} High Score: {self.high_score}", font=FONT,)

    def game_over(self):
        if self.player_score > self.high_score:
            self.high_score = self.player_score
            with open("data.txt", mode="w") as data:
                data.write(f"{self.high_score}")
        self.teleport(x=-60, y=0)
        self.write(f"GAME OVER", font=FONT, )



