# def foo():
#     var = 'переменная foo'
  
#     def bar():
#         var = 'переменная bar'
#         bar()
 
#     bar()
# foo()
# print('переменная в foo: ', var)

# x = "Я глобальная переменная!"
# def my_func():
#     global x
#     x = "Я могу изменяться"
# print(x)
# my_func() 
# print(x)   

# num = 3
# def mul():
#     global num
#     num**=2
# mul()
# mul()
# mul()
# print(num)

# balance = 0
# def get_salary(amount):
#     global balance
#     balance += amount

# def pay_bills(amount,log_name):
#     global balance
#     balance -= amount
#     print(f"Вы заплатили {amount} сом за {log_name}")

# def get_balance():
#     global balance
#     print(f"У вас на счету {balance} сом")

# get_salary(1000)
# get_balance()
# pay_bills(400, 'кабельное тв')
# get_balance()

# result = 0
# def pow_first(x,y):
#     global result
#     result = x ** y
# def pow_second(z):
#     global result
#     result %= z 

# pow_first(2, 3)
# pow_second(3)
# print(result)

# a = {'Мурат': 24, 'Эржан': 21, 'Чынгыз': 24, 'Алтынай': 17, 'Асема': 16}

# def age():
#     global a
#     for k,v in a.items():
#         if v >= 17:
#             print(f"{k}, Вы можете войти в клуб")
#         else:
#             print(f"{k}, извините, Вы не проходите по age-control") 
# age()

# a = ['pipi', 'papa', 'mama']
# b = []
# def title():
#     # global a
#     # global b
#     for i in a:
#         b.append(i.title())
#     return b

# print(title())
glas = "еаоэяиюёу"
znak = ""

def count_symbols(string):


