import json
import logging
import os

from UI.MenuBuilder.MenuBuilder import MenuBuilder


class MenuLab4:
    """
    A class to manage the menu for Lab4.
    """

    def __init__(self, generator, reader_writer, validator):
        """
        Initializes the MenuLab4 with a generator, a reader/writer, and a validator.

        Args:
            generator: The generator to use for ASCII art.
            reader_writer: The reader/writer to use for file operations.
            validator: The validator to use for input validation.
        """
        self.generator = generator
        self.reader_writer = reader_writer
        self.validator = validator
        self.ascii_art_created = False
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

        menu_config = config['menu4']
        menu_builder = MenuBuilder(menu_config)

        menu_builder.display()

    def run(self):
        """
        Runs the menu, allowing the user to choose options and generate ASCII art.
        """
        while True:
            self.display_options()
            choice = self.validator.validate_input("Choose an option (1/2/3/4): ", ['1', '2', '3', '4'])
            logging.info(f'User chose option: {choice}')
            if choice == '1':
                self.generator.get_user_input()
            elif choice == '2':
                if not self.generator.text:
                    print("Error: Enter text first (option 1).")
                else:
                    self.ascii_art_created = True
                    self.generator.create_ascii_art()
            elif choice == '3':
                if not self.ascii_art_created:
                    print("Error: Create ASCII art first (option 2).")
                else:
                    self.generator.save_to_file()
            elif choice == '4':
                print("Goodbye!")
                logging.info('User exited.')
                break
            else:
                print("Invalid choice. Try again.")



