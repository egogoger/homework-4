import os
import unittest

from selenium.webdriver import DesiredCapabilities, Remote
from selenium.webdriver.support.ui import WebDriverWait

from pages.main_page import MainPage, RegForm


class BeforeEachTest(unittest.TestCase):
    TITLE = "SIGN UP"

    def setUp(self):
        browser = os.environ.get('BROWSER', 'CHROME')

        self.driver = Remote(
            command_executor='http://127.0.0.1:4444/wd/hub',
            desired_capabilities=getattr(DesiredCapabilities, browser).copy()
        )

    def tearDown(self):
        self.driver.quit()

    def test(self):
        main_page = MainPage(self.driver)
        main_page.open()
        form = main_page.reg_form
        form.open()
        self.assertEqual(self.TITLE, form.title_text)
