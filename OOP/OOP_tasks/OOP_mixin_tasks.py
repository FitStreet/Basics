"""Task 1"""

class Auto:
    def ride(self):
        print("Riding on a ground")

class Boat:
    def swim(self):
        print("Floating on water")

class Amphibian(Auto, Boat):
    pass

# obj = Amphibian()
# obj.ride()
# obj.swim()

"""Task 2"""

class RadioMixin:
    def play_music(self, title):
        print(f"Песня называется {title}")

class Auto(RadioMixin):
    def ride(self):
        print("Riding on a ground")

class Boat(RadioMixin):
    def swim(self):
        print("Floating on water")

class Amphibian(Auto, Boat, RadioMixin):
    pass

# obj = Amphibian()
# auto = Auto()
# boat = Boat()
# obj.play_music("lalala")
# auto.play_music("Trulala")
# boat.play_music("olololo")

"""Task 3"""

class Clock:
    def current_time(self):
        from datetime import datetime
        date = datetime.now() 
        time = str(date.time())       
        print(time[:8])

class Alarm:
    def on(self):
        print("Будильник включен ")
    def off(self):
        print("Будильник выключен ")

class AlarmClock(Clock, Alarm):
    def alarm_on(self):
        super().on()

clock = AlarmClock()
# clock.current_time()
# clock.alarm_on()

"""Task 4"""
from abc import ABC, abstractmethod

class Coder(ABC):
    count_code_time = 0

    @abstractmethod
    def get_info(self):
        pass

    @abstractmethod
    def coding(self):
        pass

class Backend(Coder):
    # self.count_code_time = count_code_time
    def __init__(self, experience, languages_backend):
        self.experience = experience
        self.languages_backend = languages_backend

    def coding(self, time):
        self.count_code_time = time
    
    def get_info(self):
        return f"{self.languages_backend} разработчик, уровень: {self.experience}, потрачено {self.count_code_time} часов на программирование"
    

class Frontend(Coder):
    def __init__(self, experience, languages_frontend):
        self.experience = experience
        self.languages_backend = languages_frontend
    
    def coding(self, time):
        self.count_code_time = time

    def get_info(self):
        return f"{self.languages_backend} разработчик, уровень: {self.experience}, потрачено {self.count_code_time} часов на программирование"

class Fullstack(Backend, Frontend):
    pass

a = Backend("Junior","Python")
b = Frontend("Middle","Javascript")
c = Fullstack("Senior", "Python and JS")

# a.coding(12) 
# b.coding(45) 
# c.coding(17) 
# print(a.get_info()) 
# print(b.get_info()) 
# print(c.get_info()) 

"""Task 5"""

class Square:
    def __init__(self, side) -> None:
        self.side = side

    def get_area(self):
        return int(self.side ** 2)

class Triangle:
    def __init__(self, hight, base) -> None:
        self.height = hight
        self.base = base

    def get_area(self):
        return int(0.5*self.base*self.height) 


class Pyramid(Triangle, Square):
    def get_volume(self):
        return int(1/3 * (self.base ** 2) * self.height)
    
# obj1 = Square(3) 
# obj2 = Triangle(3,5) 
# obj3 = Pyramid(10,10)
# print(obj1.get_area())  
# print(obj2.get_area())
# print(obj3.get_volume())

"""Task 6"""

class CreateMixin:
    def create(self, key, todo):
        if key in self.todos:
            return 'Задача под таким ключом уже существует'
        else:
            self.todos[key] = todo
            return self.todos

class DeleteMixin:
    def delete(self, key):
        data = self.todos.pop(key)
        return data

class UpdateMixin:
    def update(self, key, new_value):
        self.todos[key] = new_value
        return self.todos

class ReadMixin():
    def read(self):
        sorted_todos = list(sorted(self.todos.items()))
        return sorted_todos


class ToDo(
    CreateMixin,
    UpdateMixin,
    DeleteMixin,
    ReadMixin
    ):
    todos = {}

    def set_deadline(self, deadline):
        import datetime
        time_ = datetime.datetime.now().strftime('%d/%m/%Y')
        deadline = deadline.split("/")
        time_ = time_.split('/') 
        deadline = list(map(int, deadline))
        time_ = list(map(int, time_)) 
        time_ = sum((time_[0], time_[1]*30, time_[2]*365))
        deadline = datetime.date(deadline[2], deadline[1], deadline[0])
        time_ = datetime.date.today() 
        return (deadline - time_).days


# task = ToDo()
# print(task.create(1, 'Do housework')) 
# print(task.create(1, 'Do housework')) 
# print(task.create(2, 'Go for a walk')) 
# print(task.update(1, 'Do homework')) 
# print(task.delete(2)) 
# print(task.read()) 
# print(task.set_deadline('31/12/2023')) 
# print(task.todos) 

"""Task 7"""

class ExtensionMixin:

    def add_extension(self, extension):
        self.extensions.append(extension)
        return f"Добавлено новое расширение {extension} для игры {self.name}."
    
    def remove_extension(self, extension):
        try:    
            self.extensions.remove(extension)
            return f"{extension} был отключен от {self.name}" 
        except:
            return "Такого расширения нет в списке."

class Game(ExtensionMixin):
    def __init__(self, type, name):
        self.type = type
        self.name = name
        self.extensions = []
    def get_description(self, description):
        return f"{self.name} это {description}"
    
    def get_extensions(self):
        if len(self.extensions) == 0:
            return "Нет подключенных расширений"
        else:
            return " ".join(self.extensions)
    

game = Game('gg', 'Minencraft')
# print(game.get_description('инди-игра в жанре песочницы с элементами выживания и открытым миром')) 
# print(game.add_extension('Multiverse-Core')) 
# print(game.add_extension('Multiverse-Core1')) 
# game.extensions 
# print(game.get_extensions()) 
# print(game.remove_extension('Multiverse-Core')) 
# print(game.get_extensions())
    
"""Task 8"""

class WalkMixin:
    def walk(self):
        print("я могу ходить")

class FlyMixin:
    def fly(self):
        print("я могу летать")

class SwimMixin:
    def swim(self):
        print("я могу плавать")

class Human(WalkMixin, SwimMixin):
    pass

class Fish(SwimMixin):
    pass

class Exocoetidae(FlyMixin, SwimMixin):
    pass

class Duck(WalkMixin, FlyMixin, SwimMixin):
    pass

human = Human()
fish = Fish()
exocoetidae = Exocoetidae()
duck = Duck()

# human.walk()
# human.swim()
# fish.swim()
# exocoetidae.fly()
# exocoetidae.swim()
# duck.walk()
# duck.swim()
# duck.fly()

