class Rectangle:
   __x=10
   __y=10
   __height=10
   __weigth=20

   def __init__(self,x,y,height,weigth):
       self.__x=x
       self.__y=y
       self.__height=height
       self.__weigth=weigth
   def __str__(self):
       return f"«Прямоугольник с координатами ({self.x}; {self.y}) шириной {self.weigth} и высотой {self.height}»"
   def volume(self):
       return self.weigth * self.height



   def perimeter(self):
       return (self.weigth+self.height)*2

   def getX(self):
       self.__printlog("Запрошено свойство 'x'")
       return self.__x

   def getY(self):
       return self.__y

   def getHeight(self):
       return self.__height

   def getWeight(self):
       return self.__weigth

   def setX(self,x):
       self.__printlog("Изменено свойство 'x'")
       self.__x=x

   def sety(self, y):
       self.__y = y

   def setHeight(self, height):
       self.__height = height

   def setWeight(self, weight):
       self.__weigth = weight

   def __printlog(self,x):
       print(x)















rectangle=Rectangle(12,12,12,12)
rectangle.setX(20)
print(rectangle.getX())

