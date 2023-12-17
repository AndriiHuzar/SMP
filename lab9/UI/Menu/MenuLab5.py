import json
import logging
import os
from BLL.Lab5.Cube import Cube
from BLL.Lab5.Pyramid import Pyramid
from UI.MenuBuilder.MenuBuilder import MenuBuilder


class MenuLab5:
    """
    A class to manage the menu for Lab5.
    """

    def __init__(self, reader_writer, validator):
        """
        Initializes the MenuLab5 with a reader/writer and a validator.

        Args:
            reader_writer: The reader/writer to use for file operations.
            validator: The validator to use for input validation.
        """
        self.reader_writer = reader_writer
        self.validator = validator
        self.figure = None
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

        menu_config = config['menu5']
        menu_builder = MenuBuilder(menu_config)

        menu_builder.display()

    def run(self):
        """
        Runs the menu, allowing the user to choose options and generate ASCII art.
        """
        while True:
            self.display_options()
            choice = self.validator.validate_input("Choose an option (1/2/3/4/5/6): ", ['1', '2', '3', '4', '5', '6'])
            logging.info(f'User chose option: {choice}')
            if choice == '1':
                figure_choice = self.validator.validate_input("Choose a figure (Cube/Pyramid): ", ['Cube', 'Pyramid'])
                if figure_choice == 'Cube':
                    self.figure = Cube()
                else:
                    self.figure = Pyramid()
            elif choice == '2':
                if self.figure is None:
                    print("Error: Choose a figure first (option 1).")
                else:
                    size = self.validator.validate_input("Enter size for figure (1 or 2): ", ['1', '2'])
                    color = self.validator.validate_input(
                        "Enter color for figure (RED, GREEN, YELLOW, BLUE, MAGENTA, CYAN, WHITE): ",
                        ['RED', 'GREEN', 'YELLOW', 'BLUE', 'MAGENTA', 'CYAN', 'WHITE'])
                    symbol = self.reader_writer.read_input("Enter symbol for figure: ")
                    remove_shades = self.validator.validate_input(
                        "Do you want to remove shades? (yes/no): ", ['yes', 'no'])
                    self.figure = Cube(int(size), color, symbol, remove_shades.lower() == 'yes') if isinstance(
                        self.figure, Cube) else Pyramid(int(size), color, symbol, remove_shades.lower() == 'yes')
            elif choice == '3':
                if self.figure is None:
                    print("Error: Enter parameters for figure first (option 2).")
                else:
                    self.figure.draw_3D()
            elif choice == '4':
                if self.figure is None:
                    print("Error: Enter parameters for figure first (option 2).")
                else:
                    self.figure.draw_2D()
            elif choice == '5':
                if self.figure is None:
                    print("Error: Enter parameters for figure first (option 2).")
                else:
                    filename = self.reader_writer.read_input("Enter a filename to save the 3D figure: ")
                    if isinstance(self.figure, Cube):
                        self.figure.saveCube_3D(filename)
                    else:
                        self.figure.savePyramid_3D(filename)
                    print(f"3D figure saved in file {filename}")
            elif choice == '6':
                print("Goodbye!")
                logging.info('User exited.')
                break
            else:
                print("Invalid choice. Try again.")

