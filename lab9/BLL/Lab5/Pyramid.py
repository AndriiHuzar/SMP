import os

from colorama import init, Fore
import re


class Pyramid:
    """
    The Pyramid class generates a 3D or 2D representation of a pyramid.
    """

    def __init__(self, size=1, color='WHITE', symbol='#', remove_shadesPyramid=False):
        """
        Initializes a Pyramid object with a size, color, symbol, and a flag to remove shades.
        """
        self.size = size
        self.color = color
        self.symbol = symbol
        self.remove_shadesPyramid = remove_shadesPyramid
        self.pyramid_3D = None
        self.pyramid_2D = None

    def remove_color_codes(self, string):
        """
        Removes color codes from the string.
        """
        ansi_escape = re.compile(r'\x1B\[[0-?]*[ -/]*[@-~]')
        return ansi_escape.sub('', string)

    def remove_shades(self):
        """
        Removes shades from the pyramid.
        """
        if self.pyramid_3D is not None:
            self.pyramid_3D = [[cell.replace("=", "") for cell in row] for row in self.pyramid_3D]
        if self.pyramid_2D is not None:
            self.pyramid_2D = [[cell.replace("=", "") for cell in row] for row in self.pyramid_2D]

    def draw_3D(self):
        """
        Draws a 3D representation of the pyramid.
        """
        init()

        colors = {
            'RED': Fore.RED,
            'GREEN': Fore.GREEN,
            'YELLOW': Fore.YELLOW,
            'BLUE': Fore.BLUE,
            'MAGENTA': Fore.MAGENTA,
            'CYAN': Fore.CYAN,
            'WHITE': Fore.WHITE
        }

        self.pyramid_3D = [
            [colors[self.color] + " " * self.size * 11 + "/\\" + "*" * self.size + "."],
            [colors[self.color] + " " * self.size * 10 + "/" + self.symbol * self.size * 2 + "\\" + "*" * self.size * 2 + "."],
            [colors[self.color] + " " * self.size * 9 + "/" + self.symbol * self.size * 4 + "\\" + "*" * self.size * 3 + "."],
            [colors[self.color] + " " * self.size * 8 + "/" + self.symbol * self.size * 6 + "\\" + "*" * self.size * 4 + "."],
            [colors[self.color] + " " * self.size * 7 + "/" + self.symbol * self.size * 8 + "\\" + "*" * self.size * 4 + "|"],
            [colors[self.color] + " " * self.size * 6 + "/" + self.symbol * self.size * 10 + "\\" + "*" * self.size * 3 + "|"],
            [colors[self.color] + " " * self.size * 5 + "/" + self.symbol * self.size * 12 + "\\" + "*" * self.size * 2 + "|"],
            [colors[self.color] + " " * self.size * 4 + "/" + self.symbol * self.size * 14 + "\\" + "*" * self.size + "|"],
            [colors[self.color] + " " * self.size * 3 + "/" + "_" * self.size * 16 + "\\" + "|" + Fore.RESET],
            [colors[self.color] + " " * self.size * 2 + "=" * self.size * 15],
            [colors[self.color] + " " * self.size * 2 + "=" * self.size * 12],
            [colors[self.color] + " " * self.size * 2 + "=" * self.size * 9],
            [colors[self.color] + " " * self.size * 2 + "=" * self.size * 6],
            [colors[self.color] + " " * self.size * 2 + "=" * self.size * 3]
        ]

        if self.remove_shadesPyramid:
            self.remove_shades()

        for row in self.pyramid_3D:
            print(''.join(row))

    def draw_2D(self):
        """
        Draws a 2D representation of the pyramid.
        """
        init()

        colors = {
            'RED': Fore.RED,
            'GREEN': Fore.GREEN,
            'YELLOW': Fore.YELLOW,
            'BLUE': Fore.BLUE,
            'MAGENTA': Fore.MAGENTA,
            'CYAN': Fore.CYAN,
            'WHITE': Fore.WHITE
        }

        self.pyramid_2D = [
            [colors[self.color] + " " * self.size * 11 + "/\\"],
            [colors[self.color] + " " * self.size * 10 + "/" + self.symbol * self.size * 2 + "\\"],
            [colors[self.color] + " " * self.size * 9 + "/" + self.symbol * self.size * 4 + "\\"],
            [colors[self.color] + " " * self.size * 8 + "/" + self.symbol * self.size * 6 + "\\"],
            [colors[self.color] + " " * self.size * 7 + "/" + self.symbol * self.size * 8 + "\\"],
            [colors[self.color] + " " * self.size * 6 + "/" + self.symbol * self.size * 10 + "\\"],
            [colors[self.color] + " " * self.size * 5 + "/" + self.symbol * self.size * 12 + "\\"],
            [colors[self.color] + " " * self.size * 4 + "/" + self.symbol * self.size * 14 + "\\"],
            [colors[self.color] + " " * self.size * 3 + "/" + "_" * self.size * 16 + "\\" + Fore.RESET]
        ]

        if self.remove_shadesPyramid:
            self.remove_shades()

        for row in self.pyramid_2D:
            print(''.join(row))

    def set_size(self, size):
        """
        Sets the size of the pyramid.
        """
        if size in [1, 2]:
            self.size = size
        else:
            print("Invalid size. Please choose 1 or 2.")

    def savePyramid_3D(self, filename):
        """
        Saves the 3D representation of the pyramid to a file.
        """
        if self.pyramid_3D is None:
            print("Error: Draw the 3D pyramid first.")
            return

        pyramid_3D_no_color = [''.join([self.remove_color_codes(cell) for cell in row]) for row in self.pyramid_3D]

        self.output_directory = os.path.join('..', 'Data', 'Lab5')

        os.makedirs(self.output_directory, exist_ok=True)

        file_path = os.path.join(self.output_directory, filename)

        with open(file_path, 'w') as f:
            for row in pyramid_3D_no_color:
                f.write(row + '\n')


