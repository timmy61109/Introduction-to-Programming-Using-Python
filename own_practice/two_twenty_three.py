"""
程式設計練習題 2.2-2.10 2.23 Turtel:畫四個圓形.

撰寫一程式提示使用者輸入半徑。然後在螢幕中心畫四個圓形，如圖2.fa。
"""
import ast

from turtle import Turtle


TURTLE = Turtle()

RADIUS = ast.literal_eval(input("輸入半徑:"))
TURTLE.showturtle()
TURTLE.penup()
TURTLE.goto(RADIUS, 0)
TURTLE.pendown()
TURTLE.circle(RADIUS)

TURTLE.penup()
TURTLE.goto(RADIUS * -1, 0)
TURTLE.pendown()
TURTLE.circle(RADIUS)

TURTLE.penup()
TURTLE.goto(RADIUS, RADIUS * -1 * 2)
TURTLE.pendown()
TURTLE.circle(RADIUS)

TURTLE.penup()
TURTLE.goto(RADIUS * -1, RADIUS * -1 * 2)
TURTLE.pendown()
TURTLE.circle(RADIUS)
