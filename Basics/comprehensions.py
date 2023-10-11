"=================Comprehensions================="
#comprehensions - генератор, который мы можем использовать, чтобы создать последовательность используя цико For в одну строчку

# результат for элемент in последовательность
# результат for элемент in последовательность if фильтрация


comprehension = (i for i in range(1,6))
# генератор - итериркемый объект, который не хранит в себе полностью всю последовательность, а содает их когда требуется
# print(comprehension) # generator object
# for i in comprehension:
#     print(i)

# print(next(comprehension)) # 1
# print(next(comprehension)) # 2
# print(next(comprehension)) # 3
# print(next(comprehension)) # 4
# print(next(comprehension)) # 5
# print(next(comprehension)) # StopIteration

# next функция , которая запрашивает у генератора текущий элемент и генератор создает элемент

"============Синтаксический сахар============"

# list_comprehension = list( (i for i in range(1,6)) )
# print(list_comprehension) # [1, 2, 3, 4, 5]
# list_comprehension = [i for i in range(1,6) if i % 2 == 0]
# print(list_comprehension) # [2, 4]

# lst = [i for i in range(1,101) if i % 2 != 0]
# print(lst)
# lst1 = [i*2 for i in range(1,101)]
# print(lst1)

# lst = ['hello' for i in range(5)]
# print(lst) # ['hello', 'hello', 'hello', 'hello', 'hello']

# lst = ["Fizz" if i % 3 == 0 else i for i in range(1, 101)]
# print(lst) # [1, 2, 'Fizz', 4, 5, 'Fizz', 7, 8, 'Fizz', 10, 11, 'Fizz', 13, 14, 'Fizz', 16, 17, 'Fizz', 19, 20, 'Fizz' ....

# matrix = [
#     [0,0,0],
#     [1,1,1],
#     [2,2,2]
#          ]
# lst = [j for i in matrix for j in i ]
# print(lst) # [0, 0, 0, 1, 1, 1, 2, 2, 2]

"====================Set comprehension==================="

# result = {i for i in range(1, 11)}
# print(result) # {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
# set1 = set(range(1,11))
# print(set1) # {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}

result = {i if i%2==0 else i*2 for i in range(1,21)}
print(result) # {2, 34, 4, 6, 38, 8, 10, 12, 14, 16, 18, 20, 22, 26, 30}

# если условие находится в начале то это тернарные условия(добавляется оператор else)
# если условие в конце то это фильтрация

"====================Dict Comprehension=========="

# dict_ = {}
# for i in range(1,11):
#     dict_.update({i:i**2})
# print(dict_) # {1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64, 9: 81, 10: 100}
# result = {i:i**2 for i in range(1,11)}
# print(result) # {1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64, 9: 81, 10: 100}

# lst = [1,1,2,2,2,4,4,4,4,4]
# dict_ = {i:lst.count(i) for i in lst}
# print(dict_) # {1: 2, 2: 3, 4: 5}

# lst1 = [1,1,2,2,2,4,4,4,4,4]
# dict_1 = {}
# for i in lst1:
#     dict_1.update({i:lst1.count(i)})
# print(dict_1) # {1: 2, 2: 3, 4: 5}

# inp1, inp2, inp3 = [input() for i in range(3)]
# print(inp1, inp2, inp3)

# dict_ = {'a': 2, 'b': 3}
# dict_ = {val:key for key, val in dict_.items()}
# print(dict_) # {2: 'a', 3: 'b'}

# dict_ = {'a': 2, 'b': 3}
# dict_1 = {key: "четное" if val % 2 == 0 else "нечетное" for key, val in dict_.items()}
# print(dict_1) # {'a': 'четное', 'b': 'нечетное'}

# dict_ = {'a': 2, 'b': 3}
# dict2 = {}
# for k, v in dict_.items():
#     if v % 2 == 0:
#         dict2.update({k:"четное"})
#     else:
#         dict2.update({k:"нечетное"})
# print(dict2) # {'a': 'четное', 'b': 'нечетное'}
