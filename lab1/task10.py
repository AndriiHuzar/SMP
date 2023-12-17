import math

memory = None  # Зберігання в пам'яті
history = []  # Список для зберігання історії
num2 = None
decimal = 2

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
            result = "Помилка: ділення на нуль"
    elif operator == "settings":
        print("Налаштування:")
        print(f"1. Кількість десяткових розрядів (зараз {decimal}):")
        print(f"2. Зберігання результату в пам'яті (зараз {'Включено' if memory is not None else 'Виключено'}):")
        setting_choice = input("Виберіть опцію (1/2): ")
        if setting_choice == "1":
            decimal = int(input("Введіть нову кількість десяткових розрядів: "))
        elif setting_choice == "2":
            if memory is not None:
                memory = None
                print("Зберігання результату в пам'яті вимкнено.")
            else:
                memory = result
                print(f"Збережено результат в пам'яті: {memory}")
        else:
            print("Невірний вибір налаштувань.")
        continue
    else:
        result = "Помилка"

    if isinstance(result, float):
        result = round(result, decimal)
    #Додавання до історії
    if num2 is not None:
        history.append(f"{num1} {operator} {num2} = {result}")
    else:
        history.append(f"{num1} {operator} = {result}")

    print(f"Результат: {result}")

    newcalc = input("Продовжити: '+' (settings/history/exit) Введіть операцію:")
    if newcalc.lower() != '+':
        if newcalc.lower() == 'settings':
            print("Налаштування:")
            print(f"1. Кількість десяткових розрядів (зараз {decimal}):")
            print(f"2. Зберігання результату в пам'яті (зараз {'Включено' if memory is not None else 'Виключено'}):")
            setting_choice = input("Виберіть опцію (1/2): ")
            if setting_choice == "1":
                decimal = int(input("Введіть нову кількість десяткових розрядів: "))
            elif setting_choice == "2":
                if memory is not None:
                    memory = None
                    print("Зберігання результату в пам'яті вимкнено.")
                else:
                    memory = result
                    print(f"Збережено результат в пам'яті: {memory}")
            else:
                print("Невірний вибір налаштувань.")
        elif newcalc.lower() == 'history':
            print("Історія обчислень:")
            for entry in history:
                print(entry)
        elif newcalc.lower() == 'exit':
            break
