class Auto:
    x=10
    y=10
    def __init__(self,x,y):
        self.x=x
        self.y=y

    def movement(self,x,y):
        self.x=x
        self.y=y
        print(f'{self.x},{self.y}')



class Audi(Auto):
    km=10

    def __init__(self,x,y,km):
        Auto.__init__(self,x,y)
        self.km=km
    def movement(self,x,y,km):
        self.x=x
        self.y=y
        self.km=km
        print(f'{self.x},{self.y},{self.km}')



auto=Auto(2,3)
audi=Audi(10,3,4)
auto.movement(1,3)
audi.movement(2,5,7)