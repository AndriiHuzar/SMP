class MenuBuilder:
    """
    A class to build and display a menu.
    """

    def __init__(self, config):
        """
        Initializes the MenuBuilder with a configuration.

        Args:
            config (dict): The configuration for the menu.
        """
        self.version = config['version']
        self.title = config['title']
        self.options = config['options']
        self.is_vertical = config['is_vertical']

    def display(self):
        """
        Displays the menu to the user.
        """
        max_option_length = max([len(option) for option in self.options])
        border_length = max_option_length * len(self.options) + len(
            self.options) * 5 - 1 if not self.is_vertical else len(self.title) + 2
        border = "+" + "-" * border_length + "+"
        title_padding = (border_length - len(self.title)) // 2
        print(border)
        print("|" + " " * title_padding + "\033[1;31m" + self.title + "\033[m" + " " * (
                    border_length - title_padding - len(self.title)) + "|")  # Red color
        print(border)
        for i, option in enumerate(self.options):
            print("\033[1;32m" + (str(i + 1) + ". " if self.is_vertical else str(i + 1) + ". ") + option + "\033[m",
                  end=("\n" if self.is_vertical else "     "))  # Green color
        print(border)
        print("\033[1;34m" + f"Menu Version: {self.version}" + "\033[m")  # Blue color
