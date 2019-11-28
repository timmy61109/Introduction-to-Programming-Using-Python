"""
程式設計練習題 2.2-2.10 2.24 Turtel:畫四個六邊形.

撰寫一程式在螢幕中心畫四個六邊形，如圖2.fb。
"""
import turtle


radius = 50
turtle.showturtle()
turtle.penup()
turtle.forward(radius / 2)
turtle.left(90)
turtle.forward(radius / 2)
turtle.pendown()

turtle.forward(radius)
turtle.right(60)

turtle.forward(radius)
turtle.right(60)

turtle.forward(radius)
turtle.right(60)

turtle.forward(radius)
turtle.right(60)

turtle.forward(radius)
turtle.right(60)

turtle.forward(radius)
turtle.right(60)

turtle.penup()
turtle.left(90)
turtle.forward(radius * (2 * (3 ** 0.5) + 1))
turtle.right(90)
turtle.pendown()

turtle.forward(radius)
turtle.right(60)

turtle.forward(radius)
turtle.right(60)

turtle.forward(radius)
turtle.right(60)

turtle.forward(radius)
turtle.right(60)

turtle.forward(radius)
turtle.right(60)

turtle.forward(radius)
turtle.right(60)

turtle.penup()
turtle.left(180)
turtle.forward(radius * 2)
turtle.left(180)
turtle.pendown()

turtle.forward(radius)
turtle.right(60)

turtle.forward(radius)
turtle.right(60)

turtle.forward(radius)
turtle.right(60)

turtle.forward(radius)
turtle.right(60)

turtle.forward(radius)
turtle.right(60)

turtle.forward(radius)
turtle.right(60)

turtle.penup()
turtle.right(90)
turtle.forward(radius * (2 * (3 ** 0.5) + 1))
turtle.left(90)
turtle.pendown()

turtle.forward(radius)
turtle.right(60)

turtle.forward(radius)
turtle.right(60)

turtle.forward(radius)
turtle.right(60)

turtle.forward(radius)
turtle.right(60)

turtle.forward(radius)
turtle.right(60)

turtle.forward(radius)
turtle.right(60)
