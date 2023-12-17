import json
import logging
import os

from UI.MenuBuilder.MenuBuilder import MenuBuilder


class MenuLab1:
    """
    A class to manage the menu for Lab1.
    """

    def __init__(self, calculator, validator):
        """
        Initializes the MenuLab1 with a calculator and a validator.

        Args:
            calculator: The calculator to use for calculations.
            validator: The validator to use for input validation.
        """
        self.calculator = calculator
        self.validator = validator
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

        menu_config = config['menu1']
        menu_builder = MenuBuilder(menu_config)

        menu_builder.display()

    def run(self):
        """
        Runs the menu, allowing the user to choose options and perform calculations.
        """
        valid_options = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11']

        while True:
            self.display_options()

            choice = self.validator.validate_input("Choose an option (1/2/3/4/5/6/7/8/9/10/11): ", valid_options)
            logging.info(f'User chose option: {choice}')
            if choice == '1':
                num1 = self.validator.validate_input("First number: ", [])
                num2 = self.validator.validate_input("Second number: ", [])
                result = self.calculator.summ(num1, num2)
                print(f"Result: {result}")
            elif choice == '2':
                num1 = self.validator.validate_input("First number: ", [])
                num2 = self.validator.validate_input("Second number: ", [])
                result = self.calculator.subtraction(num1, num2)
                print(f"Result: {result}")
            elif choice == '3':
                num1 = self.validator.validate_input("First number: ", [])
                num2 = self.validator.validate_input("Second number: ", [])
                result = self.calculator.multiplication(num1, num2)
                print(f"Result: {result}")
            elif choice == '4':
                num1 = self.validator.validate_input("First number: ", [])
                num2 = self.validator.validate_input("Second number: ", [])
                result = self.calculator.division(num1, num2)
                print(f"Result: {result}")
            elif choice == '5':
                num1 = self.validator.validate_input("First number: ", [])
                num2 = self.validator.validate_input("Second number: ", [])
                result = self.calculator.power(num1, num2)
                print(f"Result: {result}")
            elif choice == '6':
                num1 = self.validator.validate_input("First number: ", [])
                result = self.calculator.square(num1)
                print(f"Result: {result}")
            elif choice == '7':
                num1 = self.validator.validate_input("First number: ", [])
                num2 = self.validator.validate_input("Second number: ", [])
                result = self.calculator.remains(num1, num2)
                print(f"Result: {result}")
            elif choice == '8':
                self.calculator.decimal_places = int(
                    self.validator.validate_input("Enter the number of decimal places: ", []))
            elif choice == '9':
                print("Value from memory:", self.calculator.memory)
            elif choice == '10':
                print("History of calculations:")
                for entry in self.calculator.history:
                    print(entry)
            elif choice == '11':
                print("Goodbye!")
                logging.info('User exited.')
                break

