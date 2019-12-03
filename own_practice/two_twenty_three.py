"""
程式設計練習題 2.2-2.10 2.23 Turtel:畫四個圓形.

撰寫一程式提示使用者輸入半徑。然後在螢幕中心畫四個圓形，如圖2.fa。
"""
import turtle


radius = eval(input("輸入半徑:"))
turtle.showturtle()
turtle.penup()
turtle.goto(radius, 0)
turtle.pendown()
turtle.circle(radius)

turtle.penup()
turtle.goto(radius * -1, 0)
turtle.pendown()
turtle.circle(radius)

turtle.penup()
turtle.goto(radius, radius * -1 * 2)
turtle.pendown()
turtle.circle(radius)

turtle.penup()
turtle.goto(radius * -1, radius * -1 * 2)
turtle.pendown()
turtle.circle(radius)
