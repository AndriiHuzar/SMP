import requests

class DisplayDogApi:
    # Base URL for the Dog API
    BASE_URL = "https://dog.ceo/api"

    @classmethod
    def get_all_breeds(cls):
        """
        Get a list of all dog breeds from the Dog API.

        Returns:
            list: A list of dog breeds.
        """
        # Make a request to the API to get the list of all breeds
        response = requests.get(f"{cls.BASE_URL}/breeds/list/all")
        # Parse the JSON response
        data = response.json()
        # Extract the breeds from the response
        breeds = data.get("message", {})
        return breeds.keys()

    @classmethod
    def get_random_image(cls, breed):
        """
        Get a random image URL for a specific dog breed from the Dog API.

        Args:
            breed (str): The dog breed for which to retrieve a random image.

        Returns:
            str: The URL of a random image for the specified breed.
        """
        # Make a request to the API to get a random image for the specified breed
        response = requests.get(f"{cls.BASE_URL}/breed/{breed}/images/random")
        # Parse the JSON response
        data = response.json()
        # Extract the image URL from the response
        image_url = data.get("message", "")
        return image_url
