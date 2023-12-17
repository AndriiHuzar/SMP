"""
Utility class for adding color to text in a terminal.
"""


class ColorUtil:
    """
    Define color codes as ANSI escape sequences.
    """
    colors = {
        'white': '\033[1;37m',
        'grey': '\033[1;30m',
        'reset': '\033[0m'
    }

    @classmethod
    def colorize(cls, text, color='white'):
        """
        Colorizes the given text with the specified color.

        Args:
            text (str): The text to colorize.
            color (str, optional): The color to use. Defaults to 'white'.

        Returns:
            str: The colorized text.
        """
        color_code = cls.colors.get(color)
        if color_code:
            return f"{color_code}{text}{cls.colors['reset']}"
        else:
            return text
