from turtle import Turtle
import time

ALIGNMENT = "center"
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    """The scoreboard of the Snake game."""
    def __init__(self, name):
        """Initialize the scoreboard."""
        super(Scoreboard, self).__init__()
        self.name = name
        self.score = 0
        self.escaped_turtles = 0
        self.color("white")
        self.hideturtle()
        self.penup()
        self.countdown()
        self.update_scoreboard()

    def countdown(self):
        self.home()
        for sec in range(3, 0, -1):
            self.write(f"{sec}", align=ALIGNMENT, font=FONT)
            time.sleep(1)
            self.clear()

    def increase_score(self):
        """Increase the score."""
        self.clear()
        self.score += 1
        self.update_scoreboard()

    def decrease_score(self):
        """Decrease the score and increase the number of escaped turtles."""
        self.clear()
        self.score -= 1
        self.escaped_turtles += 1
        self.update_scoreboard()

    def update_scoreboard(self):
        """Updates the scoreboard to the current score."""
        self.goto(0, 260)
        self.write(f"{self.name}'s Score: {self.score}", align=ALIGNMENT, font=FONT)
        self.goto(0, 220)
        self.write(f"Escaped turtles: {self.escaped_turtles}", align=ALIGNMENT, font=FONT)

    def game_over(self):
        """Displays 'GAME OVER' in the center of the screen."""
        self.home()
        self.write("GAME OVER", align=ALIGNMENT, font=FONT)
