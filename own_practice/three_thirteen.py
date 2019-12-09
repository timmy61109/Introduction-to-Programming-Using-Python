"""
程式設計練習題 3.3-3.6 3.12 Turtle:顯示STOP標示.

請撰寫一程式，顯示STOP標示，圖形紅色，字白色。
"""


import turtle


turtle.hideturtle()
turtle.right(60)
turtle.forward(200)
turtle.left(90)
turtle.begin_fill()
turtle.color("red")
turtle.fillcolor("red")
turtle.circle(200, steps=6)
turtle.end_fill()
turtle.home()
turtle.goto(0, -25)
turtle.color("white")
turtle.write("STOP", align="center", font=("Arial", 50, "normal"))

input("Pleace Enter")
