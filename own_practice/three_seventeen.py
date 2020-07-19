u"""
程式設計練習題 3.3-3.6 3.17 Turtle:三角形面積.

請撰寫一程式，提示使用者輸入三角形的三個點p1、p2、p3，然後再三角形下面顯示面積，如圖3.7a所示。
計算三角形面積的公式請參閱程式設計練習題2.14。
"""
import ast

from turtle import Screen

from turtle import Turtle


TURTLE = Turtle()
SCREEN = Screen()

X1, y1, X2, y2, X3, y3 = ast.literal_eval(
    input("Enter three points for a triangle:"))

SIDE1 = ((X1 - X2) ** 2 + (y1 + y2) ** 2) ** 0.5
SIDE2 = ((X2 - X3) ** 2 + (y2 + y3) ** 2) ** 0.5
SIDE3 = ((X1 - X3) ** 2 + (y1 + y3) ** 2) ** 0.5

s = (SIDE1 + SIDE2 + SIDE3) / 2
AREA = (s * (s - SIDE1) * (s - SIDE2) * (s - SIDE3)) ** 0.5

TURTLE.penup()
TURTLE.goto(X1, y1)
TURTLE.pendown()
TURTLE.write("p1(" + str(X1) + "," + str(y1) + ")",
             font=("Times", 18, "bold"))

TURTLE.goto(X2, y2)
TURTLE.write("p2(" + str(X2) + "," + str(y2) + ")",
             font=("Times", 18, "bold"))

TURTLE.goto(X3, y3)
TURTLE.write("p3(" + str(X3) + "," + str(y3) + ")",
             font=("Times", 18, "bold"))

TURTLE.goto(X1, y1)

TURTLE.penup()
TURTLE.goto(0, min(y1, y2, y3) - 50)
TURTLE.pendown()
TURTLE.write("The area of the triangle is" + str(AREA),
             font=("Times", 18, "bold"))

TURTLE.hideturtle()

SCREEN.mainloop()
