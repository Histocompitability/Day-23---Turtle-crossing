import time
from turtle import Screen
from player import Player
from car_manager import CarManager, Car
from scoreboard import Scoreboard

def player_move():
    player.move()
    screen.update()


screen = Screen()
screen.setup(width=600, height=600)
# screen.tracer(0)
player = Player()
scoreboard = Scoreboard()
screen.update()

screen.listen()
screen.onkey(player_move, "space")
car_manager = CarManager()

game_is_on = True
while game_is_on:
    pass




    # time.sleep(0.1)
    # screen.update()


screen.exitonclick()