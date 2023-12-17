import os
import sys
import pyfiglet
from colorama import Fore, init


init(autoreset=True)


class ASCIIArtGenerator:
    """
    The ASCIIArtGenerator class generates ASCII art based on user input.
    """

    def __init__(self, reader_writer, validator):
        """
        Initializes an ASCIIArtGenerator object with a reader_writer, a validator, and default settings.
        """
        self.validator = validator
        self.reader_writer = reader_writer
        self.settings = {
            "text": "",
            "font": "standard",
            "color": "white",
            "character": "@",
            "width": 60,
            "height": 20,
            "saved_art": None
        }

    def get_user_input(self):
        """
        Prompts the user for a word or phrase to convert into ASCII art.
        """
        self.settings["text"] = self.reader_writer.read_input("Enter a word or phrase: ")

    def choose_font(self):
        """
        Prompts the user to choose a font from the available options.
        """
        fonts = pyfiglet.FigletFont.getFonts()
        print("Available fonts:")
        for font in fonts:
            print(font)
        self.settings["font"] = self.reader_writer.read_input("Choose a font: ")

    def choose_color(self):
        """
        Prompts the user to choose a color for the ASCII art.
        """
        print("Available colors: red, blue, green, yellow, white, etc.")
        self.settings["color"] = self.reader_writer.read_input("Choose a color: ")

    def choose_character(self):
        """
        Prompts the user to choose a character to use in generating the ASCII art.
        """
        self.settings["character"] = self.reader_writer.read_input("Enter a character for generating ASCII art: ")

    def get_art_size(self):
        """
        Prompts the user to enter the desired width and height for the ASCII art.
        """
        self.settings["width"] = int(input("Enter the desired width: "))
        self.settings["height"] = int(input("Enter the desired height: "))

    def generate_ascii_art(self):
        """
        Generates ASCII art based on the user's settings.
        """
        custom_fig = pyfiglet.Figlet(font=self.settings["font"], width=self.settings["width"])
        ascii_art = custom_fig.renderText(self.settings["text"])
        ascii_art = ascii_art.replace("#", self.settings["character"])
        self.settings["saved_art"] = ascii_art
        return ascii_art

    def preview_ascii_art(self):
        """
        Displays a preview of the generated ASCII art.
        """
        ascii_art = self.generate_ascii_art()
        if ascii_art:
            colored_ascii_art = Fore.__getattribute__(self.settings["color"].upper()) + ascii_art
            print("\nHere is a preview of your ASCII art:\n")
            print(colored_ascii_art)
        else:
            print("Empty!")

    def save_to_file(self):
        """
        Saves the generated ASCII art to a file.
        """
        if not self.settings["saved_art"]:
            print("Nothing to save!")
            return
        filename = input("Enter the file name for saving (with .txt extension): ")
        relative_path = os.path.join('..', 'Data', 'Lab3', filename)
        absolute_path = os.path.abspath(relative_path)
        with open(absolute_path, "w") as file:
            file.write(self.settings["saved_art"])
        print(f"ASCII art saved to the file {absolute_path}")

