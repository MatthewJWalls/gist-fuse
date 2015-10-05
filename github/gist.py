
API_BASE_URL = "https://api.github.com"

import requests

class GistProxy:

    """ lazy-loaded proxy for the gist file data """
    
    def __init__(self, gistFileDict):
        """ takes a "files" dict from the json repr """
        self.name = gistFileDict["filename"]
        self.url = gistFileDict["raw_url"]

    def content(self):
        """ returns the content of the gist """
        r = requests.get(self.url)
        return r.text
        
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

        files = []
        
        for gist in g.json():
            for gistFile in gist["files"].values():
                files.append(GistProxy(gistFile))

        return files
    
