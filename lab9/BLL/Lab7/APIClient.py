import requests


class APIClient:
    """
    The APIClient class interacts with an API to get data.
    """

    def __init__(self, api_url):
        """
        Initializes an APIClient object with an API URL.
        """
        self.api_url = api_url

    def get_data(self):
        """
        Gets data from the API.
        """
        response = requests.get(self.api_url)
        return response.json()


