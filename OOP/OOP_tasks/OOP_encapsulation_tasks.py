"""Task 1"""

# class A:
#     def public(self):
#         return 'Public method'
    
#     def _protected(self):
#         return 'Protected method'
    
#     def __private(self):
#         return 'Private method'
    

# obj1 = A()
# print(obj1.public())
# print(obj1._protected())
# print(obj1._A__private())

"""Task 2"""

# class A:
#     def method1(self):
#         print("Hello World")

# class B(A):
#     pass

# b1 = B()
# b1.method1()

"""Task 3"""

# class Car:
    
#     __speed = 0

#     def show_speed(self):
#         return self.__speed
    
#     def set_speed(self, new_speed):
#         self.__speed = new_speed

# car1 = Car() 
# print(car1.show_speed()) 
# car1.set_speed(20) 
# print(car1.show_speed()) 
    
"""Task 4"""

# class Car:
    
#     __speed = 0

#     @property
#     def speed(self):
#         return self.__speed
    
#     @speed.setter
#     def speed(self, new_speed):
#         self.__speed = new_speed

# car1 = Car() 
# print(car1.speed) 
# car1.speed = 20 
# print(car1.speed)

"""Task 5"""

# class Person:
#     name = "John"
#     _phone_number = "+996 557 55 17 57"
#     __card_number = "9999 9999 9999 9999"

# john = Person()
# print(john.name)
# print(john._phone_number)
# print(john._Person__card_number)

"""Task 6"""

# class Person:

#     def __init__(self, name, phone_number, card_number):
#         self.name = name
#         self._phone_number = phone_number
#         self.__card_number = card_number

# john = Person("John","+996 557 55 17 57", "9999 9999 9999 9999" )

# print(john.name)
# print(john._phone_number)
# print(john._Person__card_number)

"""Task 7"""

# class Person:
#     name = "John"
#     _phone_number = "+996 557 55 17 57"
#     __card_number = "9999 9999 9999 9999"

# john = Person()

# john.name = None
# john._phone_number = None
# john._Person__card_number = None

# print(john.name)
# print(john._phone_number)
# print(john._Person__card_number)


"""Task 8"""

# class Person:

#     def __init__(self, name, phone_number, card_number):
#         self.name = self.__validate_name(name)
#         self._phone_number = phone_number
#         self.__card_number = card_number
        
#     def __validate_name(self,name):
#         if len(name) < 2:
#             return "John"
#         else:
#             return name.capitalize()

# sam = Person("SAM","+996 557 55 17 57", "9999 9999 9999 9999" )

# print(sam.name)
# print(sam._phone_number)
# print(sam._Person__card_number)

"""Task 9"""

# class Person:

#     def __init__(self, name, phone_number, card_number):
#         self.name = name
#         self._phone_number = self._validate_phone_number(phone_number)
#         self.__card_number = self.__validate_card_number(card_number)
        
#     def _validate_phone_number(self,phone_number):
#         if isinstance(phone_number, int) and str(phone_number).startswith("996"):
#             return phone_number
        
        
#     def __validate_card_number(self,card_number):
#         if isinstance(card_number, int) and len(str(card_number)) == 16:
#             return card_number
        
# tolik = Person("Tolik",996221142806, 9999999999999999)

# print(tolik.name)
# print(tolik._phone_number)
# print(tolik._Person__card_number)

"""Task 10"""

# class Game:
#     __level = 0
   
#     def __init__(self, name) -> None:
#         self.name = name
    
#     def play(self, hours):
#         if hours > 2:
#             self.__level += 1
        
#     def get_level(self):
#         return self.__level
    

# game = Game("Ivan")
# print(game.get_level())
# print(game.get_level())
# game.play(3)
# game.play(3)
# print(game.get_level())

"""Task 11"""

# class Game:
#     __level = 0
   
#     def __init__(self, name) -> None:
#         self.name = self.__validate_name(name)
    
#     def __validate_name(self,name):
#          return name.title()

