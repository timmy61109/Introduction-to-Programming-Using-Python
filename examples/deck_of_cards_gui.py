"""Dock of card GUI."""
import random
from tkinter import Button  # Import tkinter
from tkinter import Frame  # Import tkinter
from tkinter import Label  # Import tkinter
from tkinter import LEFT  # Import tkinter
from tkinter import PhotoImage
from tkinter import Tk  # Import tkinter


class DeckOfCardsGUI(object):
    """Docstring for DeckOfCardsGUI."""

    def __init__(self):
        """Initialize DeckOfCardsGUI."""
        window = Tk()  # Create a window
        window.title("Pick Four Cards Randomly")  # Set title

        self.image_list = []  # Store images for cards
        for i in range(1, 53):
            self.image_list.append(PhotoImage(
                file="image/card/" + str(i) + ".gif"))

        frame = Frame(window)  # Hold four labels for cards
        frame.pack()

        self.label_list = []  # A list of four labels
        for i in range(4):
            self.label_list.append(Label(frame, image=self.image_list[i]))
            self.label_list[i].pack(side=LEFT)

        Button(window, text="Shuffle", command=self.shuffle).pack()

        window.mainloop()  # Create an event loop

    def shuffle(self):
        """Choose four random cards."""
        random.shuffle(self.image_list)
        for i in range(4):
            self.label_list[i]["image"] = self.image_list[i]


DeckOfCardsGUI()  # Create GUI
