import pandas as pd
from tabulate import tabulate
from colorama import Style
import numpy as np


class ResultsDisplay:
    """
    The ResultsDisplay class displays results in a formatted table.
    """

    def display_data(self, data, headers_color, font_style):
        """
        Displays data in a formatted table with the specified headers color and font style.
        """
        if np.isscalar(data):
            df = pd.DataFrame([data])
        elif isinstance(data, dict):
            df = pd.DataFrame([data])
        else:
            df = pd.DataFrame(data)
        formatted_table = tabulate(df, headers='keys', tablefmt='psql')
        print(self.apply_styles(formatted_table, headers_color, font_style))

    @staticmethod
    def apply_styles(text, color, style):
        """
        Applies the specified color and style to the text.
        """
        return f"{color}{style}{text}{Style.RESET_ALL}"
