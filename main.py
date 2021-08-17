import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard
import g

def player_move():
    player.move()
    screen.update()


screen = Screen()
screen.setup(width=600, height=600)

screen.tracer(0)

car_manager = CarManager()
scoreboard = Scoreboard()
player = Player()

screen.listen()
screen.onkey(player_move, "space")

game_is_on = True
while game_is_on:
    time.sleep(0.02)
    car_manager.move()
    if player.check_level_up():
        car_manager.lvl_up()
        scoreboard.lvl_up()
    screen.update()




    # time.sleep(0.1)
    # screen.update()


screen.exitonclick()