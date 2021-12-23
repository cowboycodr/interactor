import requests
import json

from .url import URL
from .response import Response

class Interactor:
    """
    Extensible API interaction base class
    """

    def __init__(self, url: "str | URL"):
        self.__url_history = []
        self.__url = None

        if isinstance(url, URL):
            self.url = url
        else:
            self.url = URL(url)

    def get(self, branches: "str | list[str]") -> Response:
        if isinstance(branches, str):
            branches = [branches]

        url = self.url.join_branches(branches)

        return Response(url, "GET")
    
    def post(self, branches: "str | list[str]", body, headers={}) -> Response:
        if isinstance(branches, str):
            branches = [branches]

        url = self.url.join_branches(branches)

        return requests.post(url, body, headers=headers)
    
    @property
    def url(self) -> str:
        return self.__url

    @url.setter
    def url(self, value):
        self.__url_history.append(value)
        self.__url = value

if __name__ == '__main__':
    class Bible(Interactor):
        def __init__(self):
            super().__init__("https://bible-api.com/")

        def quote(self, quote: str):
            return self.get(quote)

    print(
        Bible().quote("John 15:16")
    )
