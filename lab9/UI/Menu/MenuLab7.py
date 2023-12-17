import json
import logging
import os
from colorama import Fore
from colorama import Style
from UI.MenuBuilder.MenuBuilder import MenuBuilder


class MenuLab7:
    """
    A class to manage the menu for Lab7.
    """

    def __init__(self, api_app, validator, reader_writer):
        """
        Initializes the MenuLab7 with an API app, a validator, and a reader/writer.

        Args:
            api_app: The API app to use for data retrieval.
            validator: The validator to use for input validation.
            reader_writer: The reader/writer to use for file operations.
        """
        self.api_app = api_app
        self.validator = validator
        self.reader_writer = reader_writer
        log_file_path = os.path.join('..', 'Data', 'Lab9', 'app.log')
        logging.basicConfig(filename=log_file_path, filemode='w',
                            format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        logging.getLogger().setLevel(logging.INFO)

    def display_options(self):
        """
        Displays the menu options to the user.
        """
        current_file_directory = os.path.dirname(os.path.abspath(__file__))
        relative_config_path = os.path.join('..', '..', 'Config', 'init.json')
        config_path = os.path.abspath(os.path.join(current_file_directory, relative_config_path))

        with open(config_path, 'r') as file:
            config = json.load(file)

        menu_config = config['menu7']
        menu_builder = MenuBuilder(menu_config)

        menu_builder.display()

    def run(self):
        """
        Runs the menu, allowing the user to choose options and interact with the API app.
        """
        while True:
            self.display_options()
            choice = self.validator.validate_input("Choose an option (1/2/3/4/5): ", ['1', '2', '3', '4', '5'])
            logging.info(f'User chose option: {choice}')
            if choice == '1':
                valid_data = False
                data = None
                while not valid_data:
                    data_type, user_input = self.api_app.get_user_input()
                    if data_type == 'phone':
                        if self.validator.validate_phone(user_input):
                            valid_data = True
                    elif data_type == 'email':
                        if self.validator.validate_email(user_input):
                            valid_data = True
                    elif data_type == 'credit card':
                        if self.validator.validate_credit_card(user_input):
                            valid_data = True
                    elif data_type == 'date':
                        if self.validator.validate_date(user_input):
                            valid_data = True
                if valid_data:
                    self.api_app.run(data_type, user_input)
            elif choice == '2':
                self.api_app.history.view_history()
            elif choice == '3':
                display_choice = self.validator.validate_input("Choose a data display format (list/table): ",
                                                               ['list', 'table'])
                data_from_api = self.api_app.get_data_from_api()
                self.api_app.history.add_to_history('Display data', data_from_api)
                if display_choice == 'list':
                    print(data_from_api)
                else:
                    self.api_app.results_display.display_data(data_from_api, Fore.BLUE, Style.BRIGHT)
            elif choice == '4':
                save_choice = self.validator.validate_input("Do you want to save the data? (yes/no): ", ['yes', 'no'])
                if save_choice == 'yes':
                    format_choice = self.validator.validate_input(
                        "Choose a format to save the data (json/csv/txt): ", ['json', 'csv', 'txt'])
                    self.api_app.data_saver.save_data(self.api_app.get_data_from_api(), format_choice)
                    print(f"Data saved in {format_choice} format.")
            elif choice == '5':
                print("Goodbye!")
                logging.info('User exited.')
                break
            else:
                print("Invalid choice. Please try again.")


