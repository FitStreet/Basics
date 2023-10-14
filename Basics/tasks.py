# sets task 13

# robert = {5, 7, 11, 10, 28} 
# kail = {1, 5, 14, 8, 22} 
# merri = {19, 20, 3, 11, 10}

# kail_guess = len(robert.intersection(kail)) > 0
# merri_guess = len(robert.intersection(merri)) > 0

# if kail_guess and merri_guess:
#     print("kail merri")
# elif kail_guess:
#     print("kail")
# elif merri_guess:
#     print("merri")
# else:
#     print("no one")

#task 14

# tilek = {'Dodo', "imperiaPizza", "FreshBox"}
# timur = {'OchakKebab', "FreshBox"}
# alexander = {"FreshBox", "KFC"}
# elina = {"Mac", "Subway"}
# elina |= tilek
# elina |= timur
# elina |= alexander

# tilek.intersection_update(timur)
# tilek.intersection_update(alexander)
# tilek.intersection_update(elina)

# print(tilek)

# ingredients = {"cыр чеддар","грибы", "соус","шпинат"} 

# ingredients.add("помидор")
# ingredients.discard("колбаса")
# ingredients.remove("шпинат")
# ingredients.add("базилик")
# ingredients.remove("cыр чеддар")
# ingredients.add("сыр моцарелла")

# print(ingredients)


# a = [set(), set(), set()]

# inp1 = 'Hello world'
# inp2 = 3
# if inp2 == 1:
#     a[0].add(inp1)
# else:
#     a[0].add("default value")

# if inp2 == 2:
#     a[1].add(inp1)
# else:
#     a[1].add("default value")

# if inp2 == 3:
#     a[2].add(inp1)
# else:
#     a[2].add("default value")
# print(a)

# set1 = {i for i in range(10) if i % 2 == 0}
# set1 = {i for i in range(0,10,2)}
# set2 = {i for i in range(1,10,2)}
# print(set1)
# if set1.intersection(set2):
#     print("Множества пересекаются!")
# else:
#     print("Множества не пересекаются!")
    

"============================Comprehensions================"
# dict_ = {k:k**2 for k in range(1,11)}
# print(dict_)

"task 11"
# a = {'a': 1, 'b': 5, 'c': 4, 'd': 3}
# dict_ = {k:[v for v in range(1,v+1)] for k,v in a.items()}
# print(dict_)

"task 13"
# string_ = 'In 1984 there were 13 instances of a protest with over 1000 people attending'
# list_ = [i for i in string_.split(" ") if i.isdigit() ]
# print(list_)

"task 14"
# dict_ = {'Timur': {'history': 90, 'math': 95, 'literature': 91},
 
# 'Olga': {'history': 92, 'math': 96, 'literature': 81},
 
#  'Nik': {'history': 84, 'math': 85, 'literature': 87}}

# result_dict = {student: max(subjects, key=subjects.get) for student, subjects in dict_.items()}

# print(result_dict)

"task 15"
# my_dict = {'first': {'a': 1}, 'second': {'b': 2}} 
# dict_ = {k:int(list({val for val in v.values()})[0])for k,v in my_dict.items()}
# print(dict_)

"task 26"
# dict_ = {'a': {'d': 3, 'e': 45}, 'b': {'f': 23, 'j': 9}, 'c': {'h': 12, 'i': 89}}
# list_ = [i for v in dict_.values() for i in v.values()]
# print(list_)

"task 28"
# dict_ = {"Sedan": 1500, "SUV": 2000, "Pickup": 2500, "Miivan": 1600, "Vann": 2400, "Semi": 13600, "Bicycle": 7, "Motorcycle": 110}

# list_ = [k.upper() for k,v in dict_.items() if 200 <= v <= 5000]

# print(list_)

"task 29"
# dict1 = {"Sedan": 1500, "SUV": 2000, "Pickup": 2500, "Miivan": 1600, "Vann": 2400, "Semi": 13600, "Bicycle": 7, "Motorcycle": 110}

# dict2 = {k.replace("i",""):k.count('i') for k,v in dict1.items()}
# print(dict2)

