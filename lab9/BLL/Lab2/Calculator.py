import decimal
from decimal import Decimal


from decimal import Decimal


class Calculator:
    """
    The Calculator class performs arithmetic operations on two numbers.
    """

    def __init__(self):
        """
        Initializes a Calculator object with two inputs and an operator.
        """
        self.first_input = Decimal(0)
        self.second_input = Decimal(0)
        self.operator = None

    def user_input(self):
        """
        Prompts the user for two numbers and an operator.
        """
        while True:
            try:
                first_input_str = input("Enter the first number: ")
                if first_input_str is None:
                    print("Invalid input. Please enter valid numbers.")
                    return
                self.first_input = Decimal(first_input_str)

                second_input_str = input("Enter the second number: ")
                if second_input_str is None:
                    print("Invalid input. Please enter valid numbers.")
                    return
                self.second_input = Decimal(second_input_str)
                self.operator = input("Enter operator (+, -, *, /, sqrt, ^, %): ")

                if self.operator not in ('+', '-', '*', '/', 'sqrt', '^', '%'):
                    print("Invalid operator. Please enter a valid operator (+, -, *, /, sqrt, ^, %).")
                else:
                    break

            except (ValueError, decimal.InvalidOperation):
                print("Invalid input. Please enter valid numbers.")

    def perform_calculation(self):
        """
        Performs the calculation based on the user's input.
        """
        self.user_input()
        result = self.start_calculation()
        if result is not None:
            print(f"Result: {result}")

    def start_calculation(self):
        """
        Determines the operation to perform based on the operator.
        """
        if self.check_input():
            return None
        if self.operator == '+':
            return self.add()
        elif self.operator == '-':
            return self.subtract()
        elif self.operator == '*':
            return self.multiply()
        elif self.operator == '/':
            return self.divide()
        elif self.operator == 'sqrt':
            return self.square_root()
        elif self.operator == '^':
            return self.power()
        elif self.operator == '%':
            return self.leftover()
        else:
            return "Invalid operator"

    def check_input(self):
        """
        Checks if the inputs are valid.
        """
        if self.first_input is None or self.second_input is None:
            print("Empty input")
            return True
        if (self.first_input == 0 or self.second_input == 0) and self.operator == '/':
            print("Can't divide by zero")
            return True

    def add(self):
        """
        Adds the two numbers.
        """
        result = self.first_input + self.second_input
        return result

    def subtract(self):
        """
        Subtracts the second number from the first.
        """
        result = self.first_input - self.second_input
        return result

    def divide(self):
        """
        Divides the first number by the second.
        """
        if self.first_input == 0 and self.second_input == 0:
            raise ZeroDivisionError("Can't divide zero by zero")
        elif self.second_input == 0:
            raise ZeroDivisionError("Can't divide by zero")
        result = self.first_input / self.second_input
        return result

    def multiply(self):
        """
        Multiplies the two numbers.
        """
        result = self.first_input * self.second_input
        return result

    def square_root(self):
        """
        Calculates the square root of the first number.
        """
        if self.first_input < 0:
            print("Can't calculate square root of a negative number")
            return None
        result = self.first_input.sqrt()
        return result

    def power(self):
        """
        Raises the first number to the power of the second number.
        """
        if self.first_input < 0 and self.second_input % 1 != 0:
            print("Can't calculate the root of a negative number")
            return None
        result = self.first_input ** self.second_input
        return result

    def leftover(self):
        """
        Calculates the remainder of the first number divided by the second.
        """
        if self.second_input == 0:
            print("Can't calculate remainder with a divisor of zero")
            return None
        result = self.first_input % self.second_input
        return result

