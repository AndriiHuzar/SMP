from colorama import init

# Initialize colorama with autoreset to automatically reset colors after each print statement
init(autoreset=True)

class DogAPI:
    # Base URL for The Dog API
    base_url = "https://api.thedogapi.com/v1"

    def __init__(self, api_key):
        # Initialize DogAPI object with the provided API key
        self.headers = {"x-api-key": api_key}
