"=======================Модули и Пакеты================"
# Модуль - любой файл с расширением .py
# Пакет - набор модулей(обязательно должен быть файл __init__.py)

# import math # Модули
# import collections # Модули
# import itertools # Модуль


"======================Работа с файлами================"
# file = open("test.txt", "r") 
# print(file.read())
# open - функция, которая открывает файл в определенном режиме

# r - read (только для чтение)
# w - write (только для записи), перезаписывает файл
# a - append (только для дозаписи, добавляет в конец файла)
# x - создает файл, если такой файл существует, выдает ошибку
# b - binary (выдает всю информацию в файле в бинарном виде(0 и 1))

"""================READ"""
try:
    file = open('test.txt', 'r')
    print(dir(file))
    print(file.readable()) # True проверка на читабельность
    print(file.writable()) # False проверка на записываемость
    print(file.read()) # весь файл (str)
    print(file.tell()) # показывает текущее положение каретки
    file.seek(0) # управляет положением каретки
    print(file.readline()) # возвращает строку (str)
    print(file.readlines()) # возвращает список из строк(list)
finally:
    file.close() # закрывает файл

"""================WRITE"""
try:
    file = open('test.txt', 'w') # 'w' стирает все в файле перед открытием
    file.write("My name is Anton \n") # Принимает строку и записывает в файл и возвращает индекс положения каретки
    file.seek(17)
    file.write("My name is Anton \n")
    file.writelines(['Makers\n', 'Bootcamp\n']) # принимает список из строк и записывает его элементы в файл
finally:
    file.close()

file = open('test.txt', 'r')

"""================APPEND"""
try:
    file = open('test.txt', 'a') # флаг a добавляет строку в конец списка
    file.write("\n Hello!") # добавит строку в конец файла(если флаг а)
    file.seek(0) # не работает с флагом а
    file.write("i am John\n")
finally:
    file.close()

"=========================Контекстный менеджер====================="

with open('test.txt', 'r') as file:
    print(file.read())

with open('test.txt', 'a') as file:
    file.write("hello\n")

# with open('ertay.py', 'x') as file:
#     if file.writable():
#         file.write('print("hello world")')