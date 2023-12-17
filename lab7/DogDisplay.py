import csv
import json
from io import BytesIO

import requests
from PIL import Image
from tabulate import tabulate
from colorama import Fore

from DisplayDogAPI import DisplayDogApi


class DogDisplay:
    @staticmethod
    def display_table(data, color):
        # Display data in a table format with headers and colors
        headers = [Fore.RESET + color + "DogBreed", Fore.RESET + color + "PictureUrl"]
        rows = [(color + breed, DisplayDogApi.get_random_image(breed)) for breed in data]
        table = tabulate(rows, headers, tablefmt="grid")
        print(table)

    @staticmethod
    def display_list(data, color):
        # Display data as a list with colors
        for breed in data:
            print(color + f"{breed}: {DisplayDogApi.get_random_image(breed)}")

    @staticmethod
    def display_image(image_url):
        # Display an image given its URL
        response = requests.get(image_url)
        img = Image.open(BytesIO(response.content))
        img.show()

    @staticmethod
    def remove_color_codes(text):
        # Remove color codes from the given text
        while '\033[' in text:
            start = text.find('\033[')
            end = text.find('m', start)
            if end != -1:
                text = text[:start] + text[end + 1:]
            else:
                break
        return text

    @staticmethod
    def save_to_json(data, filename):
        # Save data to a JSON file
        data_to_save = [{"DogBreed": breed, "PictureUrl": DisplayDogApi.get_random_image(breed)} for breed in data]
        with open(filename, 'w') as file:
            json.dump(data_to_save, file, indent=2)
        print(f"Data saved to {filename} in JSON format.")

    @staticmethod
    def save_to_csv(data, filename):
        # Save data to a CSV file
        with open(filename, 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow([Fore.RESET + "DogBreed", Fore.RESET + "PictureUrl"])
            for breed in data:
                writer.writerow([DogDisplay.remove_color_codes(breed), DogDisplay.remove_color_codes(DisplayDogApi.get_random_image(breed))])
        print(f"Data saved to {filename} in CSV format.")

    @staticmethod
    def save_to_txt(data, filename):
        # Save data to a TXT file
        with open(filename, 'w') as file:
            for breed in data:
                file.write(f"{DogDisplay.remove_color_codes(breed)}: {DogDisplay.remove_color_codes(DisplayDogApi.get_random_image(breed))}\n")
        print(f"Data saved to {filename} in TXT format.")
