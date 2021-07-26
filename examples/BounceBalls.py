from random import randint
from tkinter import Button  # Import tkinter
from tkinter import Canvas
from tkinter import Frame  # Import tkinter
from tkinter import Label  # Import tkinter
from tkinter import LEFT  # Import tkinter
from tkinter import PhotoImage
from tkinter import Tk  # Import tkinter


def get_random_color():
    """Return a random color string in the form #RRGGBB."""
    color = "#"
    for j in range(6):
        color += to_hex_char(randint(0, 15))  # Add a random digit
    return color


def to_hex_char(hex_value):
    """Convert an integer to a single hex digit in a character."""
    if 0 <= hex_value <= 9:
        return chr(hex_value + ord('0'))
    else:  # 10 <= hex_value <= 15
        return chr(hex_value - 10 + ord('A'))

# Define a Ball class
class Ball:
    def __init__(self):
        self.x = 0  # Starting center position
        self.y = 0
        self.dx = 2  # Move right by default
        self.dy = 2 # Move down by default
        self.radius = 3 # The radius is fixed
        self.color = get_random_color() # Get random color


class BounceBalls:
    def __init__(self):
        self.ballList = []  # Create a list for balls

        window = Tk()  # Create a window
        window.title("Bouncing Balls") # Set a title

        self.width = 1000  # Width of the self.canvas
        self.height = 500  # Width of the self.canvas
        self.canvas = Canvas(window, bg="white",
            width=self.width, height=self.height)
        self.canvas.pack()

        frame = Frame(window)
        frame.pack()
        bt_stop = Button(frame, text="Stop", command=self.stop)
        bt_stop.pack(side=LEFT)
        btResume = Button(frame, text="Resume",
            command = self.resume)
        btResume.pack(side=LEFT)
        btAdd = Button(frame, text="+", command=self.add)
        btAdd.pack(side=LEFT)
        btRemove = Button(frame, text="-", command=self.remove)
        btRemove.pack(side=LEFT)

        self.sleep_time = 10  # Set a sleep time
        self.is_stopped = False
        self.animate()

        window.mainloop()  # Create an event loop

    def stop(self):
        """Stop animation."""
        self.is_stopped = True

    def resume(self):
        """Resume animation."""
        self.is_stopped = False
        self.animate()

    def add(self):
        """Add a new ball."""
        self.ballList.append(Ball())

    def remove(self):  # Remove the last ball
        self.ballList.pop()

    def animate(self):  # Move the message
        while not self.is_stopped:
            self.canvas.after(self.sleep_time)  # Sleep
            self.canvas.update()  # Update self.canvas
            self.canvas.delete("ball")

            for ball in self.ballList:
                self.redisplayBall(ball)

    def redisplayBall(self, ball):
        if ball.x > self.width or ball.x < 0:
            ball.dx = -ball.dx

        if ball.y > self.height or ball.y < 0:
            ball.dy = -ball.dy

        ball.x += ball.dx
        ball.y += ball.dy
        self.canvas.create_oval(ball.x - ball.radius,
            ball.y - ball.radius, ball.x + ball.radius,
            ball.y + ball.radius, fill = ball.color, tags = "ball")


BounceBalls()  # Create GUI

x = 2
lambda x: x ** 2
[x for x in range(10)]
2 if x == 0 else 4
