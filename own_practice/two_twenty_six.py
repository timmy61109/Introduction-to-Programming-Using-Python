"""
程式設計練習題 2.2-2.10 2.26 Turtel:畫一圓形.

撰寫一程式提示使用者輸入圓心、半徑。然後顯示圓形和面積。
"""
import ast

from turtle import Turtle


TURTLE = Turtle()

centerx, centery, radius = ast.literal_eval(input("輸入圓心、半徑:"))
TURTLE.showturtle()
TURTLE.penup()
TURTLE.goto(centerx, centery - radius)

TURTLE.pendown()
area = 3.141596 * radius ** 2
TURTLE.circle(radius)

TURTLE.penup()
TURTLE.goto(centerx, centery)
TURTLE.pendown()
TURTLE.write(area)
