"""Task 1"""
class Product:
    base_price = 20000
    def __init__(self, model, year, color) -> None:
        self.model = model
        self.year = year
        self.color = color

    def has_garantiya(self, year):
        if self.year + 2 < year:
            return "Ваша гарантия истекла"
        else:
            return "Гарантия действительна"
    @classmethod    
    def change_price(cls, rate):
        cls.base_price += int(cls.base_price * rate / 100)
        return cls.base_price


# obj = Product('A218', 2008, 'red') 
# obj.change_price(2) 
# print(obj.has_garantiya(2010)) 
# print(obj.base_price) 

"""Task 2"""

class User:
    def __init__(self, name, lastname, email):
        self.name = name
        self.lastname = lastname
        self.email = email

    @staticmethod
    def validate_email(email):
        if "@" in email:
            return True
        else:
            return False
        
    def __str__(self):
        if self.validate_email(self.email):
            return f"{self.name}:{self.email}"
        else:
            return "email в неправильном формате"
        
    @classmethod
    def create_user(cls, string):
        data = string.split(",")
        user = cls(data[0], data[1], data[2])
        return user
    
user1 = User.create_user("Jaanger,Barakanov,jbarakanov@mail.ru")
user2 = User.create_user("Mars,Radbekov,marsradbek")


# print(user1) 
# print(user2) 

"""Task 3"""

class Makers:
    student_count = 0
    def __init__(self, name, language, kpi):
        self.name = name
        self.language = language
        self.kpi = kpi

    @classmethod
    def new_student(cls, name, language, kpi):
        cls.student_count += 1
        student  = cls(name, language, kpi)
        return student
    
    def get_info(self):
        return f"Student name: {self.name}, Language: {self.language}"
    
    def set_kpi(self, mark):
        self.kpi = mark
        return self.kpi
    
student1 = Makers.new_student("Vlad", "Python", 0)
student2 = Makers.new_student("Malik", "JavaScript", 0)

# print(student1.set_kpi(89)) 
# print(student1.get_info()) 
# print(student2.set_kpi(89)) 
# print(student2.get_info()) 
# print(Makers.student_count) 

"""Task 4"""

class Bike:
    def __init__(self, cost, make, model, year, min_profit):
        self.cost = cost
        self.make = make
        self.model = model
        self.year = year
        self.min_profit = min_profit
        self._sale_price = None
        self.sold = False

    def set_cost(self, price):
        if price >= self.cost:
            self._sale_price = price
        else:
            self._sale_price = price + self.min_profit

    def service(self, fix_price):
        self._sale_price += fix_price
        return self._sale_price
    
    def sell(self):
        self.sold = True
        return self.cost - self._sale_price
    
    @classmethod
    def get_default_bike(cls):
        bike = cls(10000, "Author", "Basic ASL", 2020, 2000)
        return bike

bike = Bike.get_default_bike() 
bike.set_cost(6000) 
bike.service(300) 
print(bike.sell()) 
print(bike.cost) 
print(bike.make) 
print(bike.year) 
print(bike._sale_price) 
print(bike.sold) 
print(bike.min_profit) 

"""Task 5"""

class MoneyFmt:
    def __init__(self, amount):
        self.amount = amount

    def update(self, new_amount):
        self.amount = new_amount

    """@staticmethod
    def dollarize(float_num):
        if float_num < 0:
            num = format(round(abs(float_num),3),",")
            return f"-${num}"
        else:
            num =format(round(float_num,3),",")
            return f"${num}0" """
    @staticmethod
    def dollarize(float_num):
        formatted_num = "${:,.2f}".format(float_num) # вот тут вопрос
        if float_num < 0:
            formatted_num = formatted_num.replace("$-", "-$")
        return formatted_num
    
    def __repr__(self) -> str:
        return repr(self.amount)
        

    def __str__(self) -> str:
        return self.dollarize(self.amount)




# cash = MoneyFmt(12000)
# cash.update(-0.3)
# print(cash)
# print(repr(cash)) 

