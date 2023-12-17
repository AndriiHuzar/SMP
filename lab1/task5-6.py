while True:
    num1 = float(input("Введіть перше число: "))
    operator = input("Введіть оператор (+, -, *, /): ")
    num2 = float(input("Введіть друге число: "))

    while True:
        if operator in ('+', '-', '*', '/'):
            break
        else:
            print("Помилка: невірний оператор")
            operator = input("Введіть оператор (+, -, *, /): ")

    if operator == "+":
        result = num1 + num2
    elif operator == "-":
        result = num1 - num2
    elif operator == "*":
        result = num1 * num2
    elif operator == "/":
        if num2 != 0:
            result = num1 / num2
        else:
            result = "Помилка: ділення на нуль"
    else:
        result = "Помилка"

    print(f"Результат: {result}")

    newcalc = input("Продовжити? (+/-): ")
    # .lower() конвертує текст в нижній регістр
    if newcalc.lower() != '+':
        break
