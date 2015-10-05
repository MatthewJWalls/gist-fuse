
API_BASE_URL = "https://api.github.com"

import requests
import json

class GistProxy:

    """ lazy-loaded proxy for the gist file data """
    
    def __init__(self, headers, api, gistFileDict):
        """ takes a "files" dict from the json repr """
        self.headers = headers
        self.api = api
        self.name = gistFileDict["filename"]
        self.url = gistFileDict["raw_url"]

    def content(self):
        """ returns the content of the gist """
        r = requests.get(self.url)
        return r.text

    def update(self, data):
        """ replace the content of this gist with data """
        content = { "files" : { self.name : { "content" : data } }}

        r = requests.patch(
            self.api,
            headers=self.headers,
            data=json.dumps(content)
        )
    
class API:

    """ thin requests wrapper around the github gist API """

    def __init__(self, name=None, token=None):
        """ we take the users github api token in the constructor """
        self.token = token
        self.name = name
        self.headers = {"Authorization" : "token %s" % token}
        self.endpoints = {
            "list" : "users/%s/gists" % name
        }

    def all(self):
        """ retrieve a list of all gist names """

        g = requests.get(
            "%s/%s" % (API_BASE_URL, self.endpoints["list"]),
            headers=self.headers
        )

        files = []
        
        for gist in g.json():
            for gistFile in gist["files"].values():
                files.append(GistProxy(
                    self.headers,
                    gist["url"],
                    gistFile
                ))

        return files
