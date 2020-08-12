from ..Client import Client
from nltk import word_tokenize,probability
import re



class FindCard(Client):

    def __init__(self, url=None, username=None, password=None, token=None):
        super().__init__(url, username, password, token)

    def transform(self, query):

        '''
            transform function transfom the query
            to words and its frequency.

            Attributes:
                query (str) : query trasformation. requide

            return:
                dict
        '''

        # step 1 : drop special char
        query = re.sub('[^A-Za-z.]+', ' ', query)

        # Step 2 : tokenize
        query = word_tokenize(query)

        # step 3 : droping char len < 1
        query = [i for i in query if len(i) > 1]

        # step 4 : count prob
        query = probability.FreqDist(query)

        # step 6 : convert for search
        query = dict(query)

        return query

    def search_match(self, search_query, query_db):

        '''
            transform function transfom the query
            to words and its frequency.

            Attributes:
                search_query (str) : search query . requide
                query_db (list(str)) : list(str) query universe . requide

            return:
                index (int)
        '''

        os = []
        d = self.transform(search_query)
        for i in query_db:
            try:
                q = self.transform(i)
                r = [k for k, v in q.items() if k in d.keys() and d[k] == v]
                os.append([i['id'], len(r) / len(q)])
            except Exception as e:
                os.append(-1)

        return os.index(max(os))