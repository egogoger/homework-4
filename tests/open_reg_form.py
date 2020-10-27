import os
import unittest

from selenium.webdriver import DesiredCapabilities, Remote
from selenium.webdriver.support.ui import WebDriverWait

from pages.main_page import MainPage, RegForm
from tests.test_class import Test


def open_reg_form(test_case: unittest.TestCase, main_page: MainPage, form: RegForm):
    main_page.open()
    form.open()
    test_case.assertEqual("SIGN UP", form.title_text)


class OpenRegTest(Test):
    def test(self):
        main_page = MainPage(self.driver)
        form = main_page.reg_form
        open_reg_form(self, main_page, form)
