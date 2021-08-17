from turtle import Turtle
import random
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10
NUMBER_OR_CARS = 30


class CarManager:
    def __init__(self):
        self.car_bank = []
        self.car_speed = STARTING_MOVE_DISTANCE
        for i in range (NUMBER_OR_CARS):
            c = Car()
            c.goto(random.randint(-140, 160), random.randint(-6, 7)*20)
            self.car_bank.append(c)


    def move(self):
        for car in self.car_bank:
            car.back(self.car_speed)

    def lvl_up(self):
        self.car_speed += MOVE_INCREMENT





class Car(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("square")
        self.shapesize(stretch_wid=1, stretch_len= 2)
        self.color(random.choice(COLORS))





