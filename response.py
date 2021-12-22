import requests

from .url import URL

class Response:
    """
    Base response class
    """

    # build response
    def __init__(self, url: URL, method):
        self.url = url
        self.method = method

        # TODO: Add support for PUSH method
        self.__response = requests.get(self.url)
        self.__response.raise_for_status()

    def search(self):
        pass

    @property
    def text(self) -> str:
        return self.__response.text

    @property
    def json(self) -> dict:
        return self.__response.json()

    @property
    def dict(self) -> dict:
        return self.__response.json()