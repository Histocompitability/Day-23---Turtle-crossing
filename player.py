from turtle import Turtle
STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.penup()
        self.setheading(90)
        self.speed("fastest")
        self.goto(STARTING_POSITION)
        self.difficulty_level = 1

    def move(self):
        self.fd(MOVE_DISTANCE)

    def check_level_up(self):
        if self.position()[1] >= FINISH_LINE_Y:
            self.goto(STARTING_POSITION)
            return True


