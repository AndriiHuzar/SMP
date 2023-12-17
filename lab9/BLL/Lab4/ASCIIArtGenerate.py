import os

from Shared.Libraries.validator_lib.Validator import Validator
from Shared.Libraries.util_lib.color_util import ColorUtil


class ASCIIArtGenerate:
    """
    The ASCIIArtGenerator class generates ASCII art based on user input.
    """

    def __init__(self, ascii_art, reader_writer):
        """
        Initializes an ASCIIArtGenerator object with an ascii_art object, a reader_writer, and default settings.
        """
        self.ascii_art = ascii_art
        self.text = ''
        self.validator = Validator(None)
        self.reader_writer = reader_writer

    def get_user_input(self):
        """
        Prompts the user for a word or phrase to convert into ASCII art.
        """
        self.text = self.reader_writer.read_input('Enter a word: ')

    def get_user_symbol(self):
        """
        Prompts the user to choose a symbol to use in the ASCII art.
        """
        symbol_mapping = {
            '*': 'Star (*)',
            '#': 'Hash character (#)',
            '@': 'Special character (@)',
            '?': 'Question mark (?)',
            '=': 'Equal sign (=)',
            '-': 'Hyphen (-)'
        }

        print("Available symbols for ASCII art:")
        for symbol, description in symbol_mapping.items():
            print(f"{symbol}: {description}")

        user_choice = self.reader_writer.read_input('Choose a symbol for ASCII art: ')
        if user_choice in symbol_mapping:
            self.user_symbol = user_choice
        else:
            print("Invalid choice.")

    def get_art_size(self):
        """
        Prompts the user to enter the desired width and height for the ASCII art.
        """
        self.width = int(self.reader_writer.read_input('Enter the width of the ASCII art (2-40): '))
        self.height = int(self.reader_writer.read_input('Enter the height of the ASCII art (2-40): '))

    def get_alignment(self):
        """
        Prompts the user to choose the alignment of the ASCII art.
        """
        alignment_options = {
            'left': 'left',
            'center': 'center',
            'right': 'right',
        }
        choice = self.reader_writer.read_input('Choose text alignment (left/center/right): ')
        if choice in alignment_options:
            self.alignment = alignment_options[choice]
        else:
            print("Invalid choice.")

    def get_colors(self):
        """
        Prompts the user to choose the colors of the symbols in the ASCII art.
        """
        self.colors = []
        for i in range(len(self.user_symbol)):
            color_options = {
                'white': 'white',
                'grey': 'grey',
            }
            choice = self.reader_writer.read_input(f'Choose a color for symbol {self.user_symbol[i]}: ')
            while choice not in color_options:
                print("Invalid choice.")
                choice = self.reader_writer.read_input(f'Choose a color for symbol {self.user_symbol[i]}: ')
            self.colors.append(choice)

    def generate_art(self):
        """
        Generates ASCII art based on the user's settings.
        """
        ascii_art = ''
        for char in self.text:
            if char.upper() in self.ascii_art:
                art = self.ascii_art[char.upper()]
                art = [line.replace('*', self.user_symbol) for line in art]
                art = art[:self.height]
                while len(art) < self.height:
                    art.append(' ' * self.width)
                ascii_art += '\n'.join(art) + '\n'
            else:
                ascii_art += f"ASCII art for the letter {char} is not available.\n"

        if self.alignment == 'center':
            lines = ascii_art.strip().split('\n')
            ascii_art = '\n'.join(line.center(self.width) for line in lines)
        elif self.alignment == 'right':
            lines = ascii_art.strip().split('\n')
            ascii_art = '\n'.join(line.rjust(self.width) for line in lines)

        colored_art = ''
        for symbol, color in zip(self.user_symbol, self.colors):
            colored_art += ColorUtil.colorize(symbol, color)

        ascii_art = ascii_art.replace(self.user_symbol, colored_art)
        return ascii_art

    def create_ascii_art(self):
        """
        Creates ASCII art based on user input.
        """
        self.get_user_symbol()
        self.get_art_size()
        self.get_alignment()
        self.get_colors()
        self.ascii_art = self.generate_art()
        self.display_art(self.ascii_art)

    def display_art(self, ascii_art):
        """
        Displays the generated ASCII art.
        """
        print("Created ASCII art:")
        print(ascii_art)

    def save_to_file(self):
        """
        Saves the generated ASCII art to a file.
        """
        filename = self.reader_writer.read_input("Enter a filename to save the ASCII art: ")
        ascii_art_no_color = self.remove_color_codes(self.ascii_art)

        directory = os.path.join('..', 'Data', 'Lab4')

        if not os.path.exists(directory):
            os.makedirs(directory)

        filepath = os.path.join(directory, filename)

        self.reader_writer.write_output(filepath, ascii_art_no_color)
        print(f"ASCII art saved in file {filepath}")

    def remove_color_codes(self, text):
        """
        Removes color codes from the text.
        """
        while '\033[' in text:
            start = text.find('\033[')
            end = text.find('m', start)
            if end != -1:
                text = text[:start] + text[end + 1:]
            else:
                break
        return text


