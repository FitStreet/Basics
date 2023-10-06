'===========================словари================'
# dict - изменяемый, итерируемый, неиндексируемый, неупорядоченный тип данных, где данные хранятся в парах (ключ: значение)

user = {
    'name':'Ivan',
    'password':'12345678',
    'last_name': 'Godin'
    }
print(user['password']) # 12345678

# ключами в словаре могут быть только неизменяемые типы данных
dict1 = {'a': 1, 'b': 5, 'a':5, 'a': 6}
print(dict1['a'])# 6
# при одинаковых ключах выводится будет только последнее значение ключа в словаре
# print(dict['c']) # KeyError: 'c'

'===============Создание================'

dict1 = {'a': 'hello'}
dict1 = dict([('a', 'hello')]) # {'a': 'hello'}

dict2 = dict(['ab', 'cd']) # {'a':'b','c':'d'} длина переменной списка не должна превышать 2 символа

dict1 = {}
dict1['name'] = 'Ivan'
# {'name':'Ivan'}
dict1['name'] = 'Tima'
# {'name':'Tima'}

'KISS' # keep it simple stupid

'=========Методы Словаря================='
# get метод который возвращает значение по ключу, если такого ключа нет выводит None , или дефолтное значение
user = {
    'name':'Ivan',
    'password':'12345678',
    'last_name': 'Godin'
    }
# print(user['nam']) # KeyError
print(user.get('nam')) # None
print(user.get('nam', 'yes')) # yes

# pop удаляет пару по ключу и возвращает значение
dict1 = {'a': 1, 'b': 2}
popped = dict1.pop('a')
print(dict1, popped) # {'b': 2} 1

#del оператор удаления
#del dict1['v'] # KeyError
del dict1['b']
print(dict1) # {}

# popitem удаляет последнюю пару и возвращает ее
dict1 = {'a':1, 'b':2}
popped = dict1.popitem()
print(dict1, popped) # {'a':1} ('b': 2)

# update добавляет новую пару, если есть существующая пара, то он заменяет ее
dict1 = { 1: "a", 2: "b", 3: "c"}
dict1[4] = "d"
dict1.update({5: "e"})
print(dict1) # {1: 'a', 2: 'b', 3: 'c', 4: 'd', 5: 'e'}

# clear полностью очищает словарь
dict1 = { 1: "a", 2: "b", 3: "c"}
dict1.clear()
print(dict1) # {}

# keys - возвращает все ключи словаря 
# values - возвращает все значения словаря 
# items - возвращает все пары (ключ, значение) словаря 

user = {
    'name':'Ivan',
    'password':'12345678',
    'last_name': 'Godin'
    }

print(user.keys()) # dict_keys(['name', 'password', 'last_name'])
print(user.values()) # dict_values(['Ivan', '12345678', 'Godin'])
print(user.items()) # dict_items([('name', 'Ivan'), ('password', '12345678'), ('last_name', 'Godin')])

"============================Итерирование словарей===================="

user = {
    'name':'Ivan',
    'password':'12345678',
    'last_name': 'Godin'
    }
for key in user:
    print(key)
    # при итерации в словарях будут приходить только ключи
for values in user.values():
    print(values)
    # при итерации dict_values будут приходить только ключи
for i in user.items():
    print(i)
    # при итерации dict_items будут приходить пары ключ и значение в виде tuple
for key, values in user.items():
    print(key, values)
    # при итерации dict_items будут приходить отдельно ключи и отдельно значения в виде tuple

item = ('name', 'Ivan')
key, values = ('name', 'Ivan')

dict_1 = {'a': 1, 'b': 2, 'c': 3}
dict_2 = {}
for key, values in dict_1.items():
    dict_2.update({values: key})
print(dict_2)