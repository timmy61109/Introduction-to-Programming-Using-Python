"""
程式設計練習題 3.3-3.6 3.14 Turtle:畫出奧林匹亞的圖樣.

請撰寫一程式，提示使用者輸入環形的半徑，以相同的大小畫出欄、黑、紅、黃以及綠色的色環。
"""
from turtle import Screen

from turtle import Turtle


SIZE = int(input("Enter the size:"))
X_SCALING_FACTOR = SIZE * 10 / 45
Y_SCALING_FACTOR = SIZE * 5 / 9
Y2_SCALING_FACTOR = SIZE * 2 / 3
PENSIZE = SIZE * 2 / 9

TURTLE = Turtle()
SCREEN = Screen()

TURTLE.pensize(PENSIZE)
TURTLE.color("blue")
TURTLE.penup()
TURTLE.goto(- (X_SCALING_FACTOR * 2 + SIZE * 2), -Y_SCALING_FACTOR)
TURTLE.pendown()
TURTLE.circle(SIZE)

TURTLE.color("black")
TURTLE.penup()
TURTLE.goto(0, -Y_SCALING_FACTOR)
TURTLE.pendown()
TURTLE.circle(SIZE)

TURTLE.color("red")
TURTLE.penup()
TURTLE.goto(X_SCALING_FACTOR * 2 + SIZE * 2, -Y_SCALING_FACTOR)
TURTLE.pendown()
TURTLE.circle(SIZE)

TURTLE.color("yellow")
TURTLE.penup()
TURTLE.goto(-SIZE - X_SCALING_FACTOR, - SIZE - Y2_SCALING_FACTOR)
TURTLE.pendown()
TURTLE.circle(SIZE)

TURTLE.color("green")
TURTLE.penup()
TURTLE.goto(SIZE + X_SCALING_FACTOR, - SIZE - Y2_SCALING_FACTOR)
TURTLE.pendown()
TURTLE.circle(SIZE)

SCREEN.mainloop()
