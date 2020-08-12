from json import loads
import requests


class Dashboard:

    '''
        Card Class is core class which provides metabase
        dashboards.

        Attributes:
            url (str) : metabase host. default value None
            token (str) : metabase session token. default value None
            api_endpoint (str) : metabase api endpoint

        Return:
            class object
        '''

    url = None
    token = None
    api_endpoint = '/api/dashboard'

    def __init__(self, url, token):

        '''
            class constructor

            Attributes:
                url (str) : metabase host. Requide
                token (str) : metabase session token. Requide

            Return:
                class object
        '''

        self.url = url
        self.token = token

    def get(self, id=None):

        '''
        get function returns all the dashboard
        stored in metabase.

        Attributes:
            id (int) : dashboard id. default value None
            id = None return all the queries stored in metabase dashboard.

        Return:
            list(json) or json representation card stored.
    '''

        headers = {
            "Content-Type": "application/json",
            "X-Metabase-Session": self.token
        }

        if id != None:
            dashboard = requests.get(self.url + self.api_endpoint + '/' + str(id),
                            headers=headers)
        else:
            dashboard = requests.get(self.url + self.api_endpoint,
                            headers=headers)

        return loads(dashboard.text)
