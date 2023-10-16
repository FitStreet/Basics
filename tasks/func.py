# def func12(lst, reg):
#     lst1 = []
#     for i in lst:
#         if reg == "lower":
#             lst1.append(i.lower())
#         elif reg == "upper":
#             lst1.append(i.upper())
#     return lst1

# print(func12(["HeLLO", "world",], "upper"))

""""""
# def func13(string):
    
#     dict1 = {i:string.count(i) for i in string}
#     return dict1

# print(func13("hellllllo"))

""""""
# def add_(x,y):
#     return x+y
# def sub_(x,y):
#     return x-y
# def div_(x,y):
#     return x/y
# def mult_(x,y):
#     return x*y
# def calc(num1,num2,znak):
#     if znak == "+":
#         return add_(num1,num2)
#     elif znak == '-':
#         return sub_(num1,num2)
#     elif znak == '/':
#         return div_(num1,num2)
#     elif znak == '*':
#         return mult_(num1,num2)
    
# print(calc(5,5,"*"))

""""""
# users = [
#   { 'name': 'Jack', 'age': 35, 'work': 'IT-backend developer' },
#   { 'name': 'Helen', 'age': 35, 'work': 'Nurse' },
#   { 'name': 'Bob', 'age': 35, 'work': 'Driver' },
#   { 'name': 'Jessica', 'age': 35, 'work': 'IT-frontend developer' },
#   { 'name': 'Helga', 'age': 35, 'work': 'IT-HR' }
# ]

# def func15(slovar):
#     lst1 = []
#     for i in slovar:
#         for k in i:
#             if "IT" in i['work']:
#                 lst1.append(i.get('name'))
#     for i in set(lst1):
#         print(f"{i}, скидки в магазин компьютерной техники!")
# func15(user)

# def func15(users)
#     it_professionals = [user['name'] for user in users if 'IT' in user['work']]
    
#     if it_professionals:
#         for name in set(it_professionals):
#             print(f"{name}, скидки в магазин компьютерной техники!")
#     else:
#         print("Нет IT-профессионалов в списке.")
        

# def func16(km, l):
#     x = (l/km)*100
#     return f"На 100км было расходовано {x}л горючего"

# print(func16(1000, 100))

# list_ = [1,'a', 2, 'c', 3, 'd']
# def func18(lst):
#     lst_num = []
#     lst_str = []
#     for i in lst:
#         if type(i) == int:
#             lst_num.append(i)
#         elif type(i) == str:
#             lst_str.append(i)
#     return lst_num, lst_str

# print(func18(list_))

# students = [
#   {'student': 'Jack', 'marks': 43},
#   {'student': 'Tom', 'marks': 92}, 
#   {'student': 'Helen', 'marks': 85}, 
#   {'student': 'Peter', 'marks': 58},
#   {'student': 'Jessica', 'marks': 78}
# ]

# def func19(lst):
#     sorted_lst = sorted(lst, key = lambda x: x["marks"], reverse = True )
#     return sorted_lst

# print(func19(students))

# products = [
#   {
#     'title': 'Samsung S10', 
#     'price': 800, 
#     'count': 6, 
#     'category': 'samsung'},
#   {
#     'title': 'iPhone 13 Pro', 
#     'price': 1200, 
#     'count': 9, 
#     'category': 'apple'},
#   {
#     'title': 'Xiaomi Mi 10', 
#     'price': 500, 
#     'count': 2, 
#     'category': 'xiaomi'},
#   {
#     'title': 'Samsung S9', 
#     'price': 600, 
#     'count': 4, 
#     'category': 'samsung'},
#   {
#     'title': 'iPhone 11', 
#     'price': 850, 
#     'count': 1, 
#     'category': 'apple'}
# ]

# def func20(lst, string):
#     lst1 = [i for i in lst for k,v in i.items() if k == "title" and string.lower() in v.lower() ]
    # for i in lst:
    #     for k,v in i.items():
    #         if k == "title" and string.lower() in v.lower():
    #             lst1.append(i)
#     return lst1        

# print(func20(products,"i"))
            
# def func21(lst, string):
#     lst1 = [i for i in lst for k,v in i.items() if k == "category" and v == string ]
#     return lst1

# print(func21(products,"apple"))

# employees = [
#   {'name': 'Jack', 'salary': 10000, 'overTime': 4},
#   {'name': 'Tom', 'salary': 15000, 'overTime': 3},
#   {'name': 'Jessica', 'salary': 20000, 'overTime': 9},
#   {'name': 'Helen', 'salary': 25000, 'overTime': 2},
#   {'name': 'Peter', 'salary': 30000, 'overTime': 7}
# ]
# def func17(lst):
#     lst1 = []
#     for i in lst:
#            i["salary"]+=i["overTime"]*200
#            del i["overTime"]
#     return(lst)

# print(func17(employees))



# balance = 1000

# def spent(target,potracheno,current_balance):
#     rashodi = {}
#     if potracheno <= current_balance:
#         rashodi = {"target": target, "spend": potracheno}
#         current_balance -= potracheno
#         return rashodi, current_balance 
#     else:
#         return ("Недостаточно средств")
#     # return rashodi, current_balance

# def deposit(prihod, current_balance):
#     current_balance += prihod
#     return current_balance

# print(spent("sock", 100, balance))

database = []
def create(lst, title, price, category):
    lst.append({"title": title, "price": price, "category": category})
    return lst

def read(lst):
    print(lst)

def update(lst, index, title, price, category):
    lst[index] = {"title": title, "price": price, "category": category}
    return lst
def delete(lst,index):
    del lst[index]
    return lst


        
create([{'title': 'Coffee', 'price': 50, 'category': 'Grocery'}, {'title': 'title', 'price': 233, 'category': 'category'}])    
create(database, "silvia", 300, "cars")
read(database)
create(database, "s2000", 200, "cars" )
read(database)
create(database, "pip", 200, "list")
read(database)
update(database, 1, "mork", 300, "pork")
read(database)
delete(database, 0)
read(database)

database=list() 
def create(db:list,title:str,price:int,category:str)->list: 
    db.append({'title':title,'price':price,'category':category}) 
    return db 
def read(db:list)->list: 
    print(db) 
    return db 
def update(db:list,index:int,title:str,price:int,category:str)->list:
    db[index]['title']=title 
    db[index]['price']=price 
    db[index]['category']=category 
    return db 
def delete(db,index): 
    db.pop(index) 
    return db