
API_BASE_URL = "https://api.github.com"

import requests

class API:

    """ thin requests wrapper around the github gist API """

    def __init__(self, name=None, token=None):
        """ we take the users github api token in the constructor """
        self.token = token
        self.name = name
        self.endpoints = {
            "list" : "users/%s/gists" % name
        }

    def all(self):
        """ retrieve a list of all gist names """
        g = requests.get("%s/%s" % (API_BASE_URL, self.endpoints["list"]))
        return g.json()
