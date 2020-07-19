u"""
程式設計練習題 3.3-3.6 3.19 Turtle:畫一條線.

撰寫一程式，提示使用者輸入兩個點，然後將連接成一條線，顯示點的座標，如圖3.7c所示。
"""
import ast

from turtle import Screen

from turtle import Turtle


TURTLE = Turtle()
SCREEN = Screen()

X1, Y1, X2, Y2 = ast.literal_eval(
    input("Enter six coordinates of three points \
    separated by commas like x1, y1, x2, y2: "))

TURTLE.penup()
TURTLE.goto(X1, Y1)
TURTLE.pendown()
TURTLE.write("p1(" + str(X1) + str(Y1) + ")",
             font=("Times", 18, "bold"))

TURTLE.goto(X2, Y2)
TURTLE.write("p2(" + str(X2) + str(Y2) + ")",
             font=("Times", 18, "bold"))

TURTLE.hideturtle()

SCREEN.mainloop()
