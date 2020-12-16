from turtle import Turtle
import random

TURTLE_SHAPE = "turtle"
TURTLE_COLOR = "dodger blue"


class Food(Turtle):
    """The food that a snake can eat"""
    def __init__(self):
        """Initialize the food and its placement."""
        super(Food, self).__init__()
        self.shape(TURTLE_SHAPE)
        self.penup()
        # self.shapesize(stretch_len=0.75, stretch_wid=0.75)
        self.color(TURTLE_COLOR)
        self.speed("fastest")
        self.refresh()

    def refresh(self):
        """Randomly change the position of the food."""
        random_x = random.randint(-280, 280)
        random_y = random.randint(-280, 280)
        self.goto(random_x, random_y)
