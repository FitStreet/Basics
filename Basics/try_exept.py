"==================Exeptions================"
# Исключения (ошибки) - объекты, которые прерывают работу кода, если не были обработаны

SyntaxError 
# Исключение которое выходит, когда в коде допущена синтаксическая ошибка
"""
print(
SyntaxError: '(' was never closed
(когда мы не закрыли скобку или кавычку)    
"""
"""
a = 
SyntaxError: invalid syntax
(когда мы сделали что-то не то в синтаксисе)
"""

NameError
# исключение, которое выходит, когда мы обращаемся к несуществующей переменной
"""
name.split()
NameError: name 'name' is not defined
"""

TypeError
# исключение, котрое выходит, когда мы проводим не правильные операции между типами данных


"""
'asdf' + 2
TypeError: can only concatenate str (not "int") to str

{1,2,3, [1,2,3]}
TypeError: unhashable type: 'list'

for i in 124343:
    pass
TypeError: 'int' object is not iterable

input("введи возраст", 1)    
TypeError: input expected at most 1 argument, got 2

[].append()
TypeError: list.append() takes exactly one argument (0 given)
"""

IndexError
list_ = [1,2,3,4,5,6]
# выходит когда указали не существующий индекс
"""
list_[27]
IndexError: list index out of range

list_.pop(45)
IndexError: pop index out of range

"""
KeyError
# выходит, когда мы передали не существующий ключ

"""
dict_ = {'a':6}
dict_['b']
KeyError: 'b'
"""

dict_ = {'a':6}
dict_['b'] = 7
print(dict_.clear())
dict_.get('a')
print(dict_)

ValueError
# выходит когда мы передаем неправильный тип данных в определенную функцию

"""
int("asdf")
ValueError: invalid literal for int() with base 10: 'asdf'
"""

"""
a,b,c = [1,2]
ValueError: not enough values to unpack (expected 3, got 2)
"""

list_ = [1,2]
a = list_[0]
b = list_[1]
a,b = list_

ZeroDivisionError
# выхолит при делении на 0
"""
45 / 0
45 // 0
45 % 0
"""
AttributeError
# выходит, когда мы обращаемся к не существующему методу объект(типу данных)
"""
lst = [1,2,3]
lst.replace(1,'hello')
print(lst)
AttributeError: 'list' object has no attribute 'replace'
"""

"""
string = 'hello'
string.pop(0)
print(string)
AttributeError: 'str' object has no attribute 'pop'
"""

IndentationError
# выходит когда мы не правильно используем отступы
"""
 a = 5
IndentationError: unexpected indent

"""

"""
for i in [1,2,3]:
print(i)
IndentationError: unexpected indent
"""

Exception
# исключение, которое создали, чтобы его вызвать

"===================Вызов исключений==================="

# raise Exception

# raise NameError('я хочу, чтобы эта ошибка вышла')

"=================Обработка искючений================="
# чтобы ыкод не прекращал свою работу, мы можем использовать конструкцию try except и обрабатывать вызванные исключения

# try:
#     age = int(input("Введите свой возраст: "))
# except Exception as e:
#     print('Введите число!', type(e), sep = "|")
play = True
while play:
    try:
        num1 = int(input("Num1: "))
        num2 = int(input("Num2: "))
        print(num1//num2)
        play = False
    except ValueError:
        print("Введи число")
    except ZeroDivisionError:
        print("На ноль делить нельзя")

try:
    age = int(input("Введите свой возраст: "))
    # код, который возможно вызовет ошибку
except ValueError:
    # код, который отработает, когда выйдет ошибка
    print("Введи число")
else:
    # код, который отработает, только если никакая ошибка не вышла
    print("Введенное число:", age)
finally:
    # код, который отработает в любом случае
    print("See you!")

# исключение мы можем словить(обработать)(косяк со стороны клиента)
# ошибку мы не можем словить(обработать)(косяк со стророны разработчика)




KeyboardInterrupt # за что отвечает это исключение


 