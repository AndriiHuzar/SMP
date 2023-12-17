import psutil
import pyfiglet
from colorama import init, Fore

class ASCIIArtGenerator:
    def __init__(self):
        self.text = ""
        self.font = "standard"
        self.color = Fore.WHITE
        self.character = "@"

    def get_user_input(self):
        self.text = input("Enter a word or phrase: ")

    def choose_font(self):
        fonts = ["standard", "banner", "big", "block", "doom", "slant"]
        print("Available fonts:")
        for font in fonts:
            print(font)
        font_1 = input("Choose a font: ").lower()
        if font_1 not in fonts:
            print("Invalid font choice. Using default (standard).")
        else:
            self.font = font_1

    def choose_color(self):
        print("Available colors: RED, BLUE, GREEN, YELLOW, WHITE, etc.")
        color_choice = input("Choose a color: ").upper()
        if hasattr(Fore, color_choice):
            self.color = getattr(Fore, color_choice)
            print(f"Selected color: {color_choice}")
        else:
            print(f"Invalid color choice: {color_choice}. Using default (WHITE).")

    def choose_art_size(self):
        while True:
            try:
                self.width = int(input("Enter the width of the ASCII art: "))
                self.height = int(input("Enter the height of the ASCII art: "))
                if self.width <= 0 or self.height <= 0:
                    print("Width and height must be positive integers.")
                else:
                    break
            except ValueError:
                print("Invalid input. Please enter a valid integer for width and height.")

    def generate_ascii_art(self):
        ascii_art = pyfiglet.Figlet(font=self.font).renderText(self.text)
        formatted_ascii_art = self.format_ascii_art(ascii_art)
        return formatted_ascii_art

    def format_ascii_art(self, ascii_art):
        lines = ascii_art.split('\n')
        formatted_art = ""
        for line in lines:
            formatted_art += line.center(self.width) + "\n"
        return formatted_art

    def preview_ascii_art(self, ascii_art):
        print("Preview of the ASCII art:")
        print(self.color + ascii_art)

    def save_to_file(self, ascii_art):
        filename = input("Enter the file name for saving (with .txt extension): ")

        available_memory = psutil.virtual_memory().available
        ascii_art_size = len(ascii_art.encode('utf-8'))

        if ascii_art_size > available_memory:
            print("Not enough memory to save the ASCII art. Please reduce the size of your art.")
        else:
            with open(filename, "w") as file:
                file.write(ascii_art)
            print(f"ASCII art saved to the file {filename}")

if __name__ == "__main__":
    init(autoreset=True)  # Initializes colorama to automatically reset the color
    generator = ASCIIArtGenerator()

    generator.get_user_input()
    generator.choose_font()
    generator.choose_color()
    generator.choose_art_size()

    ascii_art = generator.generate_ascii_art()
    generator.preview_ascii_art(ascii_art)
    generator.save_to_file(ascii_art)