"""
程式設計練習題 1-6 1-16 Turtle:畫四個圓形.

撰寫一程式，在螢幕的中央畫四個圓形。
"""

import turtle
turtle.showturtle()
turtle.penup()
turtle.goto(0, 50)
turtle.right(90)
turtle.pendown()
turtle.circle(50)

turtle.right(180)
turtle.circle(50)

turtle.penup()
turtle.goto(0, -50)

turtle.pendown()
turtle.circle(50)

turtle.right(180)
turtle.circle(50)