"task 30"
# list1 = [1, 2, 3, 0, None, 'a', 'abc', [], 23, [1, 2, 3, 4], '', {'a': 1, 'b': 2}, 'drf', []]
# a = [0, None, [], {}, '']
# list2 = [i for i in list1 if i not in a]
# print(list2)

# SPL_Patrons = [
# ['Kim Tremblay', 134],
# ['Emily Wilson', 42],
# ['Jessica Smith', 215],
# ['Alex Roy', 151],
# ['Sarah Khan', 105],
# ['Samuel Lee', 220],
# ['William Brown', 24],
# ['Ayesha Qureshi', 199],
# ['David Martin', 56],
# ['Ajeet Patel',69]
# ]

'task 31'
# list1 = [k for i in SPL_Patrons for k in i if type(k) == str and i[1] > 100 ]
# print(list1)

"task 32"
# sved_amount = [round(i[1] * 11.95, 2) for i in SPL_Patrons]
# print(sved_amount)

"task 33"
# prairie_pirates = [
# ['Tractor Jack', 1000, True],
# ['Plowshare Pete', 950, False],
# ['Prairie Lily', 245, True],
# ['Red River Rosie', 350, True],
# ['Mad Athabasca McArthur', 842, False],
# ['Assiniboine Sally', 620, True],
# ['Thresher Tom', 150, True],
# ['Cranky Canola Carl', 499, False]
# ]

# pirat = [[i[0],i[1] * 42] for i in prairie_pirates if i[2] == True]
# print(pirat)

# dict_ = {
#     'Sasha': {
#         'likes': 23,
#         'comments': 2,
#         'rating': 4
#     },
#     'Aliya': {
#         'likes': 34,
#         'comments': 5,
#         'rating': 5
#     },
#     'Dasha': {
#         'likes': 15,
#         'comments': 3,
#         'rating': 2
#     },
#     'Luna': {
#         'likes': 12,
#         'comments': 2,
#         'rating': 1
#     },
#     'Rena': {
#         'likes': 26,
#         'comments': 7,
#         'rating': 2
#     }
# }
# list_ = [1, 4, 9, 16, 25, 36] 
# try:
#     print(list_[27])
# except IndexError:
#     print("Нет такого элемента!")


# try:
#     num1 = int(input())
#     num2 = int(input())
#     print(num1/num2)
# except ValueError:
#     print("Произошла ошибка!")
# except ZeroDivisionError:
#     print("Произошла ошибка!")

# try:
#     cash = int(input())
#     if cash < 0:
#         raise ValueError("Сумма не может быть отрицательной!")
#     else:
#         print(cash)
# except ValueError as e:
#     print(e)

# try:
#     age = int(input())
#     if age < 18:
#         raise ValueError("Доступ запрещён")
# except ValueError:
#     print("Введен некорректный возраст")
# else:
#     print("Спасибо")
# finally:
#     print("До свидания!")

# dict_ = {
#     'Sasha': {
#         'likes': 23,
#         'comments': 2,
#         'rating': 4
#     },
#     'Aliya': {
#         'likes': 34,
#         'comments': 5,
#         'rating': 5
#     },
#     'Dasha': {
#         'likes': 15,
#         'comments': 3,
#         'rating': 2
#     },
#     'Luna': {
#         'likes': 12,
#         'comments': 2,
#         'rating': 1
#     },
#     'Rena': {
#         'likes': 26,
#         'comments': 7,
#         'rating': 2
#     }
# }

# dict_ = sum([like for v in dict_.values() for key,like in v.items() if v["rating"] > 3 and key == "likes"])
# print(dict_)

# list_name = ['paul', 'john', 'george', 'ringo', 'eric', 'patty', 'yoko', 'cynthia', 'linda', 'jude' ] 
# dict_ = {i:len(i)**2 for i in list_name if len(i) > 4} 
# print(dict_)

# dict_ = {
#     'Dasha': {
#         'likes': 15,
#         'comments': [
#             {'id': 1, 'text': 'some text'},
#             {'id': 2, 'text': 'some text'},
#         ],
#         'rating': 2
#     },
#     'Luna': {
#         'likes': 12,
#         'comments': [
#             {'id': 1, 'text': 'some text'},
#             {'id': 2, 'text': 'some text'},
#             {'id': 3, 'text': 'some text'},
#         ],
#         'rating': 1
#     },
#     'Rena': {
#         'likes': 26,
#         'comments': [
#             {'id': 1, 'text': 'some text'},
#             {'id': 2, 'text': 'some text'},
#             {'id': 3, 'text': 'some text'},
#             {'id': 4, 'text': 'some text'},
#             {'id': 5, 'text': 'some text'},
#             {'id': 6, 'text': 'some text'},
#         ],
#         'rating': 2
#     }
# }

