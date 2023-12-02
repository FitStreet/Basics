# Магический методы - это в первую очередь те методы, который записываются через __"метод"__, срабатывают они при выполнении операции (>< * - . == + / ** %)
# dunder methods - double underscore methods

# new - конструктор класса, отвечает за создание объекта   
# init - инициализатор класса(работает как конструктор), задает созданному объекту атрибуты
# del - деструктор класса, отвечает за удаление объекта 

# class User:
#     def __new__(cls, *args, **kwargs):
#         print("new worked: ")
#         super().__new__(cls)

#     def __init__(self, name, email):
#         print("init worked: ")
#         self.name = name
#         self.email = email

#     def __del__(self):
#         print("del worked: ")


# user = User("Nikita", "nikita@gmail.com")



class MyInt(int):
    def __init__(self, value) -> None:
        self.value = value

    def __add__(self, other: int) -> int:
        return f"Это сложение и результат равен: {self.value + other}"
    
    def __sub__(self, other: int) -> int:
        return f"Это вычитание и результат равен: {self.value - other}"
    
    def __mul__(self, other: int) -> int:
        return f"Это умножение и результат равен: {self.value * other}"

    def __truediv__(self, other: int) -> float:
        return f"Это деление(/) и результат равен: {self.value / other}"
    
    def __floordiv__(self, other: int) -> float:
        return f"Это деление(//) и результат равен: {self.value // other}"

    def __lt__(self, other: int) -> bool: # lower then
        return f"Это знак <: {self.value < other}"
    
    def __gt__(self, other: int) -> bool: # greater then
        return f"Это знак >: {self.value > other}"
    
    def __eq__(self, other: int) -> bool: # equal
        return f"Это знак ==: {self.value == other}"
    
    def __ne__(self, other: int) -> bool: 
        return f"Это знак !=: {self.value != other}"

    def __le__(self, other: int) -> bool: 
        return f"Это знак <=: {self.value <= other}"
    
    def __ge__(self, other: int) -> bool: 
        return f"Это знак <=: {self.value >= other}"
    
    # ** - __pow__
    # % - __mod__
# В чем отличие маг.методов с буквой r в начале и без нее

# obj_int = MyInt(5)
# "------------------"
# print(obj_int+9)
# "||"
# # obj_int.__add__(9)
# "------------------"
# print(obj_int-9)
# "||"
# # obj_int.__sub__(9)
# "------------------"
# print(obj_int*9)
# "||"
# # obj_int.__mul__(9)
# "------------------"
# print(obj_int/9)
# "||"
# # obj_int.__truediv__(9)
# "------------------"
# print(obj_int//9)
# "||"
# # obj_int.__floordiv__(9)
# "------------------"
# print(obj_int>9)
# "||"
# # obj_int.__lt__(9)
# "------------------"
# print(obj_int<9)
# "||"
# # obj_int.__gt__(9)
# print(obj_int == 9)

# __getitem__ - поиск элемента объект[элемент]


a = "asdf"
a[0]
dict_ = {"a": 5}
dict_.__getitem__('a')

class MyStr(str):
    def __init__(self, value) -> None:
        self.value = value
    def __getitem__(self, __key) -> str:
        __key += 1
        return super().__getitem__(__key)
    
    def __setitem__(self, __key, new):
        old = self.value[__key]
        self.value = self.value.replace(old, new)
    
    def __str__(self) -> str:
        return self.value


mystr = MyStr("nikita")
# print(mystr[0])
mystr[3] = "tt"
print(mystr)   

    
