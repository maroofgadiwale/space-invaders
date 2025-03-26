# Program to implement Alien class:
from turtle import Turtle,Screen
import random

IMAGE = "images/ufo.gif"

class Alien(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.s = Screen()
        self.s.addshape(IMAGE)
        self.xcord = -250
        self.flag = True
        self.direction = "left"
        self.all_alien_missiles = []
        self.all_aliens = []

    # Adding alien spaceships:
    def add_aliens(self):
        xcord = -250
        for _ in range(6):
            self.alien = Turtle()
            self.alien.penup()
            self.alien.shape(IMAGE)
            self.alien.goto(xcord,250)
            self.all_aliens.append(self.alien)
            xcord += 100

    # Moving aliens towards left and right:
    def move_aliens(self):
        if len(self.all_aliens) > 0:
            if self.direction == "left":
                for alien in self.all_aliens:
                    alien.goto(alien.xcor() - 2, alien.ycor())

                if self.all_aliens[0].xcor() <= -380:
                    self.direction = "right"

            elif self.direction == "right":
                for alien in self.all_aliens:
                    alien.goto(alien.xcor() + 2, alien.ycor())

                if self.all_aliens[-1].xcor() >= 380:
                    self.direction = "left"

    # Random shooting:
    def shoot_out(self):
        for alien in self.all_aliens:
            val = random.randint(1,100)
            if val == 65:
                self.missile = Turtle(shape="square")
                self.missile.penup()
                self.missile.color("#38ef7d")
                self.missile.shapesize(stretch_len=0.3, stretch_wid=2)
                self.missile.goto(alien.xcor(), alien.ycor() - 30)
                self.all_alien_missiles.append(self.missile)


