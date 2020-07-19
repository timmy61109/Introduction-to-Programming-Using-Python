u"""
程式設計練習題 3.3-3.6 3.16 Turtle:畫出一些形狀.

請撰寫一程式顯示笑臉的程式。
"""
from turtle import Screen

from turtle import Turtle


TURTLE = Turtle()
SCREEN = Screen()

TURTLE.pensize(3)  # Set pen thickness to 3 pixels
TURTLE.penup()  # Pull the pen up
TURTLE.goto(-200, -50)
TURTLE.left(60)  # Draw a triangle
TURTLE.pendown()  # Pull the pen down
TURTLE.begin_fill()  # Begin to fill color in a shape
TURTLE.color("red")
TURTLE.circle(40, steps=3)  # Draw a triangle
TURTLE.end_fill()  # Fill the shape

TURTLE.penup()
TURTLE.goto(-100, -50)
TURTLE.setheading(0)
TURTLE.left(45)
TURTLE.pendown()
TURTLE.begin_fill()  # Begin to fill color in a shape
TURTLE.color("blue")
TURTLE.circle(40, steps=4)  # Draw a square
TURTLE.end_fill()  # Fill the shape

TURTLE.penup()
TURTLE.goto(0, -50)
TURTLE.setheading(0)
TURTLE.left(36)
TURTLE.pendown()
TURTLE.begin_fill()  # Begin to fill color in a shape
TURTLE.color("green")
TURTLE.circle(40, steps=5)  # Draw a pentagon
TURTLE.end_fill()  # Fill the shape

TURTLE.penup()
TURTLE.goto(100, -50)
TURTLE.setheading(0)
TURTLE.left(30)
TURTLE.pendown()
TURTLE.begin_fill()  # Begin to fill color in a shape
TURTLE.color("yellow")
TURTLE.circle(40, steps=6)  # Draw a hexagon
TURTLE.end_fill()  # Fill the shape

TURTLE.penup()
TURTLE.goto(200, -50)
TURTLE.setheading(0)
TURTLE.left(22.5)
TURTLE.pendown()
TURTLE.begin_fill()  # Begin to fill color in a shape
TURTLE.color("purple")
TURTLE.circle(40, steps=8)  # Draw a circle
TURTLE.end_fill()  # Fill the shape

TURTLE.color("green")
TURTLE.penup()
TURTLE.goto(-100, 50)
TURTLE.pendown()
TURTLE.write("Cool Colorful Shapes", font=("Times", 18, "bold"))
TURTLE.hideturtle()

SCREEN.mainloop()
