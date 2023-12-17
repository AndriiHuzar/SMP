from colorama import Fore, Style


class APIApp:
    """
    The APIApp class interacts with an API client to get data, validates and parses user input,
    handles errors, displays results, and saves data.
    """

    def __init__(self, api_client, reader_writer, validator, history, error_handler, results_display, input_parser,
                 data_saver):
        """
        Initializes an APIApp object with an API client, a reader/writer, a validator, a history,
        an error handler, a results display, an input parser, and a data saver.
        """
        self.api_client = api_client
        self.reader_writer = reader_writer
        self.validator = validator
        self.history = history
        self.error_handler = error_handler
        self.results_display = results_display
        self.input_parser = input_parser
        self.data_saver = data_saver

    def get_data_from_api(self):
        """
        Gets data from the API client.
        """
        return self.api_client.get_data()

    def get_user_input(self):
        """
        Gets user input for the desired data type and the data itself.
        """
        data_type = self.validator.validate_input("Enter the desired type(phone, email, credit card, date): ",
                                                  ['phone', 'email', 'credit card', 'date'])
        user_input = self.reader_writer.read_input(f"Enter {data_type}: ")
        return data_type, user_input

    def run(self, data_type, user_input):
        """
        Runs the APIApp with the given data type and user input.
        """
        try:
            data_from_api = self.api_client.get_data()

            if data_type == 'phone':
                if self.validator.validate_phone(user_input):
                    print("Phone number is valid.")
                else:
                    print("Invalid phone format. Please enter the phone in the correct format.")
            elif data_type == 'email':
                if self.validator.validate_email(user_input):
                    print("Email is valid.")
                else:
                    print("Invalid email format. Please enter the email in the correct format.")
            elif data_type == 'credit card':
                if self.validator.validate_credit_card(user_input):
                    print("Credit card number is valid.")
                else:
                    print("Invalid credit card format. Please enter the credit card in the correct format.")
            elif data_type == 'date':
                if self.validator.validate_date(user_input):
                    print("Date is valid.")
                else:
                    print("Invalid date format. Please enter the date in the format DD/MM/YYYY.")

            dates, phones, emails, credit_cards = self.error_handler.handle_error(self.input_parser.parse_user_input)(
                user_input)

            self.history.add_to_history(user_input, (dates, phones, emails, credit_cards))

            self.results_display.display_data(data_from_api, Fore.BLUE, Style.BRIGHT)

            self.data_saver.save_data(data_from_api, 'json')

        except Exception as e:
            print(f"Error: {e}")
