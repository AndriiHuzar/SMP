import math

while True:
    num1 = float(input("Введіть перше число: "))
    operator = input("Введіть оператор (+, -, *, /, ^, sqrt, %): ")

    while True:
        if operator in ('+', '-', '*', '/', 'sqrt', '^', '%'):
            break
        else:
            print("Помилка: невірний оператор")
            operator = input("Введіть оператор (+, -, *, /, ^, sqrt, %): ")

    if operator == "+":
        num2 = float(input("Введіть друге число: "))
        result = num1 + num2
    elif operator == "-":
        num2 = float(input("Введіть друге число: "))
        result = num1 - num2
    elif operator == "*":
        num2 = float(input("Введіть друге число: "))
        result = num1 * num2
    elif operator == "/":
        num2 = float(input("Введіть друге число: "))
        if num2 != 0:
            result = num1 / num2
        else:
            result = "Помилка: ділення на нуль"
    elif operator == "^":
        num2 = float(input("Введіть степінь: "))
        result = num1 ** num2
    elif operator == "sqrt":
        if num1 >= 0:
            result = math.sqrt(num1)
        else:
            result = "Помилка: корінь з від'ємного числа"
    elif operator == "%":
        num2 = float(input("Введіть число, на яке потрібно поділити: "))
        if num2 != 0:
            result = num1 % num2
    else:
        result = "Помилка"

    print(f"Результат: {result}")

    newcalc = input("Продовжити? (+/-): ")
    # .lower() конвертує текст в нижній регістр
    if newcalc.lower() != '+':
        break
