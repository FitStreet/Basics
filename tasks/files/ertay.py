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

# def calc_price(filename:str) -> int:
#     with open(filename,'r') as file:
#         list_ = [i.split() for i in file.readlines()]
#         total = 0
#         for i in list_:
#             total += float(i[1]) * float(i[2])
#         return total
        
    
# print(calc_price("prices.txt"))

"""Task 12"""
# def bad_students(filename: str):
#     with open(filename, 'r') as file:
#         data_list = [i.strip().split() for i in file.readlines()]
#         print(data_list)
#         bad_students = []
#         for i in data_list:
#             if int(i[-1]) < 4:
#                 bad_students.append(i[1])
#                 print(i)
#         return bad_students

# print(bad_students('students.txt')

"""Task 13"""

# def reverse_file_print(filename: str) -> None:
#     with open(filename, 'r') as file:
#         list_reversed = [i[::-1] for i in file.readlines()]
#         for i in list_reversed:
#             print(i)


# reverse_file_print('zen_of_python.txt')

"""Task 8"""
# import csv
# import time
# import datetime

# columns = ["№", "Секунда", "Микросекунда"]
# data_list = []
# for i in range(1,301):
#     current_time_seconds = time.strftime("%S")
#     current_time_mil_seconds = int(time.time() * 1000)
#     data_list.append([i, current_time_seconds, current_time_mil_seconds])
#     time.sleep(0.01)

# filename = 'rows_300.csv'
# with open(filename, 'w', newline= '') as file:
#     writer = csv.writer(file)

#     writer.writerow(columns)
#     writer.writerows(data_list)

"""filename = 'rows_300.csv' 
with open(filename, 'w', newline='') as file: 
    writer = csv.writer(file) 
    for i in range(1, 301): 
        now = datetime.datetime.now() 
        second = now.second 
        microsecond = now.microsecond 
        writer.writerow([i, second, microsecond]) 
        time.sleep(0.01)
"""

"""Task 10"""
import csv

def  read_csv(filename: str):
    with open(filename, 'r', newline = '') as file:
        data_dict = {}
        reader = csv.reader(file)
        for i in reader:
            key = i[0]
            values = i[1:]
            data_dict[key] = values
    return data_dict

print(read_csv('data.csv'))