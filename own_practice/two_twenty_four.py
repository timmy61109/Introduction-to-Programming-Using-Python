"""
程式設計練習題 2.2-2.10 2.24 Turtel:畫四個六邊形.

撰寫一程式在螢幕中心畫四個六邊形，如圖2.fb。
"""
from turtle import Turtle


TURTLE = Turtle()


RADIUS = 50
TURTLE.showturtle()
TURTLE.penup()
TURTLE.forward(RADIUS / 2)
TURTLE.left(90)
TURTLE.forward(RADIUS / 2)
TURTLE.pendown()

TURTLE.forward(RADIUS)
TURTLE.right(60)

TURTLE.forward(RADIUS)
TURTLE.right(60)

TURTLE.forward(RADIUS)
TURTLE.right(60)

TURTLE.forward(RADIUS)
TURTLE.right(60)

TURTLE.forward(RADIUS)
TURTLE.right(60)

TURTLE.forward(RADIUS)
TURTLE.right(60)

TURTLE.penup()
TURTLE.left(90)
TURTLE.forward(RADIUS * (2 * (3 ** 0.5) + 1))
TURTLE.right(90)
TURTLE.pendown()

TURTLE.forward(RADIUS)
TURTLE.right(60)

TURTLE.forward(RADIUS)
TURTLE.right(60)

TURTLE.forward(RADIUS)
TURTLE.right(60)

TURTLE.forward(RADIUS)
TURTLE.right(60)

TURTLE.forward(RADIUS)
TURTLE.right(60)

TURTLE.forward(RADIUS)
TURTLE.right(60)

TURTLE.penup()
TURTLE.left(180)
TURTLE.forward(RADIUS * 2)
TURTLE.left(180)
TURTLE.pendown()

TURTLE.forward(RADIUS)
TURTLE.right(60)

TURTLE.forward(RADIUS)
TURTLE.right(60)

TURTLE.forward(RADIUS)
TURTLE.right(60)

TURTLE.forward(RADIUS)
TURTLE.right(60)

TURTLE.forward(RADIUS)
TURTLE.right(60)

TURTLE.forward(RADIUS)
TURTLE.right(60)

TURTLE.penup()
TURTLE.right(90)
TURTLE.forward(RADIUS * (2 * (3 ** 0.5) + 1))
TURTLE.left(90)
TURTLE.pendown()

TURTLE.forward(RADIUS)
TURTLE.right(60)

TURTLE.forward(RADIUS)
TURTLE.right(60)

TURTLE.forward(RADIUS)
TURTLE.right(60)

TURTLE.forward(RADIUS)
TURTLE.right(60)

TURTLE.forward(RADIUS)
TURTLE.right(60)

TURTLE.forward(RADIUS)
TURTLE.right(60)
