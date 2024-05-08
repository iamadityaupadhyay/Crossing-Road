from turtle import Turtle,Screen
import time
from player import Player
from cars import Car
from scoreboard import Scoreboard
car=Car()
score=Scoreboard()


player=Player()
# turtle=Turtle()
screen=Screen()
screen.setup(600,600)
screen.tracer(0)
screen.listen()
player.fd(100)
screen.onkeypress(player.move,"Up")
screen.onkeypress(player.move_down,"Down")
game_is_on=True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    car.player_car()
    car.car_move()
    for cars in car.all_cars:
        if cars.distance(player)<15:
            score.game_over()
            
            
if player.ycor()>280:
        print("The turtle has crossed all the cars Successfully ! ! !")   
    
  