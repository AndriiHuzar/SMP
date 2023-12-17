import unittest
from Data.lab_2.BaseCalculator import BaseCalculator


class TestCalculator(unittest.TestCase):

    def setUp(self):
        # Initialize the calculator with some default values
        self.calculator = BaseCalculator(num_1=10, num_2=5, operator='+', custom_round=2)

    # Test getting num_1 property
    def test_get_num_1(self):
        result = self.calculator.num_1
        self.assertEqual(result, 10)

    # Test getting num_2 property
    def test_get_num_2(self):
        result = self.calculator.num_2
        self.assertEqual(result, 5)

    # Test getting operator property
    def test_get_operator(self):
        result = self.calculator.operator
        self.assertEqual(result, '+')

    # Test getting custom_round property
    def test_get_custom_round(self):
        result = self.calculator.custom_round
        self.assertEqual(result, 2)

    # Test valid number
    def test_valid_number(self):
        result = self.calculator._number_validate('10')
        self.assertEqual(result, 10.0)

    # Test invalid number
    def test_invalid_number(self):
        with self.assertRaises(ValueError) as context:
            self.calculator._number_validate('abc')
        self.assertEqual(str(context.exception),
                         "Parameter 'abc' is not number")

    # Test valid operator
    def test_valid_operator(self):
        result = self.calculator._operator_validate('+')
        self.assertEqual(result, '+')

    # Test invalid operator
    def test_invalid_operator(self):
        with self.assertRaises(TypeError) as context:
            self.calculator._operator_validate('$')

        self.assertEqual(str(context.exception),
                         "Operator is not in ('+', '-', '*', '/', '^', '√', '%')!")

    # Test addition
    def test_addition(self):
        self.calculator.operator = '+'
        self.calculator.calc()
        self.assertEqual(self.calculator._result, 15)

    # Test subtraction
    def test_subtraction(self):
        self.calculator.operator = '-'
        self.calculator.calc()
        self.assertEqual(self.calculator._result, 5)

    # Test multiplication
    def test_multiplication(self):
        self.calculator.operator = '*'
        self.calculator.calc()
        self.assertEqual(self.calculator._result, 50)

    # Test division with a non-zero divisor
    def test_division(self):
        self.calculator.operator = '/'
        self.calculator.calc()
        self.assertEqual(self.calculator._result, 2)

    # Test division by zero
    def test_division_by_zero(self):
        self.calculator.operator = '/'
        self.calculator.num_2 = 0
        with self.assertRaises(ZeroDivisionError):
            self.calculator.calc()

    # Test exponentiation
    def test_exponentiation(self):
        self.calculator.operator = '^'
        self.calculator.calc()
        self.assertEqual(self.calculator._result, 100000)

    # Test square root with a non-negative number
    def test_square_root(self):
        self.calculator.operator = '√'
        self.calculator.calc()
        self.assertEqual(self.calculator._result, 3.16)

    # Test square root with a negative number
    def test_square_root_negative(self):
        self.calculator.operator = '√'
        self.calculator.num_1 = -10
        with self.assertRaises(ArithmeticError):
            self.calculator.calc()

    # Test remainder
    def test_remainder(self):
        self.calculator.operator = '%'
        self.calculator.calc()
        self.assertEqual(self.calculator._result, 0)

    # Test remainder with division by zero
    def test_remainder_division_by_zero(self):
        self.calculator.operator = '%'
        self.calculator.num_2 = 0
        with self.assertRaises(ZeroDivisionError):
            self.calculator.calc()

