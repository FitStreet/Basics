"===================Области видимости==================="
#LEGB - local enclose glodbal built-in

"====================Built-in================"
# встроенное пространство имён - (print, input, max, min, ..........)
# a = 5
# print(dir(__builtins__))
"=========================Global========================"
# Глобальное пространство - пространство имен, в котором хранятся все глобальные переменные, которые мы объявили внктри этого файла
# чтобы псмотреть все глобальные переменные можно использовать функцию globals  (print(globals()))

# def func():
#     pass
# b = 7
# n = 8
# print(globals())
"=====================Enclosed=========================="
# замкнутое пространство имен - локальное пространство у которого есть внутренние локальное пространство
var = "глобальная переменная"
print(var)
def func():
    var = "замкнутая переменная"
    print(var)
    def inner_func():
        var = "локальная переменная"
        print(var)
    inner_func()
func()
# global enclosed local 

"=====================Local====================="
#локальное пространство имен - перменные, созданные внутри функции

# a = 10
# def func(a,b):
#     print(a)
#     n = 8
#     def inner_func(a,b):
#         pass
#     inner_func(5,7)

# count = 0
# def counter():
#     global count # global дает возможность получить глобальную пересенную в локальном пространстве
#     count += 1
#     print(count)
# counter() # 1
# counter() # 2
# counter() # 3
# counter() # 4

# def count():
#     counter = 0

#     def inner_count():
#         nonlocal counter # дает возможность использовать замкнутую переменную в локальном пространстве
#         counter += 1
#         a = 6
#         print(counter)
#     inner_count()
#     return counter
# print(count())

# print(locals())

# питон ищет переменную из свего пространства на верх(по принципу LEGB) 

# x = 2
# def check():
#     x = x * 2
#     print(x)
# check()