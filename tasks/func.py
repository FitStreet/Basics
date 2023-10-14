# def func12(lst, reg):
#     lst1 = []
#     for i in lst:
#         if reg == "lower":
#             lst1.append(i.lower())
#         elif reg == "upper":
#             lst1.append(i.upper())
#     return lst1

# print(func12(["HeLLO", "world",], "upper"))


# def func13(string):
    
#     dict1 = {i:string.count(i) for i in string}
#     return dict1

# print(func13("hellllllo"))
def add_(x,y):
    return x+y
def sub_(x,y):
    return x-y
def div_(x,y):
    return x/y
def mult_(x,y):
    return x*y
def calc(num1,num2,znak):
    if znak == "+":
        return add_(num1,num2)
    elif znak == '-':
        return sub_(num1,num2)
    elif znak == '/':
        return div_(num1,num2)
    elif znak == '*':
        return mult_(num1,num2)
    
print(calc(5,5,"*"))
