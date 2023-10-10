"======================Циклы==================="
# цикл - блок кода, который отрабатывает несколько раз
# for - цикл, который работает с итерируемыми объектами, цикл заканчивает работу после перебора всех значенийитнрируемого объекта
# while - цикл, который работает до тех пор, пока условие верно(True)

# while True:
#     print("hello") 
    # будет работать бесконечно

# while input("Хотите продолжить(y/n)") == "y":
#     num1, num2 = int(input("Введи первое число: ")), int(input("Введи второе число: "))
#     operation = input("Выбери операцию +, *, /, -: ")
#     if operation == "+":
#         print(num1+num2)
#     elif operation == "-":
#         print(num1-num2)
#     elif operation == "*":
#         print(num1*num2)
#     elif operation == "/":
#         print(num1/num2)
#     else:
#         print("Такой операции нет!!!")

# play = True
# while play:
#     num1, num2 = int(input("Введи первое число: ")), int(input("Введи второе число: "))
#     operation = input("Выбери операцию +, *, /, -: ")
#     if operation == "+":
#         print(num1+num2)
#     elif operation == "-":
#         print(num1-num2)
#     elif operation == "*":
#         print(num1*num2)
#     elif operation == "/":
#         print(num1/num2)
#     else:
#         print("Такой операции нет!!!")
#     one_time = input("Хотите продлжть? yes/no:  ")
#     if one_time.lower == 'yes':
#         play = True
#     elif one_time.lower == 'no':
#         play = False
#         print("Еще увидимся!")
#     else:
#         print("Попробуй еще")

"=======================break, continue==================="
#breake - прерывает на цикл
#continue - пропускает итерацию (пропускает один цикл)


# string = "hello world"
# for i in string:
#     if i != "o":
#         continue
#     else:
#         print(i *2)

# nums =list(range(1,101))
# nums2 = []
# for i in nums:
#     if i % 2 == 0:
#         continue
#     nums2.append(str(i)+ f"{i}")
# print(nums2)


mary = [
    {
        'name': 'Nikita',
        'password': '12324567'
    },
    {
        'name': 'Ivan',
        'password' :'563'
    },
    {
        'name': 'Jalyn',
        'password' :'115'
    },
    {
        'name': 'Amir',
        'password' :'100'
    },
    {
        'name': 'Bilal',
        'password' :'008'
    },
    {
        'name': 'Abdugadi',
        'password' :'777'
    },
    {
        'name': 'Aitenir',
        'password' :'007'
    },
    {
        'name': 'Ramazan',
        'password' :'sweeden_967'
    },
    {
        'name': 'Almaz',
        'password' :'1'
    },
    {
        'name': 'Adilet'
    },
    {
        'name': 'Erlan',
        'password' :'555'
    },
    {
        'name': 'Sagida',
        'password' :'67830'
    },
     {
        'name': 'Ertay',
        'password' :'net_parolya'
    }
    ]
play = True
while play:
    name = input("Введите свое имя:  ")
    password = input('Введите свой пароль: ')

    user_found = False
    for human in mary:
        if human.get('name').lower() == name.lower() and password == human.get("password"):
                print("успешно залогинились")
                user_found = True
                break
            
    if not user_found:
        print("Пользователь не найден или пароль не верный")
        
        
        
        one_time = input("Хотите продлжть? yes/no:  ")
        if one_time.lower == 'yes':
            play = True
        elif one_time.lower == 'no':
            play = False
            print("Еще увидимся!")
        else:
            print("Попробуй еще")
        