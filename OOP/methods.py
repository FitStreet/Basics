"существует 3 вида методов"

# instance method - обычные методы, которые первым аргументом принимают self(ссылка на объект), нкжны они для работы с атрибутами объекта
# class method - методы класса, которые принимают первым аргументом cls (ссылку на класс), они нужны нам для изменения атрибутов класса и сздания объектов от класса, чтобы создать classmethod, мы должны задекорировать его @classmethod
# static method - функции внутри класса, которые не взаимодействуют не с классом, не с объектом, они находятся внутри класса, лишь для использования только внутри класса, чтобы создать статичный метод, его нужно задекорировать @staticmetod

class A:
    def instance_method(self):
        print("метод объекта")
        print(f"первый аргумент {self}")

obj = A()
# obj.instance_method() # если вызываем у объекта, то self передается автоматически
# A.instance_method(obj) # если вызываем у класса, то self нужно будет передать объект этого класса

class B:

    @classmethod
    def class_method(cls):
        print("метод класса")
        print(f"первый аргумент {cls}")

obj = B()
# obj.class_method()
# B.class_method()
# не важно откуда мы вызываем classmethod, первым аргументом всегда прилетает ссылка на класс

class A:
    counter = 0
    def __init__(self) -> None:
        self.counter +=1

    @classmethod
    def _increment(cls):
        cls.counter +=1

class B(A):
    counter = 0
    

b1 = B()
b2 = B()
b3 = B()
b4 = B()

class Pizza:
    def __init__(self, radius, *ingredients) -> None:
        self.radius = radius
        self.ingredients = ingredients
    @classmethod
    def four_cheese(cls,r):
        pizza = cls(r, "моцарелла", "чеддер", "дорблю", "голландский")
        return pizza
    
    def get_info(self):
        return f"пицца {self.radius*2} ингредиенты {self.ingredients}"

pizza1 = Pizza(20, "сыр", "колбаса", "помидор")
pizza2 = Pizza.four_cheese(15)
pizza3 = Pizza.four_cheese(30)

lst = [pizza1, pizza2, pizza3]
for i in lst:
    print(i.get_info())

class C:
    @staticmethod
    def static_method(a, b):
        print('статичный метод')
        print("не принимает не self, ни cls (принимает то что нужно)")
from math import pi

class Cylinder:
    
    def __init__(self, diametr, height) -> None:
        self.diametr = diametr
        self.height = height
        self.area = self.get_area(diametr, height)

    @staticmethod    
    def get_area(d, h):
        print(int(pi * ((d / 2) ** 2) * h))

cylinder = Cylinder(4, 10)
cylinder.area

class Iphone15:

    def __init__(self, name, price) -> None:
        self.name = name
        self.price = price
    
    @classmethod
    def change_cost(cls, new_price):
        cls.price = new_price
        return cls.price

    @staticmethod
    def exchange(n):
        print(n / 89.140)
        return n / 89.140
    
    def som_to_dollar(self):
        return self.price / 89.140

iphone= Iphone15("pro max", 118000)
iphone.change_cost(110000)
iphone.exchange(110000)
print(iphone.som_to_dollar())
print(Iphone15.price)




