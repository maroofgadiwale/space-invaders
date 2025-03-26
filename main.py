# Program to implement space invaders game:
from turtle import Screen
from ship import Ship
from aliens import Alien
from scoreboard import ScoreBoard
import time
from wallmanager import Wall

# Adding screen setup:
screen = Screen()
screen.setup(width = 800,height = 600)
screen.title("space-invaders-marfii")
screen.bgcolor("black")
screen.tracer(0)

# User ship creation:
myship = Ship()

# Keyboard funs:
screen.listen()
screen.onkeypress(key = "Left",fun=myship.move_left)
screen.onkeypress(key = "Right",fun=myship.move_right)
screen.onkeypress(key = "space",fun = myship.shoot)

# For aliens:
alien = Alien()
alien.add_aliens()

# For arranging walls:
wall = Wall()
wall.create_walls(64)

flag = True
score_cnt = 0
board = ScoreBoard()

while flag:
    time.sleep(0.01)
    screen.update()
    # Game over condition:
    if len(alien.all_aliens) == 0:
        board.show_score(f"Victory! your score was {score_cnt}")
        flag = False

    # Detecting collision with weapon:
    for missile in myship.missiles:
        for villain in alien.all_aliens:
            if missile.distance(villain) < 50:
                villain.ht()
                missile.ht()
                score_cnt += 100
                alien.all_aliens.remove(villain)

    alien.move_aliens()
    alien.shoot_out()

    # Moving all alien missiles and detecting collison with ship:
    for missile in alien.all_alien_missiles:
        missile.goto(missile.xcor(),missile.ycor()-10)
        if missile.distance(myship) < 50:
            myship.reset()
            board.show_score(f"Game Over! Alien ship destroyed your ship!")
            flag = False

    # Detecting collision of alien missiles with walls:
    for missile in alien.all_alien_missiles:
        for block in wall.all_walls:
            if missile.distance(block) < 25:
                missile.reset()
                block.reset()

    # Detecting collision with hero's missile:
    for missile in myship.missiles:
        for block in wall.all_walls:
            if missile.distance(block) < 25:
                missile.reset()
                block.reset()

    myship.move_missile()
screen.exitonclick()