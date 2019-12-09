"""
程式設計練習題 3.3-3.6 3.12 Turtle:畫星星.

請撰寫一程式，提示使用者輸入星星的大小並加以畫出。(提示:星星每一點的內角為36度)
"""


import turtle


NUMBER = int(input("Enter star size:"))


turtle.showturtle()
turtle.penup()

turtle.left(90)
turtle.forward(NUMBER)
turtle.pendown()
turtle.left(162)
turtle.forward(NUMBER)
turtle.penup()
turtle.home()

turtle.left(162)
turtle.forward(NUMBER)
turtle.pendown()
turtle.left(162)
turtle.forward(NUMBER)
turtle.penup()
turtle.home()

turtle.left(234)
turtle.forward(NUMBER)
turtle.pendown()
turtle.left(162)
turtle.forward(NUMBER)
turtle.penup()
turtle.home()

turtle.left(306)
turtle.forward(NUMBER)
turtle.pendown()
turtle.left(162)
turtle.forward(NUMBER)
turtle.penup()
turtle.home()

turtle.left(378)
turtle.forward(NUMBER)
turtle.pendown()
turtle.left(162)
turtle.forward(NUMBER)
turtle.penup()
turtle.home()

turtle.left(90)
turtle.forward(NUMBER)
turtle.pendown()
turtle.right(162)
turtle.forward(NUMBER)
turtle.penup()
turtle.home()

turtle.left(162)
turtle.forward(NUMBER)
turtle.pendown()
turtle.right(162)
turtle.forward(NUMBER)
turtle.penup()
turtle.home()

turtle.left(234)
turtle.forward(NUMBER)
turtle.pendown()
turtle.right(162)
turtle.forward(NUMBER)
turtle.penup()
turtle.home()

turtle.left(306)
turtle.forward(NUMBER)
turtle.pendown()
turtle.right(162)
turtle.forward(NUMBER)
turtle.penup()
turtle.home()

turtle.left(378)
turtle.forward(NUMBER)
turtle.pendown()
turtle.right(162)
turtle.forward(NUMBER)
turtle.penup()
turtle.home()

input("Pleace Enter key")
