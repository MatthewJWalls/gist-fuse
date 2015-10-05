#!/usr/bin/env python3

import unittest
from github import gist

TEST_USER = "mojombo" # github's CEO

class IntegrationTests(unittest.TestCase):

    """ Integration tests that exercises the system """
    
    def test_get_all(self):
        """ test getting a list of gists """
        api = gist.API(name=TEST_USER)
        self.assertTrue(len(api.all()) > 0)

    def test_get_content(self):
        """ test getting the contents of a gist """
        api = gist.API(name=TEST_USER)
        self.assertTrue(len(api.all()[0].content()) > 0)

if __name__ == "__main__":
    unittest.main()
    
