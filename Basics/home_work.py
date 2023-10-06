


# is | ==  "==" Возвращает True если сравниваемые объекты имеют одинаковые значения.
# оператор "is" возвращает True если сравниваемые объекты помимо того, что имеют одинаковые значения, еще и ссылабтся на одну и туже область памяти.
# Таким образом, is отличается от == в Python, дополнительной проверкой на идентичность адресов в памяти, на которые ссылаются переменные.
# Если сравнивать переменные от -5 до 256, вывод у == и у is будет одинаковый(под числа от -5 до 256 в Python отводится отдельная область памяти
# и любая переменная со значением из указанного диапозона будет ссылатся на эту заранее выделенную область в памяти)



print("---------------------------------------------------------------------")
print("---Для сравнения ведите 2 строки с одинаковым количеством символов---")
print("---------------------------------------------------------------------")
str1 = input('Первая строка: ')
str2 = input('Вторая строка: ')
print("---------------------------------------------------------------------")

if len(str1) != len(str2):
    print("Вы ввели разные по длине строки")
elif len(str1) == len(str2):
    for i in range(len(str1)):
        print(f"{str1[i]} = {ord(str1[i])} -- {str2[i]} = {ord(str2[i])}")
    if str1 > str2:
        print(f"{str1} > {str2}")
    elif str1 < str2:
        print(f"{str1} < {str2}")
    elif str1 == str2:
        print(f"{str1} == {str2}")
    # elif str1 != str2:
    #     print(f"{str1} != {str2}")
    


