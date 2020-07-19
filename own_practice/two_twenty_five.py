"""
程式設計練習題 2.2-2.10 2.25 Turtel:畫矩形.

撰寫一程式提示使用者輸入中心、寬以及高。然後在螢幕顯示矩形，如圖2.fb。
"""
from turtle import Turtle

import ast

TURTLE = Turtle()


centerx, centery, width, high = ast.literal_eval(
    input("輸入中心X、中心Y、寬與高:"))
TURTLE.showturtle()
TURTLE.penup()
TURTLE.goto(centerx + width / 2, centery + high / 2)
TURTLE.pendown()

TURTLE.right(90)
TURTLE.forward(high)

TURTLE.right(90)
TURTLE.forward(width)

TURTLE.right(90)
TURTLE.forward(high)

TURTLE.right(90)
TURTLE.forward(width)
