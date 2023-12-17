import re


class Validator:
    """
    A utility class for validating user input.
    """

    def __init__(self, input_parser):
        """
        Initializes the Validator with an input parser.

        Args:
            input_parser: The input parser to use for validation.
        """
        self.input_parser = input_parser

    def validate_input(self, prompt, choices):
        """
        Validates user input against predefined choices.

        Args:
            prompt (str): The prompt to display before reading input.
            choices (list): The list of valid choices.

        Returns:
            str: The user's input if it is valid.
        """
        while True:
            user_input = input(prompt)
            if choices:
                if user_input in choices:
                    return user_input
                else:
                    print("Invalid choice.")
            else:
                try:
                    return float(user_input)
                except ValueError:
                    print("Invalid input. Please enter a number.")

    def validate_date(self, date):
        """
        Validates a date string.

        Args:
            date (str): The date string to validate.

        Returns:
            bool: True if the date string is valid, False otherwise.
        """
        if not re.match(self.input_parser.date_pattern, date):
            print("Invalid date format. Please enter the date in the format DD/MM/YYYY.")
            return False
        return True

    def validate_phone(self, phone):
        """
        Validates a phone number string.

        Args:
            phone (str): The phone number string to validate.

        Returns:
            bool: True if the phone number string is valid, False otherwise.
        """
        if not re.match(self.input_parser.phone_pattern, phone):
            print("Invalid phone format. Please enter the phone in the correct format.")
            return False
        return True

    def validate_email(self, email):
        """
        Validates an email string.

        Args:
            email (str): The email string to validate.

        Returns:
            bool: True if the email string is valid, False otherwise.
        """
        if not re.match(self.input_parser.email_pattern, email):
            print("Invalid email format. Please enter the email in the correct format.")
            return False
        return True

    def validate_credit_card(self, credit_card):
        """
        Validates a credit card number string.

        Args:
            credit_card (str): The credit card number string to validate.

        Returns:
            bool: True if the credit card number string is valid, False otherwise.
        """
        if not re.match(self.input_parser.credit_card_pattern, credit_card):
            print("Invalid credit card format. Please enter the credit card in the correct format.")
            return False
        return True
