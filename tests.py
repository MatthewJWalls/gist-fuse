#!/usr/bin/env python3

import unittest

from github import gist

class TestGistAPI(unittest.TestCase):

    def test_stub(self):
        """ test the stub """
        api = gist.API()
        self.assertEqual(api.stub(), "stub")

if __name__ == "__main__":
    unittest.main()
    
