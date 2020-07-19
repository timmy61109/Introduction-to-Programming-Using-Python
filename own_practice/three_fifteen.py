u"""
程式設計練習題 3.3-3.6 3.15 Turtle:畫出一笑臉.

請撰寫一程式顯示笑臉的程式。
"""
from turtle import Screen

from turtle import Turtle


TURTLE = Turtle()
SCREEN = Screen()

TURTLE.hideturtle()

TURTLE.penup()
TURTLE.goto(0, -200)
TURTLE.pendown()
TURTLE.circle(200)

TURTLE.penup()
TURTLE.goto(80, 40)
TURTLE.pendown()
TURTLE.begin_fill()
TURTLE.color("red")
TURTLE.fillcolor("red")
TURTLE.circle(20)
TURTLE.end_fill()

TURTLE.penup()
TURTLE.goto(-80, 40)
TURTLE.pendown()
TURTLE.begin_fill()
TURTLE.color("red")
TURTLE.fillcolor("red")
TURTLE.circle(20)
TURTLE.end_fill()

TURTLE.penup()
TURTLE.goto(0, 0)
TURTLE.pendown()
TURTLE.color("black")
TURTLE.dot()

TURTLE.penup()
TURTLE.goto(60, -(60 * (3 ** 0.5)) / 3)
TURTLE.left(60)
TURTLE.pendown()
TURTLE.color("black")
TURTLE.circle((120 * (3 ** 0.5)) / 3, steps=3)

TURTLE.penup()
TURTLE.goto(0, (-(120 * (3 ** 0.5)) / 3) * 2)
TURTLE.pendown()
TURTLE.right(30)
TURTLE.forward((240 * (3 ** 0.5)) / 3 + 10)

TURTLE.penup()
TURTLE.goto(0, (-(120 * (3 ** 0.5)) / 3) * 2)
TURTLE.pendown()
TURTLE.left(120)
TURTLE.forward((240 * (3 ** 0.5)) / 3 + 10)

SCREEN.mainloop()
