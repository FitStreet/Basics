"======================Декораторы===================="
# Декоратор - функция высшего порядка, которая нужна чтобы расширять функционал функций не изменяя ее (функция обертка) 
# DRY !!!

# def decorator(func):
#     def wrapper(*args, **kwargs):
#         import time
#         start = time.time()
#         func()
#         end = time.time()
#         print(f'{func.__name__} отработала за {end-start}')
#     return wrapper

# @decorator
# def func():
#     a = []
#     for i in range(1,1000000):
#         a.append(i)
#     return a
# func()


# def func2():
#     a = [i for i in range(1,1000000)]
#     return a
# func2()

# result = decorator(func2)
# result()


# 1. decorator
# 2. wrapper
# 3. function

# def get_info(name, last_name, age):
#     return f"Ваше имя {name}, ваша фамилия {last_name}, ваш возраст {age}"

# def god_rozhdenia(func):
#     def wrapper(*args, **kwargs):
#         print(f"{get_info(*args)}. Вы родились в {2023 - args[-1]} ")
#     return wrapper

# result = god_rozhdenia(get_info)
# result("John", "Snow", 72)


# def get_sandwitch(x):
#     # print(x)
#     return x

# def add_bread(func):
#     def wrapper_bread(*args):

#         return f"хлеб {func(*args)} хлеб"
#     return wrapper_bread

# def add_ingredients(func):
#     def wrapper_ingredients(*args):

#         return f"помидор {func(*args)} салат"
#     return wrapper_ingredients

# # @add_bread
# # @add_ingredients
# def get_sandwitch(x):
#     # print(x)
    # return x

# print(get_sandwitch("сосиска"))

# 1. ingredients - wrapper_ingredients
# 2. bread(wrapper_ingredients) - wrapper bread
# 3. result(сосика)
# 3. wrapper_bread(wrapper_ingredients)
# 4. wrapper_ingredients(get_sandwich)
# 5.    

# result = add_bread(add_ingredients(get_sandwitch))
# print(result("сосиска"))

# "хлеб помидор сосиска салат хлеб"



 