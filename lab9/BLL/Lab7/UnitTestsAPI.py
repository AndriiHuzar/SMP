import unittest
from unittest.mock import patch, Mock

from BLL.Lab7.APIClient import APIClient
from BLL.Lab7.InputParser import InputParser
from Shared.Libraries.validator_lib.Validator import Validator


class UnitTestsAPI(unittest.TestCase):
    """
    The UnitTestsAPI class contains unit tests for the API client, input parser, and validator.
    """

    def setUp(self):
        """
        This method is called before each test. It sets up the API client, input parser, and validator for testing.
        """
        self.api_client = APIClient('https://jsonplaceholder.typicode.com/posts/1')
        self.input_parser = InputParser()
        self.validator = Validator(self.input_parser)

    @patch('requests.get')
    def test_get_data(self, mock_get):
        """
        This test checks if the API client correctly gets data from the API.
        """
        mock_response = Mock()
        expected_dict = {"title": "foo", "body": "bar", "userId": 1}
        mock_response.json.return_value = expected_dict
        mock_get.return_value = mock_response
        self.assertEqual(self.api_client.get_data(), expected_dict)

    def test_validate_phone(self):
        """
        This test checks if the validator correctly validates phone numbers.
        """
        self.assertTrue(self.validator.validate_phone('+380631234567'))
        self.assertFalse(self.validator.validate_phone('1234567'))

    def test_validate_email(self):
        """
        This test checks if the validator correctly validates email addresses.
        """
        self.assertTrue(self.validator.validate_email('test@example.com'))
        self.assertFalse(self.validator.validate_email('testexample.com'))

    def test_validate_credit_card(self):
        """
        This test checks if the validator correctly validates credit card numbers.
        """
        self.assertTrue(self.validator.validate_credit_card('1234-5678-9012-3456'))
        self.assertFalse(self.validator.validate_credit_card('1234-5678-9012'))

    def test_validate_date(self):
        """
        This test checks if the validator correctly validates dates.
        """
        self.assertTrue(self.validator.validate_date('31/12/2023'))
        self.assertFalse(self.validator.validate_date('31/13/2023'))

    def test_parse_user_input(self):
        """
        This test checks if the input parser correctly parses user input.
        """
        dates, phones, emails, credit_cards = self.input_parser.parse_user_input('31/12/2023, +380631234567, '
                                                                                 'test@example.com, '
                                                                                 '1234-5678-9012-3456')
        self.assertEqual(dates, ['31/12/2023'])
        self.assertEqual(phones, ['+380631234567'])
        self.assertEqual(emails, ['test@example.com'])
        self.assertEqual(credit_cards, ['1234-5678-9012-3456'])


if __name__ == '__main__':
    unittest.main()
