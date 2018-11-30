from random import choice
from time import sleep
from turtle import *
from freegames import floor, square, vector
from tkinter import *
from PIL import Image
from PIL import ImageTk
from tkinter import ttk
import pandas as pd
i=0
leng = 0
class k:
    def __init__(self):
        self.pattern = []
        self.guesses = []
        self.tiles = {
            vector(0, 0): ('red', 'dark red'),
            vector(0, -200): ('blue', 'dark blue'),
            vector(-200, 0): ('green', 'dark green'),
            vector(-200, -200): ('yellow', 'khaki'),
        }
        setup(420, 420, 370, 0)
        hideturtle()
        tracer(False)
        self.grid()
        onscreenclick(self.start)
        done()
    def grid(self):
        "Draw grid of tiles."
        square(0, 0, 200, 'dark red')
        square(0, -200, 200, 'dark blue')
        square(-200, 0, 200, 'dark green')
        square(-200, -200, 200, 'khaki')
        update()

    def flash(self,tile):
        "Flash tile in grid."
        glow, dark = self.tiles[tile]
        square(tile.x, tile.y, 200, glow)
        update()
        sleep(0.3)
        square(tile.x, tile.y, 200, dark)
        update()
        sleep(0.3)

    def grow(self):
        "Grow pattern and flash tiles."
        tile = choice(list(self.tiles))
        self.pattern.append(tile)

        for tile in self.pattern:
            self.flash(tile)

        print('Pattern length:', len(self.pattern))
        global leng
        leng = len(self.pattern)
        self.guesses.clear()

    def tap(self,x, y):
        "Respond to screen tap."
        onscreenclick(None)
        x = floor(x, 200)
        y = floor(y, 200)
        tile = vector(x, y)
        index = len(self.guesses)

        if tile != self.pattern[index]:
            root = Tk()
            w = 500 # width for the Tk root
            h = 500 # height for the Tk root

            # get screen width and height
            ws = root.winfo_screenwidth() # width of the screen
            hs = root.winfo_screenheight() # height of the screen

            # calculate x and y coordinates for the Tk root window
            x = (ws/2) - (w/2)
            y = (hs/2) - (h/2)

            # set the dimensions of the screen 
            # and where it is placed
            root.geometry('%dx%d+%d+%d' % (w, h, x, y))
            root.title("Simon Says Test")
            global leng
            if leng < 4:
                Label(root,text="ID").place(x=250,y=250)
            else:
                Label(root,text="Not ID").place(x=250,y=250)
            Button(root,text="Next",command=exit).place(x=250,y=400)
            

        self.guesses.append(tile)
        self.flash(tile)

        if len(self.guesses) == len(self.pattern):
            self.grow()

        onscreenclick(self.tap)

    def start(self,x, y):
        "Start game."
        self.grow()
        onscreenclick(self.tap)

ak = k()