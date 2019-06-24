from dieview  import DieView
import graphics as g 
import random

def main():
    app = App()
    app.run()

class App():

    def __init__(self):
        self.win = g.GraphWin(title="Dice Game", width=500, height=500)
        self.dwidget1 = DieView(self.win, center = g.Point(40,40), size=40)
        self.dwidget2 = DieView(self.win, center= g.Point(90, 40), size=40)
        self.dwidget3 = DieView(self.win, center= g.Point(40, 100), size=40)
        self.dwidget4 = DieView(self.win, center=g.Point(90,100), size=40)
        self.dwidget5 = DieView(self.win, center=g.Point(40,160), size=40)
        
        # self.button = g.Rectangle(g.Point(10,200),g.Point(90,230))
        # self.button.setFill('green')
        self.win.bind("<Button-1>", self.reroll)
    def rollDice(self):
 
        self.dwidget1.setValue(random.randint(1,6))
        self.dwidget2.setValue(random.randint(1,6))
        self.dwidget3.setValue(random.randint(1,6))
        self.dwidget4.setValue(random.randint(1,6))
        self.dwidget5.setValue(random.randint(1,6))
    def reroll(self,event):
        
        self.dwidget1.setValue(random.randint(1,6))
        self.dwidget2.setValue(random.randint(1,6))
        self.dwidget3.setValue(random.randint(1,6))
        self.dwidget4.setValue(random.randint(1,6))
        self.dwidget5.setValue(random.randint(1,6))

    def run(self):
      
        
        self.rollDice()

        self.win.getMouse()
        print('running')
        self.win.close()

    
            
      
main()