from turtle import Turtle

STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

TRIANGLE = "triangle"
CLASSIC = "classic"


class Snake:
    """A snake that moves and gets longer as it eats food."""
    def __init__(self):
        """Initialize a new Snake instance."""
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):
        """Create the snake that the player starts with."""
        self.add_segment(STARTING_POSITIONS[0], TRIANGLE)
        for position in STARTING_POSITIONS[1:]:
            self.add_segment(position)

    def add_segment(self, position, shape=CLASSIC):
        """Add a new segment to the snake."""
        new_segment = Turtle(shape)
        new_segment.penup()
        new_segment.color("white")
        new_segment.goto(position)
        self.segments.append(new_segment)

    def extend(self):
        """Add a new segment of the snake at the end of the snake."""
        # Place the new segment at the same position as the last segment of the snake
        self.add_segment(self.segments[-1].position())

    def move(self):
        """Move the snake to follow the head."""
        # Place the segment of the snake to the segment before it starting from the end of the snake
        for seg_num in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            new_heading = self.segments[seg_num - 1].heading()
            self.segments[seg_num].goto(new_x, new_y)
            self.segments[seg_num].setheading(new_heading)
        # Move the snake head forward
        self.head.forward(MOVE_DISTANCE)

    def up(self):
        """Move the snake head up."""
        # Prevents moving backwards
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        """Move the snake head down."""
        # Prevents moving backwards
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        """Move the snake head left."""
        # Prevents moving backwards
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        """Move the snake head right."""
        # Prevents moving backwards
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