# comment_ids = [comment['id'] for user_data in dict_.values() for key, val in user_data.items() if key == "comments" and len(val) > 3 for comment in val]
# print(comment_ids)

# list_ = [i/2 for i in range(11) if i % 2 == 0]
# print(list_)

# dict_ = {1:"asd", 2: "fgha", 3: "treas"}
# dict_ = {k:len(v) if k % 2 == 0 else len(v)**3 for k,v in dict_.items()}
# print(dict_)

# import random

# set1 = {random.randint(0, 20) for _ in range(11)}
# set2 = {random.randint(10, 30) for _ in range(11)}

# full_set = set1 | set2

# full_set_length = len(full_set)

# duplicates = 20 - full_set_length
# print(set1)
# print(set2)

# if duplicates > 0:
#     print(f"В этом сете было {duplicates} повторения, его длина составляет {full_set_length}")
# else:
#     print("Ваш объединенный сет полностью уникальный!")

# list_ = [1, 2, 3]
# try:
#     list_.get(1,2)
# except AttributeError:
#     print("Так нельзя!"

# try:
#     string = "asdf"
#     num = 1
#     print(string + num)
# except TypeError:
#     print("usupported option")
# try:
#     for i in range(11):
#         list_.append(i)
# except NameError:
#     print("нет такой переменной")
# try:
#     list_ = [1, 2, 3, 4]
#     for i in range(0, len(list_) + 1):
#         print(list_[i])
# except IndexError:
#     print("index out of range")

# password = "Stdv"

# if len(password) < 6:
#     raise ValueError("Wrong password")

# warehouse = [
#     ['1', '2', '3'],
#     [1, 2],
#     [[1], [2], [3]],
#     [[1, 2, 3], [1, 2, 3, 4, 5], {'hello': 'world'}],
# ]
# if len(warehouse) > 10:
#     raise ValueError("много коробок")
# for i in warehouse:
#     if len(i) > 3:
#         raise ValueError("ytn vtcnf d rjhj,rt")

# def to_fahrenheit(k:int) -> float:
#     assert k >= 0, "Холоднее абсолютного нуля!"
#     return (k-273.15)*1.8 +32

# try:
#     import lamabimgo
# except ModuleNotFoundError:
#     print("Такого модуля нет!")

# def filter_comment(comment: str, banlist=[]) -> None:
#     new_comment = comment.split(" ")
#     for i in new_comment:
#         if i in banlist:
#             raise ValueError("Ваш комментарий отправлен на перепроверку, так как, возможно, содержит неблагоприятный контекст")

# def collect_all_possibles(list_, num):
#     possible_results = []

#     for item in list_:
       
#         if isinstance(item, (int, float)):
#             add_result = num + item
#             subtract_result = item - num
#             multiply_result = num * item
#             divide_result = item // num if item != 0 else None  # 
#             exponent_result = num ** item
#             possible_results.extend([add_result, subtract_result, multiply_result, divide_result, exponent_result])
#         elif isinstance(item, str):
           
#             string_result = item * num
#             possible_results.append(string_result)
#         elif isinstance(item, list):
            
#             list_result = item * num
#             possible_results.append(list_result)

#     return possible_results

# # Пример использования функции
# list_ = [
#     'hello',
#     6, 
#     [1, 2, 3]
# ]
# num = 2
# result = collect_all_possibles(list_, num)
# print(result)

def filter_comment(comment: str, banlist=[]) -> None:
    comment = comment.lower().split(" ")

    for i in comment:
        for j in i:
            if j in "!?,.":
                j = j.remove()
        print(i)
                
    
    for word in comment:
        if word in banlist:
            raise ValueError("Ваш комментарий отправлен на перепроверку, так как, возможно, содержит неблагоприятный контекст")
print(filter_comment('Hello, world', ['hello']))

    
    
        