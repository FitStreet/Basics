"""Task 1"""
# list_ = [1, 2, 3, 4]  
# import functools
# result = functools.reduce(lambda x,y: x+y,list_)
# print(result)
"""Task 2"""
# list_ = [5,5,5] 
# result = all(i > 3 for i in list_)
# print(result)
"""Task 3"""
# list_ = [5, 8, 4, 6, 7]
# result = any(i < 0 for i in list_)
# print(result)
"""Task 4"""
# list_ = [1, 2, 3, 4]  
# result = list(map(lambda x: x ** 2, list_))
# print(result)
"""Task 5"""
# list_ = [1, 2, 3, 4] 
# result = list(filter(lambda x: x % 2 ==0, list_))
# print(result)
"""Task 6"""
# list_ = ['inheritance', 'solid', 'polymorphism', 'dry', 'yagni',] 
# result = list(filter(lambda x: len(x) > 7, list_ ))
# print(result)
"""Task 7"""
# list_ = [5, 6, 7, 8] 
# import functools
# result = functools.reduce(lambda x,y: x*y,list_)
# print(result)
"""Task 9"""
# list_ = [-1, 2, 3, 5, -3, 7] 
# result = list(map(lambda x: x > 0, list_))
# print(result)
"""Task 10"""
# from functools import reduce 
# list_ = ['Paul', 'George', 'Ringo', 'John'] 
# result = reduce(lambda x, y: x if len(x) > len(y) else y, list_)
# print(result)
"""Task 11"""
# list_ = list(range(1,51))
# result = list(map(lambda x: "Fizz" if x % 3 == 0 else "Buzz",list_))
# print(result)
"""Task 12"""
# list_ = [1,2,3]
# result = min(list_)
# print(result)
"""13"""
# from functools import reduce 
# list_ = [1,2,3] 
# result = reduce(lambda x, y: x if x < y else y, list_)
# print(result)
"""14"""
# string = "makersbootcamp"
# result = tuple(enumerate(string))
# print(result)
"""15"""
# list_ = [-7, -2, 12, 32, 432, 23, 37, 11, 76, 0, -23, 45, -32, -56]
# print(list(abs(i) for i in list_))
"""16"""
list_ = ['hello', 123]
result = list(map(lambda x: type(x), list_))
print(result)