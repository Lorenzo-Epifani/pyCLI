

class Luminati:
    def __init__(self,token):

        self.__token=''
        self.__base_url=''

    @property
    def token(self):
        return self.__token

    @token.setter
    def token(self, token: str):
        self.__token = token

    @property
    def base_url(self):
        return self.__base_url

    @base_url.setter
    def base_url(self, base_url: str):
        self.__base_url = base_url


    