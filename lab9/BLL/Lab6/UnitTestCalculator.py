import unittest
from decimal import Decimal
from unittest.mock import patch

from BLL.Lab2.Calculator import Calculator


class UnitTestsCalculator(unittest.TestCase):
    """
    The UnitTestsCalculator class contains unit tests for the Calculator class.
    """

    def setUp(self):
        """
        This method is called before each test. It sets up the Calculator object for testing.
        """
        self.calculator = Calculator()

    def test_add(self):
        """
        This test checks if the addition operation works correctly.
        """
        self.calculator.first_input = Decimal(5)
        self.calculator.second_input = Decimal(3)
        self.calculator.operator = '+'
        self.assertEqual(self.calculator.start_calculation(), Decimal(8))

    def test_subtract(self):
        """
        This test checks if the subtraction operation works correctly.
        """
        self.calculator.first_input = Decimal(5)
        self.calculator.second_input = Decimal(3)
        self.calculator.operator = '-'
        self.assertEqual(self.calculator.start_calculation(), Decimal(2))

    def test_multiply(self):
        """
        This test checks if the multiplication operation works correctly.
        """
        self.calculator.first_input = Decimal(5)
        self.calculator.second_input = Decimal(3)
        self.calculator.operator = '*'
        self.assertEqual(self.calculator.start_calculation(), Decimal(15))

    def test_divide(self):
        """
        This test checks if the division operation works correctly.
        """
        self.calculator.first_input = Decimal(6)
        self.calculator.second_input = Decimal(3)
        self.calculator.operator = '/'
        self.assertEqual(self.calculator.start_calculation(), Decimal(2))

    def test_square_root(self):
        """
        This test checks if the square root operation works correctly.
        """
        self.calculator.first_input = Decimal(9)
        self.calculator.second_input = Decimal(0)
        self.calculator.operator = 'sqrt'
        self.assertEqual(self.calculator.start_calculation(), Decimal(3))

    def test_power(self):
        """
        This test checks if the power operation works correctly.
        """
        self.calculator.first_input = Decimal(-2)
        self.calculator.second_input = Decimal(3)
        self.calculator.operator = '^'
        self.assertEqual(self.calculator.start_calculation(), Decimal(-8))

    def test_leftover(self):
        """
        This test checks if the modulo operation works correctly.
        """
        self.calculator.first_input = Decimal(10)
        self.calculator.second_input = Decimal(3)
        self.calculator.operator = '%'
        self.assertEqual(self.calculator.start_calculation(), Decimal(1))

    def test_divide_by_zero(self):
        """
        This test checks if the Calculator correctly handles division by zero.
        """
        self.calculator.first_input = Decimal(5)
        self.calculator.second_input = Decimal(0)
        self.calculator.operator = '/'
        self.assertIsNone(self.calculator.start_calculation())

    def test_square_root_of_negative(self):
        """
        This test checks if the Calculator correctly handles square root of a negative number.
        """
        self.calculator.first_input = Decimal(-9)
        self.calculator.second_input = Decimal(0)
        self.calculator.operator = 'sqrt'
        self.assertIsNone(self.calculator.start_calculation())

    def test_leftover_by_zero(self):
        """
        This test checks if the Calculator correctly handles modulo by zero.
        """
        self.calculator.first_input = Decimal(10)
        self.calculator.second_input = Decimal(0)
        self.calculator.operator = '%'
        self.assertIsNone(self.calculator.start_calculation())

    def test_invalid_operator(self):
        """
        This test checks if the Calculator correctly handles an invalid operator.
        """
        self.calculator.first_input = Decimal(5)
        self.calculator.second_input = Decimal(3)
        self.calculator.operator = 'invalid'
        self.assertEqual(self.calculator.start_calculation(), "Invalid operator")

    def test_empty_input(self):
        """
        This test checks if the Calculator correctly handles empty input.
        """
        with patch('builtins.input', side_effect=[None, '3', '+']):
            self.assertIsNone(self.calculator.perform_calculation())

        with patch('builtins.input', side_effect=['3', None, '+']):
            self.assertIsNone(self.calculator.perform_calculation())

    def test_zero_division(self):
        """
        This test checks if the Calculator correctly handles division of zero by zero.
        """
        self.calculator.first_input = Decimal(0)
        self.calculator.second_input = Decimal(0)
        self.calculator.operator = '/'
        with self.assertRaises(ZeroDivisionError):
            self.calculator.divide()

    def test_negative_power(self):
        """
        This test checks if the Calculator correctly handles raising a negative number to a fractional power.
        """
        self.calculator.first_input = Decimal(-2)
        self.calculator.second_input = Decimal(0.5)
        self.calculator.operator = '^'
        self.assertIsNone(self.calculator.start_calculation())

