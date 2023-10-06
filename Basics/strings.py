"==============Строки==================="
# строки  неизменяемый тип данных, который предназначен для хранения текста, последовательности символов,
#  заключенного в одинарные или двойные кавычки

string = "Hello world"
string1 = 'Hello world'
string2 = "Don't" # внутри двойных кавычек все одинарные просто символы

string3 = '''  Don't "Hello"  ''' # тройные кавычки используются для больших текстов и комментариев 
# могут быть, как одинарные так и двойные("""  """)

print("asdf" + "2") # asdf2
print("asdf" * 2) # asdfasdf

string = "hello"
string2 = "World"
print(string+" "+string2) # hello world

# конкатанация склеивание строк

"===========Экранизация строк======="
"\n" # перенос на новую строку
print("hello\nworld")
#hello
#world

'\t' # табуляция
print("hello\tworld")
#hello    world
print('hello\n\tworld')
#hello
#    world

'\'' # разрешает использовать одинаковые кавычки в одинаковых
print('Don\'t')
print("Hello \\nero") # двойной бэклеш для вывода бэкслеша а тексте

'\v' # переносит строку со смещением вправо на длину предыдущей строки
print('hello\vworld\vmakers\vbootcamp') 
#hello
#     world
#          makers
#                bootcamp

"====================Форматирование строк========================="

title = 'plov'
price = 200

# f строки позволяет использовать переменные в кавычках с помощью {}

print(f"название: {title}\nцена: {price}")

# eda = input("Введите название блюда:")

# print(f"{eda} был вкусный")

# старый вариант форматирования
format2 = "название: {}\nЦена: {}"
print(format2.format(title, price))

format3 = 'Название: %s\nЦена: %s'
print(format3 % (title,price))

"============Методы строк==============="
# методы - функции, который относятся к определенному классу(типу данных), к ним мы обращаемся через точку.

# print(dir(str))
"HELLO".lower() # hello
"hello".upper() # HELLO
"HEllO".swapcase() # heLLo
'hello world'.capitalize() # Hello world
'hello world'.title() # Hello World
'hello world'.capitalize().swapcase() # hELLO WORLD

'hello'.count('l') # 2
'hello'.count('ll') # 1
'hello world'.count('makers') # 0

'hello world'.startswith('he') # True
'hello world'.startswith('He') # False

'hello world'.endswith('sd') # False
'hello world'.endswith('ld') # True

'hello world'.islower() # True
'hello worlD'.islower() # False

'HELLO'.isupper() # True
'hELLO'.isupper() # False

'1234'.isdigit() # True
'1234r'.isdigit() # False

'hello'.isalpha() # True
'hello34'.isalpha() # False

'hello !'.isalpha() # True если есть символы и буквы, но нет цифр будет True

'Hello !'.isalnum() # False если есть цифры или буквы будет True, если есть символы будет False
'1234'.isalnum() # True
"h4".isalnum() # True

'hello world'.split() # ['hello', 'world']
'hello world'.split('o') # ['hello', ' w', 'rld']
'hello world'.split('makers') # ['hello world']

' '.join(['hello', 'world']) # 'hello world' объединяет список в строку разделяя слова разделителем заданным пользователем в ковычках
''.join(['hello', 'world']) # 'helloworld'
'1'.join(['hello', 'world']) # 'hello1world'

'@'.join(['hello', 'world', 'man']) # 'hello@world@man'

string = '                                  hello world                            '
string.strip() # "hello world"
string.lstrip() # 'hello world                            '
string.rstrip() # '                                  hello world'

string = '@asdd@@@sad@@'

string.strip() # asd@@@sad

string.replace('@', '') # asddsad
string.replace('@', '', 4) # asddsad@@

'==============Индексы==============='

# индекс - это порядковый номер элементов последовательности(символа в строке) 
# мндексация начинается с нуля

'h e l l o   w o r l d'
#0 1 2 3 4 5 6 7 8 9 10
#            ...-3 -2 -1
string = 'hello world'
string[2] # 'l'
string[0] # 'h'
string[10] # 'd'
string[-1] # 'd'

# срезы подстрока строки

string[0:5] # 'hello' последний символ не входит в срез
string[:4] # 'hell'
string[6:10] # 'worl' 
string[6:] # 'world' 
string[6:-1] # 'worl'
string[:] # 'hello world'  
string[:2] + string[-2:] # "he" + "ld" = "held"

"hello world"
string[::2] # hlowrd
string[1:5] # ello
string[1:5:2] # el
string[::-1] # dlrow olleh
string[::-2] # drwolh
string[::3] # hlwl

# question isnumeric|isdigit|isdecimal в чем отличие методов


