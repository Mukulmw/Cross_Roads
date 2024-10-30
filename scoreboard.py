from turtle import Turtle
FONT = ("Courier", 24, "normal")
SCORE_BOARD_POSITION = (-60, 270)


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.player_score = 0
        self.penup()
        self.hideturtle()
        self.goto(SCORE_BOARD_POSITION)
        self.write(f"Score: {self.player_score}", font=FONT,)

    def update_score(self):
        self.clear()
        self.player_score += 1
        self.goto(SCORE_BOARD_POSITION)
        self.write(f"Score: {self.player_score}", font=FONT,)

    def game_over(self):
        self.teleport(x=-60, y=0)
        self.write(f"GAME OVER", font=FONT, )



