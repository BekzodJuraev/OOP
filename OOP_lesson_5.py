from abc import ABC,abstractmethod

class Auto(ABC):
    x=10
    y=10
    def __init__(self,x,y):
        self.x=x
        self.y=y
    @abstractmethod
    def movement(self,x,y):
        pass



class Audi(Auto):
    km=10
    speed=250
    name="Audi"
    def __init__(self,x,y,km,speed):
        Auto.__init__(self,x,y)
        self.km=km
        self.speed=speed

    def movement(self,x,y,km,speed):
        print(f'Макс скорость: {self.speed} Пробег: {self.km} и {self.x}{self.y}')

    def __str__(self):
        return self.name






audi=Audi(2,3,4,5)
print(audi)
audi.movement(250,20,2,3)

