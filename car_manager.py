from turtle import Turtle
import random
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 1
MOVE_INCREMENT = 4
NUMBER_OR_CARS = 30


class CarManager:
    def __init__(self):
        self.car_speed = STARTING_MOVE_DISTANCE
        self.car_bank = []
        for i in range(NUMBER_OR_CARS):
            c = Car()
            c.custom_x_position = random.randint(-280, 320)
            c.goto(c.custom_x_position, random.randint(-12, 12)*20)
            self.car_bank.append(c)

    def move(self):
        for car in self.car_bank:
            car.back(self.car_speed)
            if car.position()[0] < -310:
                car.goto(310, -car.position()[1])

    def lvl_up(self):
        self.car_speed += MOVE_INCREMENT


class Car(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("square")
        self.penup()
        self.shapesize(stretch_wid=0.75, stretch_len=2)
        self.color(random.choice(COLORS))


'''
trash
            for car in self.car_bank:                               #prevents cars collision
                while abs(c.custom_x_position - car.position()[0]) < 10:
                    c.custom_x_position = random.randint(-140, 160)
'''