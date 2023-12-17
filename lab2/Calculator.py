import math
#Task 1: Creating a class.

class Calculator:
    # Task 2: Calculator Initialization
    def __init__(self):
        self.result = None

    # Task 3: User Input
    def get_user_input(self):
        try:
            # Task 8: Decimal Numbers (float)
            self.num1 = float(input("Enter the first number: "))
            # Task 9: Additional Operations
            self.operator = input("Enter an operator (+, -, *, /, sqrt, ^, %): ")
        except ValueError:
            print("Error: Input must be a number.")
            return False
        return True

    # Task 4: Operator Validation
    def is_valid_operator(self):
        valid_operators = ('+', '-', '*', '/', 'sqrt', '^', '%')
        if self.operator in valid_operators:
            return True
        else:
            print("Error: Entered operator is invalid. Valid operators are: +, -, *, /, sqrt, ^, %.")
            return False

    # Task 5: Calculation
    def calculate(self):
        if self.is_valid_operator():
            if self.operator == '+':
                self.num2 = float(input("Enter the second number: "))
                self.result = self.num1 + self.num2
            elif self.operator == '-':
                self.num2 = float(input("Enter the second number: "))
                self.result = self.num1 - self.num2
            elif self.operator == '*':
                self.num2 = float(input("Enter the second number: "))
                self.result = self.num1 * self.num2
            elif self.operator == '/':
                self.num2 = float(input("Enter the second number: "))
                # Task 6.1: Error Handling
                if self.num2 == 0:
                    print("Error: Division by zero is not possible.")
                else:
                    self.result = self.num1 / self.num2
            elif self.operator == '^':
                self.num2 = float(input("Enter the exponent: "))
                self.result = self.num1 ** self.num2
            elif self.operator == 'sqrt':
                # Task 6.2: Error Handling
                if self.num1 < 0:
                    print("Error: Square root of a negative number is not possible.")
                else:
                    self.result = math.sqrt(self.num1)
            elif self.operator == '%':
                self.num2 = float(input("Enter the percentage number: "))
                self.result = (self.num1 * self.num2) / 100
            return True
        return False

    # Task 7: Repeating Calculations
    # Task 10: User-Friendly Interface
    def run_calculator(self):
        print("Perform calculations!")
        while True:
            if self.get_user_input():
                if self.calculate():
                    print("Result: {:.2f}".format(self.result))
            another_calculation = input("Perform another operation? (Yes/No): ")
            if another_calculation.lower() != "yes":
                print("Goodbye!")
                break

calc = Calculator()
calc.run_calculator()
