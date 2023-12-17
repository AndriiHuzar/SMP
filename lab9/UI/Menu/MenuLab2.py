import json
import logging
import os

from UI.MenuBuilder.MenuBuilder import MenuBuilder


class MenuLab2:
    """
    A class to manage the menu for Lab2.
    """

    def __init__(self, calculator):
        """
        Initializes the MenuLab2 with a calculator.

        Args:
            calculator: The calculator to use for calculations.
        """
        self.calculator = calculator
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

        menu_config = config['menu2']
        menu_builder = MenuBuilder(menu_config)

        menu_builder.display()

    def run(self):
        """
        Runs the menu, allowing the user to choose options and perform calculations.
        """
        while True:
            self.display_options()
            user_choice = input("Choose an option (1/2): ")
            logging.info(f'User chose option: {user_choice}')
            if user_choice == '1':
                self.calculator.perform_calculation()
                print("Would you like to perform another calculation? (y/n): ")
                user_choice = input()
                if user_choice.lower() != 'y':
                    break
            elif user_choice == '2':
                print("Goodbye!")
                logging.info('User exited.')
                break


