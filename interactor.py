import requests

class Interactor:
    def __init__(self, basepath, nospaces: bool = False):
        self.__basepath = basepath

    def validate(self, url):
        if self.__nospaces and (url.count(' ') != 0):
            raise Exception(f'Interactor does not support spaces! "{url}"')

    def get(self, url: str, basepath: bool = True):
        if not url.startswith('http') and basepath:
            url = self.__basepath + url
        
        return requests.get(url)

def str_to_dict(string):
    string = string.replace('false', 'False').replace('true', 'True').replace('null', 'None')

    return eval(string)

def objectify(dictionary: "str | dict") -> object:
    if isinstance(dictionary, str):
        dictionary = str_to_dict(dictionary)

    class Wrapper:
        def __init__(self):
            for key in dictionary.keys():
                setattr(self, str(key), dictionary[key])

    wrapper = Wrapper()

    return wrapper

if __name__ == '__main__':
    cowboycodr = str_to_dict('{"user":"cowboycodr"}')

    print(cowboycodr['user'])