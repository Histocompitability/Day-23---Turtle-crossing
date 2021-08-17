from turtle import Turtle
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.color("black")
        self.penup()
        self.goto(-260, 240)
        self.current_level = 1
        self.write(f"level: {self.current_level}", False, "left", FONT)

    def lvl_up(self):
        self.clear()
        self.current_level += 1
        self.write(f"level: {self.current_level}", False, "left", FONT)
