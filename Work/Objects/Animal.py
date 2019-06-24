

class Animal:
    def __init__(self, name='Some Random Animal'):
        self.name = name

    def printName(self):
        print(self.name)


class Cow(Animal):

    def __init__(self, name='Super Cow', master='Alex'):
        self.master = master
        return super().__init__(name)

    def walk(self):
        print('Cows walk towards its master: ' + self.master)



if __name__ == '__main__':
    someAnimal = Animal()
    someAnimal.printName()
    AlexCow = Cow()
    AlexCow.walk()
    AlexCow.printName()