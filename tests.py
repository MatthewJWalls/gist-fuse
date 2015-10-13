#!/usr/bin/env python3

import unittest
import config
from github import gist

class APIIntegrationTests(unittest.TestCase):

    """ Integration tests that exercises the system """
    
    def test_get_all(self):
        """ test getting a list of gists """
        api = gist.API(name=config.USER, token=config.TOKEN)
        self.assertTrue(len(api.all()) > 0)

    def test_get_content(self):
        """ test getting the contents of a gist """
        api = gist.API(name=config.USER, token=config.TOKEN)
        self.assertTrue(len(api.all()[0].content()) > 0)

    def test_update(self):
        """ test updating a gist """
        api = gist.API(name=config.USER, token=config.TOKEN)
        api.all()[0].update("this is a test")
        
if __name__ == "__main__":
    unittest.main()
