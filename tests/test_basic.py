# -*- coding: utf-8 -*-

import unittest

from MetabaseClient import Client


class BasicTestSuite(unittest.TestCase):
    """Basic test cases."""

    def test_import(self):
        assert True

    def test_object(self):
        ob = Client()
        assert True


if __name__ == '__main__':
    unittest.main()