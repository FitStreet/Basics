"=====Пременные======"

# Переменная это ссылка на ячеку памяти, где хранятся данные.

# ячейка памяти - [num1 = {10},str1 = {"Hello world!"},{}]

num1 = 10 
str1 = "Hello world!"

num1 = 10
num2 = 15

print(num1 + num2)

"..........Правила наименовывания переменных........"   
a = 5 # по назначению
# 1num = 4 нельзя называть переменные с чисел 
# num-li1 = 5 нельзя испрользовать символы, кроме _
# print = 10 не называть переменные встроенными названиями функций


hello_world = 7 # Snake case
helloWorld = 8 # Camel case

".........Ввод и вывод дынных......."

# print - output in terminal
# input - ввод данных из терминала

"...........Типы данных..........."
# 2 вида : изменяемые и неизменыемые
# Изменяемые: list(), dict(словарь), set(множества)
# Неизменяемые: int(), float(), complex, str(), tuple, bool(true, false), none


# Изменяемые
list_ = [1,2,3,4] #список
dict_ = {'a': 1, 'b' :2} #словарь
set_ = {1,2,3,4,4} # только уникальные значения


# Неизменяемые

int_ = 10
float_ = 0.5
str_ = 'Hello world!'
tuple_ = (1,2,3,4)
bool_1 = True
bool_0 = False
none_ = None

print('Izmen', list_, dict_, set_)
print('Neizmen', int_, float_, str_, tuple_, bool_1, bool_0, none_)

# print("Введите 2 числа и получите сумму")
# num1 = int(input("Первое число:"))
# num2 = int(input("Второе число:"))
# summa = num1 + num2
# print(f"Сумма чисел > {summa}")
