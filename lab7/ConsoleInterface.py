import sys
from DogAPI import DogAPI
from DisplayDogAPI import DisplayDogApi
import signal
from colorama import Fore
from DogDisplay import DogDisplay

class ConsoleInterface:
    def __init__(self):
        # Initialize the ConsoleInterface with an empty history list
        self.history = []

def signal_handler(sig, frame):
    # Signal handler for Ctrl+C interrupt
    print("You pressed Ctrl+C!")
    sys.exit(0)

def choose_display_format():
    # Prompt the user to choose a display format (Table or List)
    while True:
        print("Choose a display format:")
        print("1. Table")
        print("2. List")
        format_choice = input("Enter the number of the display format: ")

        if format_choice in ("1", "2"):
            return format_choice
        else:
            print("Invalid display format. Please enter 1 or 2.")

def choose_color():
    # Prompt the user to choose a color (Red, Green, or Yellow)
    while True:
        print("Choose a color:")
        print("1. Red")
        print("2. Green")
        print("3. Yellow")
        color_choice = input("Enter the number of the color: ")

        if color_choice == "1":
            return Fore.RED
        elif color_choice == "2":
            return Fore.GREEN
        elif color_choice == "3":
            return Fore.YELLOW
        else:
            print("Invalid color choice. Please enter 1, 2, or 3.")

def start_menu():
    # Display the start menu options and prompt the user to choose an option
    print("Hello! It's dog API. Choose the option:")
    print("1. Continue")
    print("2. Exit")
    option = input("Enter the number of the option: ")
    return option

def main():
    # Main function to interact with the user and perform operations
    api_key = "live_Qm70bYO91yDzUWHnjK8SpliWvFnkRCPl5lS6f8THqR0qDkzP84oTm4Y8RF0WFJvm"
    dog_api = DogAPI(api_key)
    interface = ConsoleInterface()

    while True:
        user_option = start_menu()

        if user_option == "1":
            breeds = DisplayDogApi.get_all_breeds()

            color = choose_color()
            format_choice = choose_display_format()

            if format_choice == "1":
                DogDisplay.display_table(breeds, color)
            elif format_choice == "2":
                DogDisplay.display_list(breeds, color)

            save_choice = input("Do you want to save the data? (y/n): ")
            if save_choice.lower() == 'y':
                save_format = input("Choose a save format:\n1. JSON\n2. CSV\n3. TXT\nEnter the number of the save format: ")
                save_filename = input("Enter the filename: ")
                if save_format == "1":
                    DogDisplay.save_to_json(breeds, save_filename)
                elif save_format == "2":
                    DogDisplay.save_to_csv(breeds, save_filename)
                elif save_format == "3":
                    DogDisplay.save_to_txt(breeds, save_filename)
                else:
                    print("Invalid save format. Please enter 1, 2, or 3.")

            repeat_choice = input("Do you want to perform another operation? (y/n): ")
            if repeat_choice.lower() != 'y':
                break
        elif user_option == "2":
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Invalid option. Please enter 1 or 2.")

if __name__ == "__main__":
    # Set up a signal handler for Ctrl+C
    signal.signal(signal.SIGINT, signal_handler)
    # Call the main function
    main()
