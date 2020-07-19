"""
程式設計練習題 1-6 1-20 Turtle:畫一矩形體.

撰寫一程式，顯示矩形體。
"""
import time

from turtle import Turtle


TURTLE = Turtle()

TURTLE.showturtle()
TURTLE.penup()
TURTLE.goto(0, -45)
TURTLE.pendown()
TURTLE.circle(50)

TURTLE.penup()
TURTLE.goto(0, 0)
TURTLE.pendown()
TURTLE.right(270)
TURTLE.forward(35)

TURTLE.penup()
TURTLE.goto(0, 0)
TURTLE.forward(40)
TURTLE.pendown()
TURTLE.write("12")

TURTLE.penup()
TURTLE.goto(0, 0)
TURTLE.pendown()

TURTLE.right(90)
TURTLE.forward(30)
TURTLE.penup()

TURTLE.penup()
TURTLE.goto(0, 0)
TURTLE.forward(40)
TURTLE.pendown()
TURTLE.write("3")

TURTLE.penup()
TURTLE.goto(0, 0)
TURTLE.right(90)
TURTLE.forward(40)
TURTLE.pendown()
TURTLE.write("6")

TURTLE.penup()
TURTLE.goto(-15, 0)
TURTLE.forward(60)
TURTLE.pendown()
TURTLE.write("9:15:00")

TURTLE.penup()
TURTLE.goto(0, 0)
TURTLE.pendown()
TURTLE.right(90)
TURTLE.forward(25)

TURTLE.penup()
TURTLE.goto(0, 0)
TURTLE.forward(40)
TURTLE.pendown()
TURTLE.write("9")
TURTLE.penup()
TURTLE.goto(0, -100)

time.sleep(5)
