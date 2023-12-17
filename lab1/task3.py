num1 = float(input("Введіть перше число: "))
operator = input("Введіть оператор (+, -, *, /): ")
num2 = float(input("Введіть друге число: "))

while True:
    if operator in ('+', '-', '*', '/'):
        break
    else:
        print("Помилка: невірний оператор")
        break

if operator == "+":
    result = num1 + num2
elif operator == "-":
    result = num1 - num2
elif operator == "*":
    result = num1 * num2
elif operator == "/":
    if num2 > 0:
        result = num1 / num2
else:
    result = "Помилка"

print(f"Результат: {result}")


