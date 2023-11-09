"""Task 1"""

class Song:
    def __init__(self, author, title, year) -> None:
        self.author = author
        self.title = title
        self.year = year

    def show_title(self):
        return f"Название этой песни {self.title}"

    def show_author(self):
        return f"Автор этой песни {self.author}"

    def show_year(self):
        return f"Эта песня вышла в {self.year} году"



song = Song("Pharrell Williams", "Happy", 2013)

# print(song.show_title())
# print(song.show_author())
# print(song.show_year())
        
"""Task 2"""
# import math

class Circle:
    # color = 'синий'
    # pi_m = math.pi
    pi = 3.14

    def __init__(self, radius, color = "Синий") -> None:
        self.radius = radius
        self.color = color

    def get_area(self):
        area = self.radius ** 2 * self.pi
        return round(area,2)
    

circle = Circle(2)
circle.color = "белый"
print(circle.color)
print(circle.get_area())

"""Task 3"""

class BankAccount:

    def __init__(self) -> None:
        self.balance = 0

    def withdraw(self, amount):
        self.balance -= amount
        print(f'Ваш баланс: {self.balance} сом')
    
    def deposit(self, amount):
        self.balance += amount
        print(f'Ваш баланс: {self.balance} сом')
    

account = BankAccount()

# account.deposit(1000)
# account.withdraw(500)

"""Task 4"""

class Taxi:
    def __init__(self, name, cost, cost_km) -> None:
        self.name = name
        self.cost = cost
        self.cost_km = cost_km

    def get_total_cost(self, km):
        price = self.cost + self.cost_km * km
        return f"Такси {self.name}, стоимость поездки: {price} сом"
    


taxi1 = Taxi("Namba", 20, 5)
taxi2 = Taxi("Yandex", 15, 7)
taxi3 = Taxi("Jorgo", 10, 10)

# print(taxi1.get_total_cost(10)) 
# print(taxi2.get_total_cost(6)) 
# print(taxi3.get_total_cost(14))  

"""Task 5"""

class Phone:

    def __init__(self, name, last_name, phone) -> None:
        self.name = name
        self.last_name = last_name
        self.phone = phone

    def get_info(self):
        print(f"Контакт: {self.name} {self.last_name}, телефон: {self.phone}")

contact = Phone("John", "Snow", "+996707707707")

# contact.get_info()

"""Task 6"""

class Salary:
    percent = 8

    def __init__(self, salary, experience) -> None:
        self.salary = salary
        self.experience = experience

    def count_percent(self):
        result = (self.salary * self.experience) / 100 * self.percent
        return result


# obj = Salary(10000, 10)

# print(obj.count_percent())

"""Task 7"""

class Nobel:

    def __init__(self, category, year, winner) -> None:
        self.category = category
        self.year = year
        self.winner = winner

    def get_year(self):
        from datetime import datetime
        current_year = datetime.now().year
        difference = current_year - self.year
        return f"выиграл {difference} лет назад"
    
winner1 = Nobel("Литература", 1971, "Пабло Неруда") 
# print(winner1.category, winner1.year, winner1.winner) 
# print(winner1.get_year())

  
winner2 = Nobel("Литература", 1994, "Кэндзабуро Оэ") 
# print(winner2.category, winner2.year, winner2.winner) 
# print(winner2.get_year())

"""Task 8"""

class Password:
    def __init__(self, password):
        self.password = password

    def validate(self):
        if len(self.password) < 8 or len(self.password) >= 15:
            return "Password should be longer than 8 and less than 15"
        elif not any(char.isdigit() for char in self.password):
            return "Password should contain numbers too"
        elif not any(char.isalpha() for char in self.password):
            return "Password should contain letters as well"
        elif not any(char in "@#&$%!~*" for char in self.password):
            return "Your password should have some symbols"
        else:
            return "Your password is saved."

    def __str__(self):
        return '*' * len(self.password)

# password1 = Password("joe@123456")
# print(password1.validate())
# print(password1)

# password2 = Password("abc1dr33$")
# print(password2.validate())

"""Task 9"""

class Math:

    def __init__(self, number) -> None:
        self.number = number

    def get_factorial(self):
        if self.number == 0:
            return 1
        factorial = 1
        for i in range(1, self.number+1):
            factorial = factorial * i
        return factorial
       
    
    def get_sum(self):
        num1 = self.number
        sum = 0
        for i in str(num1):
            sum += int(i)
        return sum
        
    def get_mul_table(self):
        str_ = ""
        for i in range(1,11):
            result = self.number * i
            str_ += f"{self.number}x{i}={result}\n"
        return str_
    
    def get_sqrt(self):
        return self.number ** 0.5
        

obj = Math(4)
# print(obj.get_factorial())
# print(obj.get_sum())
# print(obj.get_mul_table())
# print(obj.get_sqrt())

"""Task 10"""

class ToDo:
    instances = {}

    def __init__(self, task) -> None:
        self.task = task

    def give_priority(self, priority):
        self.instances.update({priority: self.task})  

    def list_of_tasks(self):
        list_of_tasks = []
        sorted_keys = sorted(self.instances)
        list_of_tasks = [(key, self.instances[key]) for key in sorted_keys]

        return list_of_tasks


obj1 = ToDo("поесть")
obj1.give_priority(3)
obj2 = ToDo("поспать")
obj2.give_priority(1)
obj3 = ToDo("погулять")
obj3.give_priority(2)    

# print(obj3.list_of_tasks())


    
class Math2:
    result = 0

    def __init__(self, number) -> None:
        f = self.get_factorial(number)
        self.result = self.get_sqrt(f)

    def get_factorial(self, number):
        if number ==1:
            return 1
        factorial = 1
        for i in range(1, number+1):
            factorial = factorial * i
        self.result += factorial
        return factorial
        

    def get_sqrt(self, number):
        return number ** 0.5
        
        
    
        

obj_ = Math2(4) 
# print(obj_.get_factorial())
# print(obj_.get_sqrt())
print(obj_.result)

# написать итерируемый integer
# и чтобы смог показать его длину
# 12345678

iter_int = IterInt(12345678)
for i in iter_int:
    print(i)

class 