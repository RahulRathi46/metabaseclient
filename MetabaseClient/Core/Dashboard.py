from json import loads

from requests import get


class Dashboard:
    url = None
    token = None
    api_endpoint = '/api/dashboard'

    def __init__(self, url, token):
        self.url = url
        self.token = token

    def get_dashboard(self, id=None):

        headers = {
            "Content-Type": "application/json",
            "X-Metabase-Session": self.token
        }

        if id != None:
            dashboard = get(self.url + self.api_endpoint + '/' + str(id),
                            headers=headers)
        else:
            dashboard = get(self.url + self.api_endpoint,
                            headers=headers)

        return loads(dashboard.text)
