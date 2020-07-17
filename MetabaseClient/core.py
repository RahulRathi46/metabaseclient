# -*- coding: utf-8 -*-
# from . import helpers

class Client:

    host = ''
    username = ''
    password = ''
    token = ''




    def login(self , host , username , password):
        if host == None or username == None:
            return False
        else : 
            return True


    def __init__(self , host=None , username=None , password=None , token=None):
        self.host = host
        self.username = username
        self.password = password
        self.token = token

        if password != None and token == None:
            self.login(host,username,password)



