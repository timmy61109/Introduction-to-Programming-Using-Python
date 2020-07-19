u"""
程式設計練習題 1-6 1-19 Turtle:畫一多邊形.

撰寫一程式，一順序連接點(40, -69.28)、(-40, -69.28)、(-80, -9.8)、(-40, 69)、(40, 69)
以及(80, 0)。

"""
from turtle import Turtle


TURTLE = Turtle()

TURTLE.showturtle()
TURTLE.penup()
TURTLE.goto(40, -69.28)
TURTLE.pendown()
TURTLE.goto(-40, -69.28)
TURTLE.goto(-80, -9.8)
TURTLE.goto(-40, 69)
TURTLE.goto(40, 69)
TURTLE.goto(80, 0)
TURTLE.goto(40, -69.28)
