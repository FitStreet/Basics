"==================Функции==============="
# именованный блок кода, который может принимать аргументы и возвращать результат

# def func(x:int,y:int,c:int)-> None: # параметры
#     """
#     This function return x+y
#     """
#     return x + y # возвращаю результат
# func(5,4,6) # аргументы 

""" DRY - don`t repeat yourself """ 

# print(["1"].append("2")) # none

# def pif(x:int, y:int, z:int):
#     return (x**2 + y**2)**0.5

# print(pif(5,4,3))

# def my_len(x:str):
#     counter = 0
#     for i in x:
#         counter +=1
#     return counter

# print(my_len("safdsaf"))

# def func():
#     try:
#         return 0
#     finally:
#         return 1
    
# print(func()) # 1

# return value = 0
# return value = 1 

"======================Аргументы и параметры======================"
# параметры - переменные внутри функции, хначения которые мы задаем при вызове функции
# аргументы - значения, которые мы передаем при вызове функции

"======================Виды параметров============================"
# 1.Обязательные параметры
# 2.НЕ обязательные
    # 2.1 по умолчанию(с дефолтом)
    # 2.2 args (все позиционные аргументы в виде кортеже)
    # 2.3 kwargs( все именованные аргументы в словарь)


# def func(a, b=3, *args, **kwargs): # b тут дефолтное значение *args как накопитель **
#     print(args) # (2,4)
#     print(kwargs) 
#     return a + b

# print(func(a = 4, b = 4, c = 3))

"==================Виды аргументов================"
# 1. - Позиционные
# 2. - Именованные

# def func(a,b=5, *args):
#     return a*b
# print(func(1,2,3))
# func(a=5,b=435)

# number1 = 7
# number2 = 6
# func(number1, number2) # 42

# print(func(b=5, a = 435)) # 2175

# # print(func(a=5, 4)) # SyntaxError: positional argument follows keyword argument
# print(func(4))

# def rev(string:str) -> str:
#     """
#     This func reverse string
#     """
#     return string[::-1]

# print(rev('hello')) #olleh

# def func():
#     print(5)
#     return func


# func()()()()

# "руддщ" - "hello"
# "hello" - "руддщ"

# def translate(string:str):
#  eng = "qwertyuiop[]asdfghjkl;'zxcvbnm,."
#  ru = "йцукенгшщзхъфывапролджэячсмитьбю"
#  if string[0] in eng:
#      dict_ = "".maketrans(eng,ru)
#  else:
#      dict_ = "".maketrans(ru,eng)
 
#  return string.translate(dict_)

# print(translate("нщгегиу"))

# def rev(string:str) -> str:
#     """
#     This func reverse string
#     """
#     return string[::-1]

# def is_palindrome(string):
#     if string.lower() == rev(string).lower():
#         return True
#     else:
#         return False
    
# print(is_palindrome("Tenet"))


# """что такое рекурсия ????"""


# "==========================Анонимная функция==============="
# # lambda - АНОНИМНАЯ ФУНКЦИЯ, которая записывается в одну строчку.
# func = lambda x:x**2

# print(func(2)) # 4

# def add_(x,y):
#     return x+y
# def sub_(x,y):
#     return x-y
# def div_(x,y):
#     return x/y
# def mult_(x,y):
#     return x*y

# num1 = int(input("num1:"))
# num2 = int(input("num2:"))
# operation = input("Operation choice:(+|-|*|/.)")
# calc = {
# '+': add_(num1,num2),
# '-': sub_(num1,num2),
# "*": mult_(num1,num2),
# "/": div_(num1,num2)
# }
# print(calc.get(operation, "Такой операции нет"))

# def calc(num1,num2,znak):
#     if znak == "+":
#         return add_(num1,num2)
#     elif num2 == 0 and znak == "/":
#         return "На ноль делить нельзя!"
#     elif znak == '-':
#         return sub_(num1,num2)
#     elif znak == '/' and num2 != 0:
#         return div_(num1,num2)
#     elif znak == '*':
#         return mult_(num1,num2)


# calc = {
# '+': lambda x,y: x+y,
# '-': lambda x,y: x-y,
# '*': lambda x,y: x*y,
# '//': lambda x,y: x//y,
# }


# def main():
#     try:
#         num1 = int(input("num1: "))
#         num2 = int(input("num2:"))
#         operation = input("Operation choice:(+|-|*|/.)")


#         func = calc.get(operation, "Такой операции нет")
#         print(func(num1,num2))
#     except ValueError:
#         print("Введите число!")
#     except KeyError:
#         print("Неизвестный оператор!")
#     except ZeroDivisionError:
#         print("На ноль делить нельзя!")
#     finally:
#         print("До скорой встречи")

# while True:
#     main()
#     answer = input("Завершить? (y/n)")   
#     if answer.lower() == 'y':
#         break

