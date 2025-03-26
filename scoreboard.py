from turtle import Turtle
import pyttsx3

class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.engine = pyttsx3.init()
        self.color("white")

    def show_score(self,val):
        self.clear()
        self.goto(0,0)
        self.write(f"{val}",font=("Helvetica",18,"bold"),align = "center")
        self.engine.say(f"{val}")
        self.engine.runAndWait()

