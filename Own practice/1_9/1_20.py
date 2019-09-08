"""
程式設計練習題 1-6 1-20 Turtle:畫一矩形體.

撰寫一程式，顯示矩形體。
"""
import turtle
import time

turtle.showturtle()
turtle.goto(50, 0)
turtle.goto(50, -40)
turtle.goto(0, -40)
turtle.goto(0, 0)

turtle.penup()
turtle.goto(10, 20)
turtle.pendown()
turtle.goto(50 + 10, 0 + 20)
turtle.goto(50 + 10, -40 + 20)
turtle.goto(0 + 10, -40 + 20)
turtle.goto(0 + 10, 0 + 20)

turtle.penup()
turtle.goto(0, 0)
turtle.pendown()
turtle.goto(10, 20)

turtle.penup()
turtle.goto(50, 0)
turtle.pendown()
turtle.goto(50 + 10, 0 + 20)

turtle.penup()
turtle.goto(50, -40)
turtle.pendown()
turtle.goto(50 + 10, -40 + 20)

turtle.penup()
turtle.goto(0, -40)
turtle.pendown()
turtle.goto(0 + 10, -40 + 20)
time.sleep(5)
