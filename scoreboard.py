from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    """The scoreboard of the Snake game."""
    def __init__(self):
        """Initialize the scoreboard."""
        super(Scoreboard, self).__init__()
        self.score = 0
        self.color("white")
        self.hideturtle()
        self.penup()
        self.goto(0, 260)
        self.update_scoreboard()

    def increase_score(self):
        """Increase the score."""
        self.clear()
        self.score += 1
        self.update_scoreboard()

    def decrease_score(self):
        """Decrease the score."""
        self.clear()
        self.score -= 1
        self.update_scoreboard()

    def update_scoreboard(self):
        """Updates the scoreboard to the current score."""
        self.write(f"Score: {self.score}", align=ALIGNMENT, font=FONT)

    def game_over(self):
        """Displays 'GAME OVER' in the center of the screen."""
        self.home()
        self.write("GAME OVER", align=ALIGNMENT, font=FONT)
