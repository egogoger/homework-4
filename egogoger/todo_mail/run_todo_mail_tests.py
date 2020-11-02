import unittest
import sys

from .tests.auth_test import AuthTest


def run_virusmusic_tests():
    suite = unittest.TestSuite((
        unittest.makeSuite(AuthTest),
    ))
    unittest.TextTestRunner().run(suite)
