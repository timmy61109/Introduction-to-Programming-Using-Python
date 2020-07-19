"""
程式設計練習題 3.3-3.6 3.12 Turtle:畫星星.

請撰寫一程式，提示使用者輸入星星的大小並加以畫出。(提示:星星每一點的內角為36度)
"""
from turtle import Turtle


TURTLE = Turtle()

NUMBER = int(input("Enter star size:"))


TURTLE.showturtle()
TURTLE.penup()

TURTLE.left(90)
TURTLE.forward(NUMBER)
TURTLE.pendown()
TURTLE.left(162)
TURTLE.forward(NUMBER)
TURTLE.penup()
TURTLE.home()

TURTLE.left(162)
TURTLE.forward(NUMBER)
TURTLE.pendown()
TURTLE.left(162)
TURTLE.forward(NUMBER)
TURTLE.penup()
TURTLE.home()

TURTLE.left(234)
TURTLE.forward(NUMBER)
TURTLE.pendown()
TURTLE.left(162)
TURTLE.forward(NUMBER)
TURTLE.penup()
TURTLE.home()

TURTLE.left(306)
TURTLE.forward(NUMBER)
TURTLE.pendown()
TURTLE.left(162)
TURTLE.forward(NUMBER)
TURTLE.penup()
TURTLE.home()

TURTLE.left(378)
TURTLE.forward(NUMBER)
TURTLE.pendown()
TURTLE.left(162)
TURTLE.forward(NUMBER)
TURTLE.penup()
TURTLE.home()

TURTLE.left(90)
TURTLE.forward(NUMBER)
TURTLE.pendown()
TURTLE.right(162)
TURTLE.forward(NUMBER)
TURTLE.penup()
TURTLE.home()

TURTLE.left(162)
TURTLE.forward(NUMBER)
TURTLE.pendown()
TURTLE.right(162)
TURTLE.forward(NUMBER)
TURTLE.penup()
TURTLE.home()

TURTLE.left(234)
TURTLE.forward(NUMBER)
TURTLE.pendown()
TURTLE.right(162)
TURTLE.forward(NUMBER)
TURTLE.penup()
TURTLE.home()

TURTLE.left(306)
TURTLE.forward(NUMBER)
TURTLE.pendown()
TURTLE.right(162)
TURTLE.forward(NUMBER)
TURTLE.penup()
TURTLE.home()

TURTLE.left(378)
TURTLE.forward(NUMBER)
TURTLE.pendown()
TURTLE.right(162)
TURTLE.forward(NUMBER)
TURTLE.penup()
TURTLE.home()

input("Pleace Enter key")
