u"""
程式設計練習題 1-6 1-15 Turtle:畫二個三角形.

撰寫一程式，在螢幕的畫二個三角形。
"""

from turtle import Turtle

TURTLE = Turtle()

TURTLE.showturtle()
TURTLE.right(60)
TURTLE.forward(100)
TURTLE.right(120)
TURTLE.forward(100)
TURTLE.right(120)
TURTLE.forward(200)
TURTLE.right(-120)
TURTLE.forward(100)
TURTLE.right(-120)
TURTLE.forward(100)
