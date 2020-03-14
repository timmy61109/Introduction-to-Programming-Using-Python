u"""
程式設計練習題 1-6 1-17 Turtle:畫一條線.

撰寫一程式，連接兩點(-39, 48)與(50, -50)，並且顯示這兩點的座標。
"""

from turtle import Turtle

TURTLE = Turtle()

TURTLE.showturtle()
TURTLE.penup()
TURTLE.goto(-39, 48)
TURTLE.pendown()
TURTLE.write("(-39, 48)")
TURTLE.goto(50, -50)
TURTLE.write("(50, -50)")
