"""
程式設計練習題 1-6 1-19 Turtle:畫一多邊形.

撰寫一程式，一順序連接點(40, -69.28)、(-40, -69.28)、(-80, -9.8)、(-40, 69)、(40, 69)
以及(80, 0)。

"""
import turtle
turtle.showturtle()
turtle.penup()
turtle.goto(40, -69.28)
turtle.pendown()
turtle.goto(-40, -69.28)
turtle.goto(-80, -9.8)
turtle.goto(-40, 69)
turtle.goto(40, 69)
turtle.goto(80, 0)
turtle.goto(40, -69.28)
