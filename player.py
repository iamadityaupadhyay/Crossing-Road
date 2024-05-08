from turtle import Turtle
from cars import Car
car=Car()
MOVEMENT=10
class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.penup()
        self.hideturtle()
        self.setheading(90)
        self.goto(0,-280)
        self.showturtle()
    def move(self):
        self.fd(MOVEMENT)
    def move_down(self):
      self.bk(MOVEMENT)
   
            
           
    
               
        