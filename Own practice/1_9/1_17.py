"""
程式設計練習題 1-6 1-17 Turtle:畫一條線.

撰寫一程式，連接兩點(-39, 48)與(50, -50)，並且顯示這兩點的座標。
"""

import turtle
turtle.showturtle()
turtle.penup()
turtle.goto(-39, 48)
turtle.pendown()
turtle.write("(-39, 48)")
turtle.goto(50, -50)
turtle.write("(50, -50)")
