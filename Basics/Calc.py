"==================Calculator===================="
num1 = int(input("Введите первое число: "))
num2 = int(input("Введите второе число: "))
znak = input("Введите знак(+ - * / % ** // ): ")
znaki = ['+', '-',  '*', '/', '%', '**', '//']
zapret_znaki = ['/', '%', '//']
if znak not in znaki:
    print('Данной операции нет в системе')
elif num2 == 0 and znak in zapret_znaki:
    print('На ноль делить нельзя!')
elif znak == "+":
    print(f"Ответ: {num1 + num2}")
elif znak == "-":
    print(f"Ответ: {num1 - num2}")
elif znak == "*":
    print(f"Ответ: {num1 * num2}")
elif znak == "/":
    print(f"Ответ: {num1 / num2}")
elif znak == "%":
    print(f"Ответ: {num1 % num2}")
elif znak == "**":
    print(f"Ответ: {num1 ** num2}")
elif znak == "//":
    print(f"Ответ: {num1 // num2}")

