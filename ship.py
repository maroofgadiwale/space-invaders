# Program to implement Ship class:
from aliens import Alien
from turtle import Turtle,Screen

IMAGE = "images/spaceship.gif"
class Ship(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.s = Screen()
        self.s.addshape(IMAGE)
        self.shape(IMAGE)
        self.y = -250
        self.goto(0,self.y)
        self.missiles = []

    # Moving Left:
    def move_left(self):
        if self.xcor() > - 350:
            self.x = self.xcor()-20
            self.goto(self.x,self.y)

    # Moving Right:
    def move_right(self):
        if self.xcor() < 350:
            self.x = self.xcor()+20
            self.goto(self.x,self.y)

    # Shooting:
    def shoot(self):
         self.missile = Turtle(shape="square")
         self.missile.penup()
         self.missile.color("yellow")
         self.missile.shapesize(stretch_len=0.3,stretch_wid=2)
         self.missile.goto(self.xcor(),-200)
         self.missiles.append(self.missile)

    def move_missile(self):
        if len(self.missiles) > 0:
            for missile in self.missiles:
                missile.goto(missile.xcor(),missile.ycor()+10)
                if missile.ycor() > 350:
                    missile.clear()



