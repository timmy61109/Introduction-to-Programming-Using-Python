"""
程式設計練習題 2.2-2.10 2.25 Turtel:畫矩形.

撰寫一程式提示使用者輸入中心、寬以及高。然後在螢幕顯示矩形，如圖2.fb。
"""
import turtle


centerx, centery, width, high = eval(input("輸入中心X、中心Y、寬與高:"))
turtle.showturtle()
turtle.penup()
turtle.goto(centerx + width / 2, centery + high / 2)
turtle.pendown()

turtle.right(90)
turtle.forward(high)

turtle.right(90)
turtle.forward(width)

turtle.right(90)
turtle.forward(high)

turtle.right(90)
turtle.forward(width)
