import math


class BasicCalculator:
    """
    The BasicCalculator class performs basic mathematical operations.
    """

    def __init__(self):
        """
        Initializes a BasicCalculator object.
        """
        self.memory = None
        self.history = []
        self.decimal_places = 2
        self.operations = {
            '+': self.summ,
            '-': self.subtraction,
            '*': self.multiplication,
            '/': self.division,
            '^': self.power,
            'sqrt': self.square,
            '%': self.remains
        }

    def summ(self, x, y):
        """
        Returns the sum of x and y.
        """
        return x + y

    def subtraction(self, x, y):
        """
        Returns the result of subtracting y from x.
        """
        return x - y

    def multiplication(self, x, y):
        """
        Returns the result of multiplying x by y.
        """
        return x * y

    def division(self, x, y):
        """
        Returns the result of dividing x by y. Returns an error if y equals 0.
        """
        if y == 0:
            return "Error. Division by 0 unreal"
        return x / y

    def power(self, x, y):
        """
        Returns the result of raising x to the power of y.
        """
        return pow(x, y)

    def remains(self, x, y):
        """
        Returns the remainder of dividing x by y.
        """
        return x % y

    def square(self, x):
        """
        Returns the square root of x. Returns an error if x is a negative number.
        """
        if x < 0:
            return "The square root of a negative number is impossible"
        return math.sqrt(x)
