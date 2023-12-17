import json
import logging
import os
from UI.MenuBuilder.MenuBuilder import MenuBuilder


class MenuLab8:
    """
    A class to manage the menu for Lab8.
    """

    def __init__(self, data_processor, validator, reader_writer):
        """
        Initializes the MenuLab8 with a data processor, a validator, and a reader/writer.

        Args:
            data_processor: The data processor to use for data exploration and visualization.
            validator: The validator to use for input validation.
            reader_writer: The reader/writer to use for file operations.
        """
        self.data_processor = data_processor
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

        menu_config = config['menu8']
        menu_builder = MenuBuilder(menu_config)

        menu_builder.display()

    def run(self):
        """
        Runs the menu, allowing the user to choose options and interact with the data processor.
        """
        valid_options = ['1', '2', '3', '4']

        while True:
            self.display_options()
            choice = self.validator.validate_input("Choose an option (1/2/3/4): ", valid_options)
            logging.info(f'User chose option: {choice}')
            if choice == '1':
                if self.validator.validate_input("Explore data? (yes/no): ", ['yes', 'no']) == 'yes':
                    print("Exploring data...")
                    self.data_processor.explore_data()
                    logging.info('User chose to explore data.')
            elif choice == '2':
                if self.validator.validate_input("Generate visualizations? (yes/no): ", ['yes', 'no']) == 'yes':
                    print("Generating visualizations...")
                    self.data_processor.visualize_data()
                    logging.info('User chose to generate visualizations.')
            elif choice == '3':
                if self.validator.validate_input("Save visualizations? (yes/no): ", ['yes', 'no']) == 'yes':
                    print("Saving visualizations...")
                    self.data_processor.visualize_data(save=True)
                    logging.info('User chose to save visualizations.')
            elif choice == '4':
                print("Goodbye!")
                logging.info('User exited.')
                break
            else:
                print(f"No results: {choice}. Please try again.")







