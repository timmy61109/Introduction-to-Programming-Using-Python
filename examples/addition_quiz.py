"""Additional quiz.

隨機加法練習程式
"""
import ast
import random

# Generate random numbers
number1 = random.randint(0, 9)
number2 = random.randint(0, 9)

# Prompt the user to enter an answer
answer = ast.literal_eval(
    input("What is " + str(number1) + " + " + str(number2) + "? "))

# Display result
print(number1, "+", number2, "=", answer, "is", number1 + number2 == answer)
