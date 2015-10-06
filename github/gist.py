
import requests
import json

API_BASE_URL = "https://api.github.com"

class GistProxy:

    """ lazy-loaded proxy for the gist file data """
    
    def __init__(self, session, api, gistFileDict):
        """ takes a "files" dict from the json repr """
        self.session = session
        self.api = api
        self.name = gistFileDict["filename"]
        self.url = gistFileDict["raw_url"]

    def content(self):
        """ returns the content of the gist """
        r = self.session.get(self.url)
        return r.text

    def update(self, data):
        """ replace the content of this gist with data """
        content = { "files" : { self.name : { "content" : data } }}

        r = self.session.patch(
            self.api,
            data=json.dumps(content)
        )
    
class API:

    """ thin requests wrapper around the github gist API """

    def __init__(self, name=None, token=None):
        """ we take the users github api token in the constructor """
        self.name = name
        self.token = token
        self.session = requests.Session()
        self.session.headers.update({"Authorization" : "token %s" % token})
        self.session.headers.update({"Connection" : "close"})
        
        self.endpoints = {
            "list" : "users/%s/gists" % name
        }

    def all(self):
        """ retrieve a list of all gist names """

        g = self.session.get(
            "%s/%s" % (API_BASE_URL, self.endpoints["list"]),
        )

        files = []
        
        for gist in g.json():
            for gistFile in gist["files"].values():
                files.append(GistProxy(
                    self.session,
                    gist["url"],
                    gistFile
                ))

        return files
