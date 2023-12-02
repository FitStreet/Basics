"""Task 1"""


class Account:
    def __init__(self, name, balance, city):
        self.name = name
        self.balance = balance
        self.city = city
        print("Счет создан")
    def __repr__(self):
        return f"{self.name} {self.balance}"
    def __str__(self) -> str:
        return f"Hello {self.name} {self.balance} {self.city}"
    def __del__(self):
        print("Пока")

# obj_account = Account("Rick", 2013, 'Bishkek')  
# print(obj_account)  
# print(repr(obj_account)) 

"""Task 2"""
class MyNumber(int):
    def __init__(self, value):
        self.value = value
    def __add__(self, other: int) -> int:
        return f"Это сложение и результат равен: {self.value + other}"
    def __sub__(self, other: int) -> int:
        return f"Это вычитание и результат равен: {self.value - other}"
    def __mul__(self, other: int) -> int:
        return f"Это умножение и результат равен: {self.value * other}"
    def __truediv__(self, other: int) -> int:
        return f"Это деление и результат равен: {self.value / other}"

# obj_int = MyNumber(5)  
# print(obj_int + 5)  
# print(obj_int - 5)  
# print(obj_int * 5)  
# print(obj_int / 5)  

"""Task 3"""
class MyList(list):
    def __init__(self, list_):
        self.list_ = list_
    def __getitem__(self, index):
        return self.list_[index - 1]
    
# obj_list = MyList([1,2,3,4,5])  
# print(obj_list[1]) 

"""Task 4"""
class Student: 
    def __init__(self, name, class_name, ball) -> None: 
        self.name = name 
        self.class_name = class_name 
        self.ball = ball 
    def srednee_znach(self): 
        srednee = sum(self.ball.values())/len(self.ball) 
        return srednee 
    def __gt__(self, other): 
        return f'> {self.srednee_znach() > other.srednee_znach()}' 
    def __lt__(self, other): 
        return f'< {self.srednee_znach() < other.srednee_znach()}' 
    def __ge__(self,other): 
        return f'>= {self.srednee_znach() >= other.srednee_znach()}' 
    def __le__(self, other): 
        return f'<= {self.srednee_znach() <= other.srednee_znach()}' 
# obj_student1 = Student('a', 'A', {'math': 100, 'history': 50, 'literature': 88}) 
# obj_student2 = Student('b', 'Aa', {'math': 100, 'history': 50, 'literature': 88}) 
# print(obj_student1 > obj_student2)
# print(obj_student1 < obj_student2) 
# print(obj_student1 >= obj_student2) 
# print(obj_student1 <= obj_student2)

"""Task 5"""
"""class Word(str):
    def __new__(cls,obj):
        return super(Word, cls).__new__(cls)
    
    def __init__(self, word):
        self.word = word.strip()
        
    def __lt__(self, other):
        return len(self.word) > len(other)
    
    def __gt__(self, other):
        return len(self.word) < len(other)
    
    def __le__(self, other):
        return len(self.word) >= len(other)

    def __ge__(self, other):
        return len(self.word) <= len(other)
    def __len__(self):
        return len(self.word)

word1 = Word("H e l l o!")
word2 = Word('world!')  
print(word1 > word2)  
print(word1 < word2)  
print(word1 >= word2)  
print(word1 <= word2) """

class Word: 
    def __gt__(self, other): 
        if len(self.string) > len(other.string): 
            return True 
        else: 
            return False 
    def __lt__(self, other): 
        if len(self.string) < len(other.string): 
            return True 
        else: return False 
    def __ge__(self, other): 
        if len(self.string) >= len(other.string): 
            return True 
        else: 
            return False 
    def __le__(self, other): 
        if len(self.string) <= len(other.string): 
            return True 
        else: return False 
    def __new__(cls, string): 
        instance = super().__new__(cls) 
        instance.string = string.replace(" ", "") 
        return instance
# word1 = Word('H e l l o') 
# word2 = Word('world!') 
# print(word1 > word2) 
# print(word1 < word2) 
# print(word1 >= word2) 
# print(word1 <= word2)

"""Task 6"""

class Kopilka:
    def __init__(self) -> None:
        self.__total = 0
        self.__coins = []

    def add_moneta(self, moneta):
        self.__total += moneta
        self.__coins.append(moneta)

    def __len__(self):
        return len(self.__coins)

    def __getitem__(self, index):
        return self.__coins[index]

    def __iter__(self):
        self.index = 0
        return self

    def __next__(self):
        if self.index < len(self.__coins):
            result = self.__coins[self.index]
            self.index += 1
            return result
        else:
            raise StopIteration

# obj = Kopilka()
# obj.add_moneta(25)
# obj.add_moneta(30)

# print(len(obj))
# for coin in obj:
#     print(coin)

"""Task 7"""
class Anagram(str):
    def __init__(self, word):
        self.word = word

    def __eq__(self, other):
        if self.word == other[::-1]:    
            return True
        else:
            return False

    def __mul__(self, num):
        result = self.word[::-1] * num
        return result
    

# word1 = Anagram('hello') 
# word2 = Anagram('olleh') 
# print(word1 == word2) 
# print(word1 * 3) 
        