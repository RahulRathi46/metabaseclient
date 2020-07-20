from json import loads

from requests import get


class Card:
    url = None
    token = None
    api_endpoint = '/api/card'

    def __init__(self, url, token):
        self.url = url
        self.token = token

    def get_card(self, id=None):

        headers = {
            "Content-Type": "application/json",
            "X-Metabase-Session": self.token
        }

        if id != None:
            cards = get(self.url + self.api_endpoint + '/' + str(id),
                        headers=headers)
        else:
            cards = get(self.url + self.api_endpoint,
                        headers=headers)

        return loads(cards.text)

    def post_card(self, card):
        pass
