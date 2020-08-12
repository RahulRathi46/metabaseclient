from json import loads
import requests


class Util:

    url = None
    token = None
    bug_report_details_api_endpoint = '/api/util/bug_report_details'
    logs_api_endpoint = '/api/util/logs'
    random_token_api_endpoint = '/api/util/random_token'
    stats_api_endpoint = '/api/util/stats'
    password_check_api_endpoint = '/api/util/password_check'

    def __init__(self, url, token):

        '''
            class constructor

            Note:
                You must be a superuser to use this class.

            Attributes:
                url (str) : metabase host. Requide
                token (str) : metabase session token. Requide

            Return:
                class object
        '''

        self.url = url
        self.token = token


    def bug_report_details(self):

        '''
            bug_report_details function return bug
            details.

            return:
                list(json) or json
        '''

        headers = {
            "Content-Type": "application/json",
            "X-Metabase-Session": self.token
        }

        bug_report_details = requests.get(self.url + self.bug_report_details_api_endpoint ,
                                 headers=headers)

        return loads(bug_report_details.text)

    def logs(self):

        '''
            logs function return metabase logs.

            return:
                list(json) or json

        '''

        headers = {
            "Content-Type": "application/json",
            "X-Metabase-Session": self.token
        }

        logs = requests.get(self.url + self.logs_api_endpoint ,
                                 headers=headers)

        return loads(logs.text)


    def random_token(self):

        '''
            random_token function returns 32 bit metabase
            token.

            return:
                json

        '''

        headers = {
            "Content-Type": "application/json",
            "X-Metabase-Session": self.token
        }

        token = requests.get(self.url + self.random_token_api_endpoint ,
                                 headers=headers)

        return loads(token.text)


    def stats(self):

        '''
            stats function return stats from
            metabase

            return:
                list(json) or json

        '''

        headers = {
            "Content-Type": "application/json",
            "X-Metabase-Session": self.token
        }

        stats = requests.get(self.url + self.stats_api_endpoint ,
                                 headers=headers)

        return loads(stats.text)


    def password_check(self , password):

        '''
            password_check function checks currently
            configured password complexity rules.

            return:
                json

        '''

        headers = {
            "Content-Type": "application/json",
            "X-Metabase-Session": self.token,
            "password" : password
        }

        password_check = requests.post(self.url + self.password_check_api_endpoint ,
                                 headers=headers)

        return loads(password_check.text)