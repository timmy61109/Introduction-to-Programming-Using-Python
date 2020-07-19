"""
程式設計練習題 1-6 1-16 Turtle:畫四個圓形.

撰寫一程式，在螢幕的中央畫四個圓形。
"""

from turtle import Turtle


TURTLE = Turtle()
TURTLE.showturtle()
TURTLE.penup()
TURTLE.goto(0, 50)
TURTLE.right(90)
TURTLE.pendown()
TURTLE.circle(50)

TURTLE.right(180)
TURTLE.circle(50)

TURTLE.penup()
TURTLE.goto(0, -50)

TURTLE.pendown()
TURTLE.circle(50)

TURTLE.right(180)
TURTLE.circle(50)
