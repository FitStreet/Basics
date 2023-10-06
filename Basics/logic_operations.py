"================== Логические и  условные операторы ======================="
# Логические операторы - выражения которые возвращают True, если выражение верное или False, если выражение ложно

# равенство
5==5 # True
4==5 # False

# не равенство
4!=5 # True
5!=5 # False

# больше
5>4 # True
4>5 # False
5>5 # False

# меньше
5<4 # False
5<19 # True
5<5 # False

# больше или равно
5>=10 # False
10>=5 # True
5>=5 # True

# меньше или равно
10<=5 # False
5<=10 # True
5<=5 # True

'5'=='5' # True
'5'==5 # False
'hello'=='hello' # True
'Hello'=='hello' # False

'=============And Or Not======================='
# and - и
# or - или
# not - не

a = 5
b = 6

# True and True
a == 5 and b == 6 # True
# True and False
a == 5 and b == 6 # False
# False amd False
a == 3 and b == 3 # False

# Если хоть одно True, будет True
a == 5 or b == 6 # True
a == 5 or b == 5 # True
a == 4 or b == 4 # False

not True # False
not False # True

not a == 5 # False (потому что a == 5)
not a == 4 # True (потому что a != 4)

# is | ==  "==" Возвращает True если сравниваемые объекты имеют одинаковые значения.
# оператор "is" возвращает True если сравниваемые объекты помимо того, что имеют одинаковые значения, еще и ссылабтся на одну и туже область памяти.
# Таким образом, is отличается от == в Python, дополнительной проверкой на идентичность адресов в памяти, на которые ссылаются переменные.
# Если сравнивать переменные от -5 до 256, вывод у == и у is будет одинаковый(под числа от -5 до 256 в Python отводится отдельная область памяти
# и любая переменная со значением из указанного диапозона будет ссылатся на эту заранее выделенную область в памяти)

not 5 == 5 and 6 == 6 # False
not 5 == 5 and 7 == 0 # True
not 7 >= 5 or 6 <= 4 # False
not not not True # False

'==============Boolean type======================'
# Булевый тип данный имеет всего 2 значения True и False

bool(1) # True
bool(0) # False
bool(-22) # True Все значения отличные от нуля, будет True

bool('') # False
bool(' ') # True
bool('hello') # True

bool(True) # True
bool(False) # False
bool('False') # True

bool([]) # False
bool([[]]) # True

"=====================None Type======================"
# None неизменяемый тип данных с одним значением None, который используется для обозначения отсутствия значения 
bool(None) # False
bool('None') # True

a = None
a == None # True

'hello world' == 'hello' # False
'hello' in 'hello world' # True
# print('hello' >= 'hellw') # False как сравнивать строки сроки и почему тут False

# str1 = 'hello'
# str2 = 'hellw'

# for i in range(5):
#     print(f"{str1[i]} = {ord(str1[i])} -- {str2[i]} = {ord(str2[i])}")  

"========================Условные операторы==================="
# условные операторы это - конструкция, которая используется для того, чтобы разных входных данных код работал по разгому(в зависимости от условия)

# if условие:
#     тело конструкции
#     # тело будет выполнятся, если усоловие верное

# if условие:
#     тело конструкции
#     # тело будет выполнятся, если усоловие верное
# else:
#     тело2
#     # тело2 будет выполнятся во всех других случаях

# if условие1:
#     тело1 конструкции
#     # тело1 будет выполнятся, если усоловие1 верное
# elif условие2:
#     тело2
#     # тело2 будет выполнтся если условие1 не верное,а условие2 верное
# else:
#     тело3
#     # тело3 будет выполнятся, только если все вышеуказанные условия не верные.

# n = int(input())

# if n == 0:
#     print("ZERO")
# elif n < 0:
#     print("NEGATIVE")
# else:
#     print("POSITIVE")

"=====================Тернарные операторы============"
# тернарные опраторы - условие в одну строчку
# тело1 if условие else тело2

# m = int(input())

# print("hello") if m == 5 else print('bye')

#примите число от пользователя
# если число кратно 3, выведите Fizz
# если число кратно 5, выведите Buzz
# если число кратно 5 и 3, выведите FizzBuzz
# выведите число во всех остальных случаях

num = int(input('Введите число:'))

if num % 3 == 0 and num % 5 == 0:
    print("FizzBuzz")
elif num % 3 == 0:
    print("Fizz")
elif num % 5 == 0:
    print("Buzz")
else:
    print(num)








 