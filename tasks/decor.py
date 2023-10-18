# def call_function(func):
#     def wrapper():
#         print(f"Вызываю функцию {func.__name__}")
#         func()
#         print(f"Вызов функции {func.__name__} прошёл успешно")
#     return wrapper
# @call_function
# def first():
#     print("Hello world!")
#     return "Hello world!"

# first()

# result = call_function(first)
# result()

def func_start_time(func):
    def wrapper():
        import datetime
        current_datetime = datetime.datetime.now()
        formatted_datetime = current_datetime.strftime('%Y-%m-%d %H:%M')
        print(f"Функция запущени {formatted_datetime}")
        func()
    return wrapper

@func_start_time
def func():
    print('Hello world')

func()
