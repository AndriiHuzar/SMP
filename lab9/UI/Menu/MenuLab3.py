import json
import logging
import os

from UI.MenuBuilder.MenuBuilder import MenuBuilder


class MenuLab3:
    """
    A class to manage the menu for Lab3.
    """

    def __init__(self, generator, validator, reader_writer):
        """
        Initializes the MenuLab3 with a generator, a validator, and a reader/writer.

        Args:
            generator: The generator to use for ASCII art.
            validator: The validator to use for input validation.
            reader_writer: The reader/writer to use for file operations.
        """
        self.generator = generator
        self.validator = validator
        self.reader_writer = reader_writer
        current_file_directory = os.path.dirname(os.path.abspath(__file__))
        relative_config_path = os.path.join('..', '..', 'Config', 'init.json')
        config_path = os.path.abspath(os.path.join(current_file_directory, relative_config_path))
        with open(config_path, 'r') as file:
            config = json.load(file)
        self.menu_config = config['menu3']
        self.menu_builder = MenuBuilder(self.menu_config)
        log_file_path = os.path.join('..', 'Data', 'Lab9', 'app.log')
        logging.basicConfig(filename=log_file_path, filemode='w',
                            format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        logging.getLogger().setLevel(logging.INFO)

    def display_options(self):
        """
        Displays the menu options to the user.
        """
        self.menu_builder.display()

    def run(self):
        """
        Runs the menu, allowing the user to choose options and generate ASCII art.
        """
        while True:
            self.display_options()
            choice = self.validator.validate_input("Enter a choice number: ",
                                                   [str(i + 1) for i in range(len(self.menu_config['options']))])
            logging.info(f'User chose option: {choice}')
            if choice == '1':
                if self.validator.validate_input("Get user input? (yes/no): ", ['yes', 'no']) == 'yes':
                    self.generator.get_user_input()
            elif choice == '2':
                if self.validator.validate_input("Choose font? (yes/no): ", ['yes', 'no']) == 'yes':
                    self.generator.choose_font()
            elif choice == '3':
                if self.validator.validate_input("Choose color? (yes/no): ", ['yes', 'no']) == 'yes':
                    self.generator.choose_color()
            elif choice == '4':
                if self.validator.validate_input("Select characters? (yes/no): ", ['yes', 'no']) == 'yes':
                    self.generator.choose_character()
            elif choice == '5':
                if self.validator.validate_input("Set art size? (yes/no): ", ['yes', 'no']) == 'yes':
                    self.generator.get_art_size()
            elif choice == '6':
                if self.validator.validate_input("Generate and preview ASCII Art? (yes/no): ", ['yes', 'no']) == 'yes':
                    self.generator.preview_ascii_art()
            elif choice == '7':
                if self.validator.validate_input("Save to file? (yes/no): ", ['yes', 'no']) == 'yes':
                    self.generator.save_to_file()
            elif choice == '8':
                print("Goodbye!")
                logging.info('User exited.')
                break



