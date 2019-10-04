"""
程式設計練習題 2.2-2.10 2.26 Turtel:畫一圓形.

撰寫一程式提示使用者輸入圓心、半徑。然後顯示圓形和面積。
"""
import turtle


centerx, centery, radius = eval(input("輸入圓心、半徑:"))
turtle.showturtle()
turtle.penup()
turtle.goto(centerx, centery - radius)

turtle.pendown()
area = 3.141596 * radius ** 2
turtle.circle(radius)

turtle.penup()
turtle.goto(centerx, centery)
turtle.pendown()
turtle.write(area)
