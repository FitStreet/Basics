# import re
# def filter_comment(comment: str, banlist=[]) -> None:
#     new_comment = re.sub(r"[!|?|.|,]", "", comment)
#     words = new_comment.lower().split(" ")
#     for word in words:
#             if word in banlist:
#                 raise ValueError("Ваш комментарий отправлен на перепроверку, так как, возможно, содержит неблагоприятный контекст")
            
                
    


# filter_comment('Dis? recipe. is i !!UNLike!?!! really much!', ['hate', 'unlike', 'liken\'t'])

# inp1 = input("Введите первое значение: ")
# inp2 = input("Введите второе значение: ")

# try:
#     inp1 = int(inp1)
# except ValueError:
#     pass 
# try:
#     inp2 = int(inp2)
# except ValueError:
#     pass  

# if isinstance(inp1, int) and isinstance(inp2, int):
  
#     result = inp1 + inp2
# else:
    
#     result = str(inp1) + str(inp2)

# print("Результат:", result)

# inp1 = input()
# inp2 = inp1.split(" ")
# list_ = []
# try:
#     for i in inp2:
#         if i.isdigit():
#             list_.append(int(i))
# except ValueError:
#     print('Данный элемент не является числом!')
# else:
#     print(list_)

# inp1 = input()
# inp2 = inp1.split(" ")
# list_ = []
# for i in inp2:
#     if i.isdigit():
#         list_.append(int(i))
#     elif i.isalpha():    
#          raise ValueError('Данный элемент не является числом!')


# lst = ['a',"b","c"]
# print(lst * 3)

# a = 1,2,3
# b = 1,2,3
# print(a+b)
# print(type(a+b))

# a1 = (1,2,3,4,3,3,3,3,3,3,3)
# print(a1)

# def fact(n):
#     res = 1
#     for i in range(1,n+1):
#         res *= i
#     return res

# print(fact(3))
# print(fact(5))

x = 2
def check():
    x = x*2
    print(x)

check()
#asdsafadgdsagfad
