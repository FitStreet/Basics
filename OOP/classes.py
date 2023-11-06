"===============================OOP========================="


# class - шаблон(схема)
# object - объект, экземпляр, instance -> объектб созданный по шаблону класса (перенимает все методы и атрибуты класса)

# атрибут класса - переменные, которые мы создаем при создании класса(внутри класса), будут присвоены к каждому объекту класса
# атрибут экземпляра класса - переменные внутри класса которые мы принимаем при создании экземпляра(объекта)
# метод - функция вгутри класса
# self - ссылка на сам класс
# __init__ - магический метод конструктор, который создает новые атрибуты внутри класса

# SOLID

# S – Принцип единственной ответственности (Single Responsibility Principle),

# O – Принцип открытости/закрытости (Open‐Closed Principle),

# L – Принцип подстановки Барбары Лисков (Liskov Substitution Principle),

# I – Принцип разделения интерфейсов (Interface Segregation Principle),

# D – Принцип инверсии зависимостей (Dependency Inversion Principle).

# написать калькулитор на классах
# __init__ принимает 2 числа

list
dict
bool

a = 4
a = int(4)

str_ = 'str'
str_ = str('str')


str # class
int # class
5 # объект класса int 
'asfasfdf' # объект класса str




class Car: # class

    shifter = "коробка передач" # атрибут класса
    engine = 'двигатель'
    speedometr = 'speedometr'


    def __init__(self, color, quantity_of_doors, ) -> None:
        self.color = color # атрибут экземпляра класса
        self.quantity_of_doors = quantity_of_doors # атрибут экземпляра класса

    def move(self):    # метод class
        print('whruuuum')

    def start(self):
        print('turn on')

    def end(self):
        print('turn off')

car1 = Car('черный', 4)
# print(car1.color)
# car1.start()
# car1.move()
# car1.end() 


# car2 = Car('белый', 2)
# print(car2.color)
# car3 = Car('красный', 3)
# print(car3.color)


class Human:
      
    legs =2
    arms = 2
    eyes = 2

    def __init__(self, nation, language, race, gender, hair_color) -> None: # __init__
        self.nation = nation
        self.langeage = language
        self.race = race
        self.gender = gender
        self.hair_color = hair_color
    
    def walk(self):
        print("walk")

    def voice(self):
        print('bla bla bla')

    def sleep(self):
        print("Zz Zz Zz")

    def think(self, about = "nothing"):
        print(f'thinking about {about}')

    def breath(self):
        print('breathing')

    def get_info(self):
        return f'i am a human from {self.nation}, my language is {self.langeage}, my gender is {self.gender}, my rase is {self.race}, my Hair color is {self.hair_color}'



human1 = Human('Russia', 'rus', 'europioid', 'it', 'pink')
# human1.profession = "Doctor"
# print(human1.profession)
# # print(human1.get_info())
# human2 = Human('Kyrgyzstan', 'KG', 'mongoloid', 'man', 'black')
# human3 = Human('Africa', 'Negeria', 'negirian', 'woman', 'brown')
# # print(human2.get_info())
# # print(human3.get_info())

print(human1.think(about = 'food'))
