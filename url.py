class URL:
    def __init__(self, url: str):
        self.__url = url.strip()

        if self.__url.count("//") == 0:
            self.__protocol = "https://"
            self.__url = self.__protocol + self.__url
        else:
            self.__protocol = self.__url.split("//")[0] + "//"

    def __repr__(self) -> str:
        return f"URL(url='{self.string}')"

    def __str__(self) -> str:
        return self.string

    def join(self, branch: str) -> "URL":
        branch = branch.strip()

        if branch.startswith("/"):
            branch = branch[0:]

        return URL(
            self.string + branch
        )

    def join_branches(self, branches: "list[str]"):
        result = URL(self.__url)
        for key, branch in enumerate(branches):
            if key < len(branches) - 1:
                branch += "/"

            result = result.join(branch)
            
        return result

    @property
    def string(self) -> str:
        return self.__url

    @property
    def branches(self) -> "list[URL]":
        url = self.string

        if url.endswith("/"):
            url = url[:-1]

        branches = url.replace(
            self.__protocol,
            ""
        ).split("/")[1:]

        return branches