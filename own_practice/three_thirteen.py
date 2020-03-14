u"""
程式設計練習題 3.3-3.6 3.13 Turtle:顯示STOP標示.

請撰寫一程式，顯示STOP標示，圖形紅色，字白色。
"""


from turtle import Turtle


TURTLE = Turtle()

TURTLE.hideturtle()
TURTLE.right(60)
TURTLE.forward(200)
TURTLE.left(90)
TURTLE.begin_fill()
TURTLE.color("red")
TURTLE.fillcolor("red")
TURTLE.circle(200, steps=6)
TURTLE.end_fill()
TURTLE.home()
TURTLE.goto(0, -25)
TURTLE.color("white")
TURTLE.write("STOP", align="center", font=("Arial", 50, "normal"))

input("Pleace Enter")
