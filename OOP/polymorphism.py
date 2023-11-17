# Полиморфизм - принцип ООП, в котором в разных классах методы называются одинаково, но реализация разная(функционал) разная. Один интерфейс, разный функционал.

1+1
"a"+"a"
[1,2]+[1,2]

# Полиморфизм - множество форм
# a = 1
# a.__add__(4) == a + 4

class Cat:
    def voice(self):
        print('мяу-мяу')

class Dog:
    def voice(self):
        print('гав-гав')

# objects = [Cat(),Dog()]
# for i in objects:
#     i.voice()

class ShapeMixin:
    def __init__(self) -> None:
        pass
    def area(self):
        pass

class Square(ShapeMixin):
    def __init__(self, side) -> None:
        self.side = side

    def area(self):
        return int(self.side ** 2)

class Circle(ShapeMixin):
    def __init__(self, radius):
        self.radius = radius
    def area(self):
        return int(3.14 * self.radius ** 2)
    
# square = Square(4)
# circle = Circle(5)
# print(square.area())
# print(circle.area())      

# list.pop()
# dict.pop()
# set.pop()

class India:
    def capital(self):
        print("New Delhi is tha capital of India")
    def language(self):
        print("Hindi is the language of India")
    def location(self):
        print("South Asia is the location of India")

class GreatBritan:
    def capital(self):
        print("London is tha capital of GreatBritan")
    def language(self):
        print("English is the language of GreatBritan")
    def location(self):
        print("Europe is the location of GreatBritan")
    
def func(obj):
    obj.capital()
    obj.language()
    obj.location()

india = India()
britan = GreatBritan()

# func(india)
# func(britan)

class Toyota:
    speed = 180
    km = 20
    def max_speed_20km(self):
        return 3600*(self.km / self.speed)   

class Lexus:
    speed = 240
    km = 20
    def max_speed_20km(self):
        return 3600*(self.km / self.speed) 

toy = Toyota()
lex = Lexus()
print(toy.max_speed_20km())
print(lex.max_speed_20km())