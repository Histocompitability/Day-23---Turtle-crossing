import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard
from game_over import Game_Over_Message

def player_move():
    player.move()


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
    screen.update()
    time.sleep(0.02)
    car_manager.move()
    if player.check_level_up():
        car_manager.lvl_up()
        scoreboard.lvl_up()
    for car in car_manager.car_bank:
        if player.distance(car) < 20 or (player.distance(car) < 28 and abs(player.position()[1] - car.position()[1]) < 2):
            game_is_on = False
            Game_Over_Message()






    # time.sleep(0.1)
    # screen.update()


screen.exitonclick()