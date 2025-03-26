# Program to implement Wall class:
from turtle import Turtle
import random

class Wall(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.all_walls = []

    def create_walls(self,wcnt):
        xcord,ycord = -375,80
        for i in range(wcnt):
            if i % 16 == 0:
                ycord -= 30
                xcord = -375
            wall = Turtle(shape="square")
            wall.penup()
            wall.color(random.choice(["#ED213A","#FDC830","#605C3C","#00B4DB"]))
            wall.shapesize(stretch_len=2,stretch_wid=1)
            wall.goto(xcord,ycord)
            self.all_walls.append(wall)
            xcord += 50
