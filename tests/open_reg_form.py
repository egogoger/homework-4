import os
import unittest

from selenium.webdriver import DesiredCapabilities, Remote
from selenium.webdriver.support.ui import WebDriverWait

from pages.main_page import MainPage, RegForm
from tests.test_class import Test


import unittest

class OpenRegTest(Test):
    TITLE = "SIGN UP"

    def test(self):
        main_page = MainPage(self.driver)
        main_page.open()
        form = main_page.reg_form
        form.open()
        self.assertEqual(self.TITLE, form.title_text)
