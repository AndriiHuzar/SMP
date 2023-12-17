import unittest

from BLL.Lab1.BasicCalculator import BasicCalculator
from BLL.Lab2.Calculator import Calculator
from BLL.Lab3.ASCIIArtGenerator import ASCIIArtGenerator
from BLL.Lab4.ASCIIArtGenerate import ASCIIArtGenerate
from BLL.Lab6.UnitTestCalculator import UnitTestsCalculator
from BLL.Lab7.APIApp import APIApp
from BLL.Lab7.APIClient import APIClient
from BLL.Lab7.DataSaver import DataSaver
from BLL.Lab7.ErrorHandler import ErrorHandler
from BLL.Lab7.History import History
from BLL.Lab7.InputParser import InputParser
from BLL.Lab7.ResultsDisplay import ResultsDisplay
from BLL.Lab8.DataProcessor import DataProcessor
from Shared.Libraries.rw_lib.ReaderWriter import ReaderWriter
from Shared.Libraries.validator_lib.Validator import Validator
from Shared.Libraries.art_lib.ascii_art_library import ascii_art
from UI.Menu.MenuLab1 import MenuLab1
from UI.Menu.MenuLab2 import MenuLab2
from UI.Menu.MenuLab3 import MenuLab3
from UI.Menu.MenuLab4 import MenuLab4
from UI.Menu.MenuLab5 import MenuLab5
from UI.Menu.MenuLab7 import MenuLab7
from UI.Menu.MenuLab8 import MenuLab8


class Run:
    """
    The Run class runs different labs.
    """

    def __init__(self):
        """
        Initializes a Run object with a reader/writer and a validator.
        """
        self.reader_writer = ReaderWriter()
        input_parser = InputParser()
        self.validator = Validator(input_parser)

    def run_lab1(self):
        """
        Runs lab 1.
        """
        calculator = BasicCalculator()
        menu = MenuLab1(calculator, self.validator)
        menu.run()

    def run_lab2(self):
        """
        Runs lab 2.
        """
        calculator = Calculator()
        menu = MenuLab2(calculator)
        menu.run()

    def run_lab3(self):
        """
        Runs lab 3.
        """
        generator = ASCIIArtGenerator(self.reader_writer, self.validator)
        menu = MenuLab3(generator, self.validator, self.reader_writer)
        menu.run()

    def run_lab4(self):
        """
        Runs lab 4.
        """
        generator = ASCIIArtGenerate(ascii_art, self.reader_writer)
        menu = MenuLab4(generator, self.reader_writer, self.validator)
        menu.run()

    def run_lab5(self):
        """
        Runs lab 5.
        """
        menu = MenuLab5(self.reader_writer, self.validator)
        menu.run()

    def run_lab6(self):
        """
        Runs lab 6.
        """
        suite = unittest.TestLoader().loadTestsFromTestCase(UnitTestsCalculator)
        unittest.TextTestRunner().run(suite)

    def run_lab7(self):
        """
        Runs lab 7.
        """
        api_client = APIClient(api_url='https://jsonplaceholder.typicode.com/todos/1')
        input_parser = InputParser()
        history = History()
        error_handler = ErrorHandler()
        results_display = ResultsDisplay()
        data_saver = DataSaver()

        api_app = APIApp(api_client, self.reader_writer, self.validator, history, error_handler, results_display, input_parser, data_saver)
        menu_lab7 = MenuLab7(api_app, self.validator, self.reader_writer)
        menu_lab7.run()

    def run_lab8(self):
        """
        Runs lab 8.
        """
        data_processor = DataProcessor()
        menu = MenuLab8(data_processor, self.validator, self.reader_writer)
        menu.run()

    def run(self):
        """
        Runs the specified lab or quits.
        """
        while True:
            lab = input("Enter the number of the lab (1-8) or 'q' to quit: ")
            if lab == '1':
                self.run_lab1()
            elif lab == '2':
                self.run_lab2()
            elif lab == '3':
                self.run_lab3()
            elif lab == '4':
                self.run_lab4()
            elif lab == '5':
                self.run_lab5()
            elif lab == '6':
                self.run_lab6()
            elif lab == '7':
                self.run_lab7()
            elif lab == '8':
                self.run_lab8()
            elif lab.lower() == 'q':
                print("Goodbye!")
                break
            else:
                print(f"No results: {lab}. Please try again.")


if __name__ == "__main__":
    Run().run()

