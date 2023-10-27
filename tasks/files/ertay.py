# with open("task4.txt", 'r') as file:
#     print(len(file.readlines()))

# with open('task5.txt', 'r') as file:
#     list1 = list(map(int,file.readlines()))
#     minimal = min(list1)
#     maximum = max(list1)

# with open('task6.txt', 'x') as new_file:
#     new_file.write(f'{minimal}-{maximum}')

"""Task 6"""
# def read_last(lines: int, filename: str):
#     with open(filename, 'r') as file:
#         list1 = file.readlines()[::-1]
#         list1 = [i.replace("\n", "") for i in list1]
#         if lines > len(list1):
#             for i in list1:
#                 print(i)
#         else:
#             for i in range(lines):
#                 print(list1[i])

# read_last(5, "article.txt")

"""Task 7"""
# def longest_words(filename: str): # эта версия кода работает кода е одной строчке по одному слову
#     with open(filename, 'r') as file:
#         longest = []
#         list_words = [i.replace("\n", "") for i in file.readlines()]
#         # print(list_words)
#         len_max = max(len(i) for i in list_words)
#         for i in list_words:
#             if len(i) == len_max and not i in longest:
#                 longest.append(i)
#         print(" ".join(longest))


# longest_words("article.txt")  

# def longest_words(filename: str): # работает когда в строке несколько слов 
#     with open(filename, 'r') as file:
#         longest = []
#         list_words2 =[]
#         list_words = [list_words2.extend(i.replace("\n", "").split()) for i in file.readlines()]
#         # print(list_words2)
#         len_max = max(len(i) for i in list_words2)
#         for i in list_words2:
#             if len(i) == len_max and not i in longest:
#                 longest.append(i)
#         print("".join(longest)) if len(longest) == 1 else print(longest)


# longest_words("article2.txt")

"""Task 8"""

