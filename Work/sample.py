from graphics import *
import random

def randomplot(nPoints):
        win = GraphWin("Random points", 500, 500)
        for i in range(nPoints):
                x = random.randrange(500)
                y = random.randrange(500)
                win.plot(x,y,"red")
randomplot(100)
randomplot(1000)