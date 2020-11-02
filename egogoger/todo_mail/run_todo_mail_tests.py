import unittest

from .tests.auth_test import AuthTest


def run_todo_mail_tests():
    suite = unittest.TestSuite((
        unittest.makeSuite(AuthTest),
    ))
    unittest.TextTestRunner().run(suite)
