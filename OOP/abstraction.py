# абстракция - принцип ООП, в котором создается класс пустышка, где задаются названия атрибутов и методов, для того чтобы в дочерних классах не забыть их переопределить

from abc import ABC, abstractmethod, abstractproperty

class A(ABC):
    @abstractmethod
    def func(self):
        pass
    
    @abstractproperty
    def a(self):
        pass

class B(A):
    a = 8
    def func(self):
        print("B")

b = B()

class AbstractAnimal(ABC):
    
    @abstractmethod
    def voice(self):
        pass

    @abstractproperty
    def legs(self):
        pass

    @abstractmethod
    def move(self):
        pass

class Dog(AbstractAnimal):
    
    legs = 4

    def voice(self):
        print("Гав-гав")

    def move(self):
        print("walk")

dog = Dog()

class Bird(AbstractAnimal):
    
    legs = 2
    
    def voice(self):
        print("фью-фью")

    def move(self):
        print("fly")

bird = Bird()

class Shape(ABC):

    @abstractmethod
    def calculate_area(self):
        pass

    @abstractmethod
    def calculate_perimetr(self):
        pass

    @abstractproperty
    def angle(self):
        pass

class Square(Shape):
    angle = 4
    def __init__(self,side) -> None:
        self.side = side

    def calculate_area(self):
        return self.side ** 2
    
    def calculate_perimetr(self):
        return self.side * 4
    
class Triangle(Shape):
    angle = 3
    def __init__(self, side, side1, side2) -> None:
        self.side = side
        self.side1 = side1
        self.side2 = side2
    
    def calculate_perimetr(self):
        return self.side + self.side1 + self.side1
    
    def calculate_perimetr(self):
        s = (self.side+self.side1+self.side2) / 2
        s1 = (s * (s-self.side) * (s-self.side1) (s-self.side2)) ** 0.5
        return s1


class PaymenySystem(ABC):

    @abstractmethod
    def make_payment(self):
        pass

    @abstractmethod
    def get_balance(self):
        pass

    @abstractproperty
    def balance(self):
        pass


class CreditCard(PaymenySystem):
    balance = 100

    def __init__(self, cardnumber, year) -> None:
        super().__init__()
    
    def make_payment(self, amount):
        if amount > self.balance:
            print("Не хватает средств на балансе")
        else:
            self.balance -= amount
    def get_balance(self):
        return self.balance
    


class MBank(PaymenySystem):
    balance = 200
    def __init__(self,phone_number, password) -> None:
        self.phone_number = phone_number
        self.password = password
    
    def make_payment(self, amount):
        if amount > self.balance:
            print("Не хватает средств на балансе")
        else:
            self.balance -= amount
    
    def get_balance(self):
        return self.balance

creditcard = CreditCard(9999999999999999, 2023)
mbank = MBank("0221143708", "qwerty" )

creditcard.make_payment(104)
print(creditcard.get_balance())