import time
import turtle
from turtle import Turtle
from random import randint
#open window on screen
window=turtle.Screen()
window.title("Turtle race") 
turtle.bgcolor("darkred")
turtle.color("White")
turtle.speed(0)
turtle.penup()
turtle.setpos(-140, 200)
turtle.write("Race to 2021", font=("Verdana",30))
turtle.penup() 

#2020 dirt

turtle.setpos(-400, -180)
turtle.color("wheat")
turtle.begin_fill()
turtle.pendown()
turtle.forward(800)
turtle.right(90)
turtle.forward(300)
turtle.right(90)
turtle.forward(800)
turtle.right(90)
turtle.forward(300)
turtle.end_fill()

#2021 reaching line

stamp_size=20
square_size=15
reaching_line=200

turtle.color("wheat")
turtle.shape("square")
turtle.shapesize(square_size/stamp_size)
turtle.penup()

#drawing the finishline

for i in range(10):
    turtle.setpos(reaching_line, (150-(i * square_size*2)))
    turtle.stamp()

for j in range(10):
    turtle.setpos(reaching_line, ((150 - square_size) - (j * square_size *2)))
    turtle.stamp()

turtle.hideturtle()










