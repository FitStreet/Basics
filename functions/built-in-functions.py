"===========================Втроенныее функции======================"

# print(dir(__builtins__)) # [встроенные функции в питоне]
# print, input, list, sorted, sum, len, abs, isinstance, type
# map, filter, zip, reduce, enumerate 

# zip - соединяет несколько последовательностей(итерируемые объекты)
# list1 =[1,2,3,4,5]
# list2 = ['a', 'b', 'c', 'd']
# list3 = [10.5, 11.5, 12.5, 13,5]
# print(list(zip(list1,list2,list3))) # [(1, 'a', 10.5), (2, 'b', 11.5), (3, 'c', 12.5), (4, 'd', 13)]
# print(dict(zip(list1,list2))) # {1: 'a', 2: 'b', 3: 'c', 4: 'd'}

# list1 = [[1],[2],[3],[4]]
# list2 = ['a', 'b', 'c', 'd']
# new_dict = dict(zip(list1, list2))
# print(new_dict) # TypeError

# enumerate - нумерует последовательность(по умолчанию с нуля)б можно задать стартовую цифру list(enumerate(list1, 1))
# list1 = ['a', 'b', 'c', 'd']
# new_list = list(enumerate(list1, 1))
# # [(0,"a"), (1, 'b') .....]
# for i,val in new_list:
#     print('index = ',i ,'value = ', val)

# map - принимает функцию и последовательность (записывает в новую последовательность результат функции)

# list1 = ['1', '2', '3','4']
# # list1 = [int(i) for i in list1]
# list1 = list(map(int, list1))
# print(list1)

# # def func(x):
# #     return x ** 2
# list1 = [i**2 for i in list1]
# list1 = list(map(lambda x: x**2, list1))
# print(list1)

# filter - принимает функцию и последовательностьб фильтрует в по тому что возвращает наша функция(если True оставляет, если False убирает)

# list_1 = [-1, -2, 0, 1, 12, -0.5]
# def func(x):
#     return x >= 0
# list_1 = list(filter(func, list_1))
# print(list_1)

# reduce - принимает функцию с двумя аргументами и последовательность, возвращает результат полученный из двух аргументов

# from functools import reduce

# list1 = [1,2,4,5,6]
# def func(x,y):
#     print(x,y)
#     return x+y
# list1 = reduce(func,list1)
# print(list1) # 18
# def func(x,y):
#     if x>y:
#         return x
#     else:
#         return y

# list1 = reduce(lambda x,y: x if x>y else y,list1)
# print(list1)




