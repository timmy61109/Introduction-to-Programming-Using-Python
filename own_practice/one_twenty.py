"""
程式設計練習題 1-6 1-20 Turtle:畫一矩形體.

撰寫一程式，顯示矩形體。
"""
import time

from turtle import Turtle


TURTLE = Turtle()

TURTLE.showturtle()
TURTLE.goto(50, 0)
TURTLE.goto(50, -40)
TURTLE.goto(0, -40)
TURTLE.goto(0, 0)

TURTLE.penup()
TURTLE.goto(10, 20)
TURTLE.pendown()
TURTLE.goto(50 + 10, 0 + 20)
TURTLE.goto(50 + 10, -40 + 20)
TURTLE.goto(0 + 10, -40 + 20)
TURTLE.goto(0 + 10, 0 + 20)

TURTLE.penup()
TURTLE.goto(0, 0)
TURTLE.pendown()
TURTLE.goto(10, 20)

TURTLE.penup()
TURTLE.goto(50, 0)
TURTLE.pendown()
TURTLE.goto(50 + 10, 0 + 20)

TURTLE.penup()
TURTLE.goto(50, -40)
TURTLE.pendown()
TURTLE.goto(50 + 10, -40 + 20)

TURTLE.penup()
TURTLE.goto(0, -40)
TURTLE.pendown()
TURTLE.goto(0 + 10, -40 + 20)
time.sleep(5)
