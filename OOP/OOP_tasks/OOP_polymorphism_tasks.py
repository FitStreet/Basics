"""Task 1"""
# a = '12342342345' 
# b = [1,['a',5,6],2,3,4,5] 
# c = {1:'a', 2: {'a': 1, 'b': 2}, 3:'c'} 

# f = [a,b,c]

# for i in f:
#     print(len(i))

"""Task 2"""

class Cat:
    def voice(self):
        print('Мяу')

class Dog:
    def voice(self):
        print('Гав')

def to_pet(obj):
    obj.voice()

barsik = Cat()
rex = Dog()

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
from abc import ABC, abstractmethod

class Shape(ABC):
    
    @abstractmethod
    def area(self):
        pass

class Square(Shape):
    def __init__(self, side) -> None:
        self.side = side

    def area(self):
        return int(self.side ** 2)

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
    def area(self):
        return int(3.14 * self.radius ** 2)