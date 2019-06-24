import graphics as g
import random

def main():
    app = App()
    app.run()

class App():
    
    def __init__(self):
        self.window = g.GraphWin(title="My great App",width=500,height=500)

    def run(self):
        random.seed()
        print(random.random())
        for i in range(100000):
            self.window.plot(random.randrange(500), random.randrange(500), color="red")
        self.window.getMouse()
        self.window.close()
main()