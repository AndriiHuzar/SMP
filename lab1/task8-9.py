import math

memory = None  # Змінна для зберігання значення в пам'яті
history = []  # Список для зберігання історії
num2 = None

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
    else:
        result = "Помилка"

    # Додамо обчислення до історії
    if num2 is not None:
        history.append(f"{num1} {operator} {num2} = {result}")
    else:
        history.append(f"{num1} {operator} = {result}")

    print(f"Результат: {result}")

    newcalc = input("Продовжити: '+' (save/memory/clear/history/exit) Введіть операцію:")
    if newcalc.lower() != '+':
        if newcalc.lower() == 'save':
            memory = result
            print(f"Збережено в пам'яті: {memory}")
        elif newcalc.lower() == 'memory':
            if memory is not None:
                result = memory
                print(f"Зчитано з пам'яті: {result}")
            else:
                print("Пам'ять порожня")
        elif newcalc.lower() == 'clear':
            memory = None
            print("Пам'ять очищено")
        elif newcalc.lower() == 'history':
            print("Історія обчислень:")
            for entry in history:
                print(entry)
        elif newcalc.lower() == 'exit':
            break
        else:
            continue 

