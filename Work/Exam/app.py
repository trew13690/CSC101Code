"""
    App.py ~ This App build Meh Faces !!! 0.0 -_-
    by Alex Trew ~ 03/21/19
"""
from graphics import * 
import math
class App():
    """
        App - Contains all high level objects


    """

    def __init__(self, faceR=50,eyeR=10, facecolor='blue', eyeColor='red', noseColor='green', noseWidth=10):
        self.window = GraphWin("Meh Face", width=600, height=600)
        self.window.setCoords(-100,-100,100,100)
        self.window.bind("<Motion>", self.getCoordinates)
        self.face = Face(self.window,faceR=int(faceR),eyeR=int(eyeR),facecolor=facecolor,noseColor=noseColor, noseWidth=noseWidth,eyeColor=eyeColor)

    def getCoordinates(self, event):
        print(event)
        points = self.window.toWorld(event.x, event.y)
        points = [round(p,2) for p in points]
        print(str(points))
        
    def run(self):
        print('Running ...')
        self.window.getMouse()
        self.window.close()

class Face():
    """
        Face ~ Represents the whole of a face 
    """
    def __init__(self, window, facecolor, eyeColor,noseColor ,noseWidth, faceR, eyeR):
        print('Creating a face!')
        self.head = Head(window, faceR, facecolor)
        self.eyes = Eye(window,faceR,eyeR,eyeColor)
        
        self.nose = Nose(window,noseWidth,noseColor)
        self.smile = Smile(window,faceR)



class Head():
    """
        The Face component 
    """
    def __init__(self,window, radius,facecolor, center=Point(0,0), ):
        self.radius = radius
        self.window = window
        self.head = Circle(center, radius)
        self.draw()
        self.head.setFill(facecolor)
    def draw(self):
        print('Making a head first !')
        self.head.draw(self.window)

class Eye():
    """
        Draws two eye Components
    """
    def __init__(self, window,faceR, radius, eyeColor):
        self.window = window
        self.radius = radius
        self.eyeCenterR = Eye.calculateEyeDistance(faceR, 'right')
        self.eyeCenterL = Eye.calculateEyeDistance(faceR, 'left')
        self.eyel = Circle(self.eyeCenterR,self.radius)
        self.eyel.draw(self.window)
        self.eyer = Circle(self.eyeCenterL, self.radius)
        self.eyer.draw(self.window)
        self.eyer.setFill(eyeColor)
        self.eyel.setFill(eyeColor)
    def calculateEyeDistance(faceR, side):
        if (side == 'right'):
            angle = 45
            x =  (faceR/2)*math.cos(angle)
            y = (faceR/2)*math.sin(angle)
            return Point(x,y)
        else:
            angle = 45
            x =  (faceR/2)*math.cos(angle)
            x = -x
            y = (faceR/2)*math.sin(angle)
            return Point(x,y)
class Nose():
    def __init__(self, window,noseWidth,noseColor):
        self.nose = Rectangle(Point( -noseWidth/2 ,noseWidth),Point(noseWidth/2,-noseWidth))
        self.nose.draw(window)
        self.nose.setFill(noseColor)

class Smile():

    def __init__(self, window, radius):
        self.window = window
        self.radius = radius
        self.smile = Line(Point(-radius/3,-radius/3),Point( radius/3,-radius/3))
        self.smile.draw(self.window)
        

print('Welcome to the meh creator!')
print('Please enter the information as asked!')
radius = input('\nWhat is the desired radius of the head?')
eyeRadius = input('What is your desired eye radius?')
noseWidth = input('what is the nose width?')
colorPick = input('What is the desired color for the head?')
eyeColorPick = input('What eye color do you wish? ')
noseColorPick = input('what color of nose do you wish?')
# Create check here to convert empty string allow defaults in App()
SmileApp = App(radius,eyeRadius, facecolor=colorPick,noseWidth=int(noseWidth), noseColor=noseColorPick, eyeColor=eyeColorPick)
SmileApp.run()