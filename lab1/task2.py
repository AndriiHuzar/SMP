num1 = float(input("Введіть перше число: "))
operator = input("Введіть оператор (+, -, *, /): ")
num2 = float(input("Введіть друге число: "))

while True:
    if operator in ('+', '-', '*', '/'):
        break
    else:
        print("Помилка: невірний оператор")
        break

