from turtle import Turtle
import random
COLOR = ["red","blue","orange","green","black","pink"]
class Car(Turtle):
    def __init__(self):
        self.all_cars=[]
    def player_car(self): 
        tigdambazi=random.randint(1,6)
        if tigdambazi==1:
            newCar=Turtle("square") 
            newCar.shapesize(stretch_wid=0.8,stretch_len=2)
            newCar.penup()
            random_y=random.randint(-280,280)
            newCar.goto(280,random_y)
            newCar.color(random.choice(COLOR))
            # newCar.speed("0.1")
            self.all_cars.append(newCar)
    def car_move(self):
        for car in self.all_cars:
            car.bk(3)
        # for car in self.all_cars:
        #    print(car.xcor())
    
    # def moving(self):
        