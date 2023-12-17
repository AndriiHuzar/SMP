import unittest
from unittest.mock import patch, MagicMock
from io import StringIO

from ConsoleInterface import choose_display_format
from DisplayDogAPI import DisplayDogApi

class TestDisplayDogApi(unittest.TestCase):
    @patch('requests.get')
    def test_get_all_breeds(self, mock_requests_get):
        # Create a mock response with sample data
        mock_response = MagicMock()
        mock_response.json.return_value = {"message": {"breed1": {}, "breed2": {}}}
        # Set the mock response for the requests.get method
        mock_requests_get.return_value = mock_response

        # Call the method under test
        breeds = DisplayDogApi.get_all_breeds()

        # Assert that the method returns the expected list of breeds
        self.assertEqual(list(breeds), ["breed1", "breed2"])

class TestConsoleInterface(unittest.TestCase):
    @patch('builtins.input', side_effect=['3'])
    def test_invalid_display_format(self, mock_input):
        # Test that an invalid display format input raises a ValueError or StopIteration
        with self.assertRaises((ValueError, StopIteration)):
            choose_display_format()

if __name__ == '__main__':
    # Run the test cases if the script is executed as the main module
    unittest.main()
