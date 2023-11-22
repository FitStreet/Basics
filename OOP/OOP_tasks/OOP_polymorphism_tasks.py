"""Task 1"""
# a = '12342342345' 
# b = [1,['a',5,6],2,3,4,5] 
# c = {1:'a', 2: {'a': 1, 'b': 2}, 3:'c'} 

# f = [a,b,c]

# for i in f:
#     print(len(i))

"""Task 2"""

# class Cat:
#     def voice(self):
#         print('Мяу')

# class Dog:
#     def voice(self):
#         print('Гав')

# def to_pet(obj):
#     obj.voice()

# barsik = Cat()
# rex = Dog()

# to_pet(barsik) 
# to_pet(rex) 

"""Task 3"""

# class Person:
#     def __init__(self, name, last_name):
#         self.name = name
#         self.last_name = last_name

#     def get_info(self):
#         print(f"Привет, меня зовут {self.name} {self.last_name}")       

# class Employee(Person):
#     def __init__(self, name, last_name, work, status):
#         super().__init__(name,last_name)
#         self.work = work
#         self.status = status
#     def get_info(self):
#         print(f"Привет, меня зовут {self.name} {self.last_name}, я работаю в компании {self.work} на должности {self.status}.")
    
# class Student(Person):
#     def __init__(self,name, last_name, university, course):
#         super().__init__(name,last_name)
#         self.university = university
#         self.course = course

#     def get_info(self):
#         print(f"Привет, меня зовут {self.name} {self.last_name}, я учусь в {self.university} на {self.course} курсе")
        
        
# person = Person("Иван", "Петров")
# employee = Employee("Иван", "Петров","Рога и копыта", "директор")
# student = Student("Иван", "Петров","КГТУ", 3)

# def get_human_info(obj):
#     obj.get_info()

# get_human_info(person)
# get_human_info(employee) 
# get_human_info(student)

"""Task 4""" 
# from abc import ABC, abstractmethod

# class Shape(ABC):
    
#     @abstractmethod
#     def get_area(self):
#         pass

# class Square(Shape):
#     def __init__(self, side) -> None:
#         self.side = side

#     def get_area(self):
#         return self.side ** 2

# class Circle(Shape):
#     from math import pi
#     def __init__(self, radius):
#         self.radius = radius
#     def get_area(self):
#         return self.pi * self.radius ** 2
    
# class Triangle(Shape):
#     def __init__(self, base, height) -> None:
#         self.height = height
#         self.base = base

#     def get_area(self):
#         return 0.5*self.base*self.height 

# triangle = Triangle(123, 453)
# square = Square(564)
# circle = Circle(456) 

# print(triangle.get_area())
# print(square.get_area())
# print(circle.get_area())

"""Task 5"""
# class OS:
#     def __init__(self, version) -> None:
#         self.version = version
#     pass

# class Windows(OS):
#     def copy(self,text):
#         return f'скопирован текст "{text}" горячими клавишами CTRL + C'
# class Linux(OS):
#     def copy(self,text):
#         return f'скопирован текст "{text}" горячими клавишами CTRL + SHIFT + C'
# class MacOS(OS):
#     def copy(self,text):
#         return f'скопирован текст "{text}" горячими клавишами COMMAND + C'

 
# win = Windows(1)
# lin = Linux(2)
# mac = MacOS(3)
    
# print(win.copy('Полиморфизм — одна из основных парадигм ООП'))
 
# print(mac.copy('Полиморфизм - разное поведение одного и того же метода в разных классах')) 
 
# print(lin.copy('На самом деле одинаковым является только имя метода, его исходный код зависит от класса'))

"""Task 6"""

# class Language:
#     def __init__(self, level, type) -> None:
#         self.level = level
#         self.type = type

# class Python(Language): 
#     def write_function(self, func_name, arg):
#         return f"def {func_name}({arg}):"
#     def create_variable(self, var_name, value):
#         if type(value) ==str:
#             return f"{var_name} = '{value}'"
#         else:
#             return f"{var_name} = {value}"

# class JavaScript(Language):
#     def write_function(self, func_name, arg):
#         return f"function {func_name}({arg}) {{     }};"
#     def create_variable(self, var_name, value):
#         if type(value) ==str:
#             return f"let {var_name} = '{value}';"
#         else:
#             return f"let {var_name} = {value};"
    

# py = Python(1,"a")
# js = JavaScript(3,"4")

# print(py.write_function('get_code', 'a')) 
# print(py.create_variable('name', 'John'))
# print(js.write_function('validate', 'form')) 
# print(js.create_variable('password', 'john@123'))

"""Task 7"""

# class Money:
#     def __init__(self, country, symbol):
#         self.country = country
#         self.symbol = symbol

# class Dollar(Money):
#     rate = 84.80
#     def exchange(self, amount):
#         result = amount * self.rate
#         return f"$ {amount} равен {result} сомам"
# class Euro(Money):
#     rate = 98.40
#     def exchange(self, amount):
#         result = amount * self.rate
#         return f"€ {amount} равен {result} сомам"
    
# dollar = Dollar("USA", "$")
# euro = Euro("Europe", "e")

# print(dollar.exchange(100))
# print(euro.exchange(80))

"""Task 8"""

# class Planet:
#     def __init__(self, orbit) -> None:
#         self.orbit = orbit

# class Venus(Planet):

#     def get_age(self, earth_age):
#         result = earth_age * 365 / self.orbit * 365
#         return f"на Венере ваш возраст составляет {int(result)} дней"

# class Mercury(Planet):


#     def get_age(self, earth_age):
#         result = earth_age * 365 / self.orbit
#         return f"на Меркурии ваш возраст составляет {int(result)} лет"
        
# class Jupiter(Planet):


#     def get_age(self, earth_age):
#         result = round(earth_age * 365 // self.orbit * 365 * 24)
#         return f"на Юпитере ваш возраст составляет {result} часов"
        

# v = Venus(225)
# print(v.get_age(17))

# j = Jupiter(12)
# print(j.get_age(23))

# m = Mercury(88)
# print(m.get_age(32))