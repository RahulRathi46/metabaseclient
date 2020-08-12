from .Core import Authenticate
from .Core import Card
from .Core import Dashboard
from .Core import Util


class Client(Authenticate):

    def __init__(self, url=None, username=None, password=None, token=None):
        if url != None and url[-1] == '/':
            url = url[:-1]

        super().__init__(url, username, password, token)

    def card(self):
        return Card(self.url, self.get_token())

    def dashboard(self):
        return Dashboard(self.url, self.get_token())

    def utils(self):
        return Util((self.url, self.get_token()))