#     def set_level(self, new_level):
#             if self.name == "Tolik":
#                 self.__level = new_level
#                 return self.__level
#             else:
#                 print(f"{self.name} ты не Tolik!") 

# game = Game("Raychel")
# game.set_level(5)
# print(game._Game__level)
# game2 = Game("TOLIK")
# game2.set_level(5)
# print(game2._Game__level)


"""Task 12"""

# class Game:
#     __level = 0

#     def __init__(self, name) -> None:
#         self.name = name

#     def get_level(self):
#         return self.__level
    
#     def set_level(self, new_level):
#         self.__level = new_level

# game = Game("Ivan")
# print(game.get_level())
# print(game.set_level(10))
# print(game.get_level())

"""Task 13"""

# class Game:
#     __level = 0
#     @property
#     def level(self):
#         return self.__level
    
# game = Game()
# print(game.level)

"""Task 14"""

# class Game:
#     __level = 0
    
#     @property
#     def level(self):
#         return self.__level
    
#     @level.setter
#     def level(self,n):
#         self.__level = n
    
# game = Game()
# print(game.level)
# game.level += 1
# print(game.level)

"""Task 15"""

# class Person:
#     def __init__(self, name = None, last_name = None, age = None, email = None):
#         self.__name = name
#         self.__last_name = last_name
#         self.__age = age
#         self.__email = email
    
#     def get_name(self):
#         return self.__name
#     def get_last_name(self):
#         return self.__last_name
#     def get_age(self):
#         return self.__age
#     def get_email(self):
#         return self.__email
    
#     def set_name(self, new_name):
#         self.__name = new_name
#     def set_last_name(self, new_last_name):
#         self.__last_name = new_last_name
#     def set_age(self, new_age):
#         self.__age = new_age
#     def set_email(self, new_email):
#         self.__email = new_email

# john = Person()
# print(john.get_name()) # None
# print(john.get_last_name()) # None
# print(john.get_age()) # None
# print(john.get_email()) # None
# john.set_name('John')
# john.set_last_name('Snow')
# john.set_age(30)
# john.set_email('johnsnow@gmail.com')
# print(john.get_name()) # John
# print(john.get_last_name()) # Snow
# print(john.get_age()) # 30
# print(john.get_email()) # johnsnow@gmail.com

"""Task 16"""

# class Person:
#     def __init__(self, name = None, last_name = None, age = None, email = None):
#         self.__name = name
#         self.__last_name = last_name
#         self.__age = age
#         self.__email = email
    
#     @property
#     def name(self):
#         return self.__name
#     @property
#     def last_name(self):
#         return self.__last_name
#     @property
#     def age(self):
#         return self.__age
#     @property
#     def email(self):
#         return self.__email
    
#     @name.setter
#     def name(self, new_name):
#         self.__name = new_name
#     @last_name.setter
#     def last_name(self, new_last_name):
#         self.__last_name = new_last_name
#     @age.setter
#     def age(self, new_age):
#         self.__age = new_age
#     @email.setter
#     def email(self, new_email):
#         self.__email = new_email

# john = Person()
# print(john.name) # None
# print(john.last_name) # None
# print(john.age) # None
# print(john.email) # None
# john.name = 'John'
# john.last_name = 'Snow'
# john.age = 30
# john.email = 'johnsnow@gmail.com'
# print(john.name) # John
# print(john.last_name) # Snow
# print(john.age) # 30
# print(john.email) # johnsnow@gmail.com

"""Task 17"""

# class Dad:
#     name = "John"
#     _last_name = "Snow"
#     __age = 40


# class Me(Dad):
#     name = "Sam"
#     __age = 10

#     def about_me(self):
#         return f"My name is {self.name} {self._last_name} and I am {self.__age} years old"
    
#     def about_my_father(self):
#         return f"My father is {Dad.name} {Dad._last_name}"
    

# me = Me()
# print(me.about_me())
# print(me.about_my_father())



