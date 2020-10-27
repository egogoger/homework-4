# -*- coding: utf-8 -*-

import unittest
import sys

from tests.open_reg_form import BeforeEachTest

if __name__ == '__main__':
    suite = unittest.TestSuite((
        unittest.makeSuite(BeforeEachTest),
    ))
    result = unittest.TextTestRunner().run(suite)
    sys.exit(not result.wasSuccessful())
