import time
import turtle
from random import *
import random

gameScreen = turtle.Screen()
gameScreen.screensize(canvwidth=600, canvheight=800)
gameScreen.bgcolor("light green")
gameScreen.title("                                                                                           Catch The Turtle Game")


sc = 0
def add_score():
    global sc
    score_title.undo()
    score_title.write("\rScore: " + str(sc), font=('arial', 15))
    sc += 1

t1 = turtle.Turtle()
t1.shape("turtle")
t1.shapesize(2, 3, 1)
t1.penup()
t1.speed(1)

score_title = turtle.Turtle(visible=False)
score_title.penup()
score_title.setposition(-55, 290)
score_title.write("Score: 0", font=('arial', 15))

def motion():
    t1.stamp()
    x_coordinate, y_coordinate = random.randint(-300, 350), random.randint(-300, 350)
    t1.goto(x_coordinate, y_coordinate)

def timer(t):
    time_title = turtle.Turtle(visible=False)
    time_title.penup()
    time_title.setposition(-55, 270)
    time_title.write("Süren Başlıyor", font=('arial', 15))
    time.sleep(1)
    while t:
        time_title.undo()
        time_title.write("\rKalan Süre " + str(t), font=('arial', 15))
        motion()
        t -= 1
    time_title.undo()
    time_title.write('\nGame Over!!!',  font=('arial', 15))

def score():
    t1.onclick(lambda x, y: add_score())
    timer(10)

score()
turtle.mainloop()
