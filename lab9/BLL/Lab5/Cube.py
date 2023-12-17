import os

from colorama import init, Fore
import re


class Cube:
    """
    The Cube class generates a 3D or 2D representation of a cube.
    """

    def __init__(self, size=1, color='WHITE', symbol='#', remove_shades=False):
        """
        Initializes a Cube object with a size, color, symbol, and a flag to remove shades.
        """
        self.size = size
        self.color = color
        self.symbol = symbol
        self.remove_shades = remove_shades
        self.cube_3D = None
        self.cube_2D = None

    def remove_color_codes(self, string):
        """
        Removes color codes from the string.
        """
        ansi_escape = re.compile(r'\x1B\[[0-?]*[ -/]*[@-~]')
        return ansi_escape.sub('', string)

    def draw_3D(self):
        """
        Draws a 3D representation of the cube.
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

        self.cube_3D = [
            ["*" * (3 if self.size == 1 else 3) + colors[self.color] + "X" + "=" * self.size * 10 + "X"],
            ["*" * (1 if self.size == 1 else 1) + colors[self.color] + "/" + self.symbol * self.size * 11 + "/" + "|"],
            [colors[self.color] + "X" + "=" * self.size * 11 + "X" + self.symbol * self.size + "|"],
            [colors[self.color] + "|" + self.symbol * self.size * 11 + "|" + self.symbol * self.size + "X"],
            [colors[self.color] + "|" + self.symbol * self.size * 11 + "|" + self.symbol * self.size + "/"],
            [colors[self.color] + "|" + self.symbol * self.size * 11 + "|" + "/"],
            [colors[self.color] + "X" + "=" * self.size * 11 + "X" + Fore.RESET]
        ]

        if self.remove_shades:
            self.cube_3D[0][0] = self.cube_3D[0][0].replace("*", " ", 3 if self.size == 1 else 3)
            self.cube_3D[1][0] = self.cube_3D[1][0].replace("*", " ", 1)

        if self.size == 2 and self.remove_shades:
            self.cube_3D[0][0] = "  " + self.cube_3D[0][0]
            self.cube_3D[1][0] = " " + self.cube_3D[1][0]

        for row in self.cube_3D:
            print(''.join(row))

    def draw_2D(self):
        """
        Draws a 2D representation of the cube.
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

        self.cube_2D = [
            [colors[self.color] + "X" + "=" * self.size * 11 + "X"],
            [colors[self.color] + "|" + self.symbol * self.size * 11 + "|"],
            [colors[self.color] + "|" + self.symbol * self.size * 11 + "|"],
            [colors[self.color] + "|" + self.symbol * self.size * 11 + "|"],
            [colors[self.color] + "X" + "=" * self.size * 11 + "X" + Fore.RESET]
        ]

        for row in self.cube_2D:
            print(''.join(row))

    def saveCube_3D(self, filename):
        """
        Saves the 3D representation of the cube to a file.
        """
        if self.cube_3D is None:
            print("Error: Draw the 3D cube first.")
            return

        cube_3D_no_color = [''.join([self.remove_color_codes(cell) for cell in row]) for row in self.cube_3D]

        self.output_directory = os.path.join('..', 'Data', 'Lab5')

        os.makedirs(self.output_directory, exist_ok=True)

        file_path = os.path.join(self.output_directory, filename)

        with open(file_path, 'w') as f:
            for row in cube_3D_no_color:
                f.write(row + '\n')
