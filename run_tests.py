# -*- coding: utf-8 -*-

import unittest
import sys

from tests.open_reg_form import OpenRegTest
from tests.empty_fields import EmptyFieldsTest
from tests.invalid_name import InvalidNameTest


if __name__ == '__main__':
    suite = unittest.TestSuite((
        # unittest.makeSuite(OpenRegTest),
        # unittest.makeSuite(EmptyFieldsTest),
        unittest.makeSuite(InvalidNameTest)
    ))
    result = unittest.TextTestRunner().run(suite)
    sys.exit(not result.wasSuccessful())
