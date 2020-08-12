from re import search
from ..Client import Client


class SearchCard(Client):
    results = []

    def __init__(self, url=None, username=None, password=None, token=None):
        super().__init__(url, username, password, token)

    def search_by_keyword(self, keyword):
        cards = self.card().get()
        self.results = []

        for i in cards:
            try:
                card = i['dataset_query']
                if card[card['type']]['query'].lower().find(keyword.lower()) >= 0:
                    self.results.append({
                        'Name': i['name'],
                        'link': self.url + '/question/' + str(i['id'])
                    })
            except:
                pass

        return self.results

    def search_by_email(self, email):
        cards = self.card().get()
        self.results = []

        for i in cards:
            try:
                if i['creator']['email'].lower().find(email.lower()) >= 0:
                    self.results.append({
                        'Name': i['name'],
                        'link': self.url + '/question/' + str(i['id'])
                    })
            except:
                pass

        return self.results

    def search_by_name(self, name):
        cards = self.card().get()
        self.results = []

        for i in cards:
            try:
                if i['name'].lower().find(name.lower()) >= 0:
                    self.results.append({
                        'Name': i['name'],
                        'link': self.url + '/question/' + str(i['id'])
                    })
            except:
                pass

        return self.results

    def search_by_regex(self, regex_string):
        cards = self.card().get()
        self.results = []

        for i in cards:
            try:
                card = i['dataset_query']
                if search(regex_string, card[card['type']]['query'].lower()):
                    self.results.append({
                        'Name': i['name'],
                        'link': self.url + '/question/' + str(i['id'])
                    })
            except:
                pass

        return self.results

    def search_by_function(self, function):
        cards = self.card().get()
        self.results = []

        for i in cards:
            try:
                card = i['dataset_query']
                if function(card[card['type']]['query'].lower()) == True:
                    self.results.append({
                        'Name': i['name'],
                        'link': self.url + '/question/' + str(i['id'])
                    })
            except:
                pass

        return self.results
