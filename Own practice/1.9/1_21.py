"""
程式設計練習題 1-6 1-20 Turtle:畫一矩形體.

撰寫一程式，顯示矩形體。
"""
import turtle
import time

turtle.showturtle()
turtle.penup()
turtle.goto(0, -45)
turtle.pendown()
turtle.circle(50)

turtle.penup()
turtle.goto(0, 0)
turtle.pendown()
turtle.right(270)
turtle.forward(35)

turtle.penup()
turtle.goto(0, 0)
turtle.forward(40)
turtle.pendown()
turtle.write("12")

turtle.penup()
turtle.goto(0, 0)
turtle.pendown()

turtle.right(90)
turtle.forward(30)
turtle.penup()

turtle.penup()
turtle.goto(0, 0)
turtle.forward(40)
turtle.pendown()
turtle.write("3")

turtle.penup()
turtle.goto(0, 0)
turtle.right(90)
turtle.forward(40)
turtle.pendown()
turtle.write("6")

turtle.penup()
turtle.goto(-15, 0)
turtle.forward(60)
turtle.pendown()
turtle.write("9:15:00")

turtle.penup()
turtle.goto(0, 0)
turtle.pendown()
turtle.right(90)
turtle.forward(25)

turtle.penup()
turtle.goto(0, 0)
turtle.forward(40)
turtle.pendown()
turtle.write("9")
turtle.penup()
turtle.goto(0, -100)

time.sleep(5)
