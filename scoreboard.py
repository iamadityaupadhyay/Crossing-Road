from turtle import Turtle
class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.color("black")
        self.goto(-50, 0)
    def game_over(self):
        self.write("Game Over" ,font=("Arial", 20, "normal"))
        
        