from json import loads, dumps

from requests import post


class Authenticate:
    ''' Authenticate is core class which provides metabase
        session.

        Attributes:
            url (str) : metabase host. default value None
            username (str) : metabase username. default value None
            password (str) : metabase password. default value None
            token (str) : metabase session token. default value None

        Return:
            class object
    '''

    url = ''
    username = ''
    password = ''
    token = ''
    api_endpoint = '/api/session'

    def get_token(self):

        '''get_token return metabase session token after
            login is successful else None

            Return:
                token (str)
        '''

        return self.token

    def set_token(self, token):
        self.token = token

    def authenticate(self, url, username, password):
        headers = {
            "Content-Type": "application/json"
        }

        payload = {
            "username": username,
            "password": password
        }

        session = post(url + self.api_endpoint,
                       data=dumps(payload),
                       headers=headers
                       )

        if session.ok == True:
            self.token = loads(session.content)['id']
            return self.token
        else:
            return session.status_code

    def __init__(self, url=None, username=None, password=None, token=None):
        self.url = url
        self.username = username
        self.password = password
        self.token = token

        if url != None and password != None:
            self.token = self.authenticate(url, username, password)
