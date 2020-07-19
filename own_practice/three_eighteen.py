u"""
程式設計練習題 3.3-3.6 3.18 Turtle:三角形角度.

重新修改範例程式3.2 ComputeAngles.py，提示使用者輸入三角形的三個點p1、p2、p3，然後顯示其角
度，如圖3.7b所示。
"""
import ast

import math

from turtle import Screen

from turtle import Turtle


TURTLE = Turtle()
SCREEN = Screen()

X1, Y1, X2, Y2, X3, Y3 = ast.literal_eval(
    input("Enter six coordinates of three points \
    separated by commas like x1, y1, x2, y2, x3, y3: "))

a = math.sqrt((X2 - X3) * (X2 - X3) + (Y2 - Y3) * (Y2 - Y3))
b = math.sqrt((X1 - X3) * (X1 - X3) + (Y1 - Y3) * (Y1 - Y3))
c = math.sqrt((X1 - X2) * (X1 - X2) + (Y1 - Y2) * (Y1 - Y2))

A = math.degrees(math.acos((a * a - b * b - c * c) / (-2 * b * c)))
B = math.degrees(math.acos((b * b - a * a - c * c) / (-2 * a * c)))
C = math.degrees(math.acos((c * c - b * b - a * a) / (-2 * a * b)))

TURTLE.penup()
TURTLE.goto(X1, Y1)
TURTLE.pendown()
TURTLE.write("p1(" + str(A) + ")",
             font=("Times", 18, "bold"))

TURTLE.goto(X2, Y2)
TURTLE.write("p2(" + str(B) + ")",
             font=("Times", 18, "bold"))

TURTLE.goto(X3, Y3)
TURTLE.write("p3(" + str(C) + ")",
             font=("Times", 18, "bold"))

TURTLE.goto(X1, Y1)

TURTLE.hideturtle()

SCREEN.mainloop()
