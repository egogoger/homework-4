import os
import unittest

from selenium.webdriver import DesiredCapabilities, Remote
from selenium.webdriver.support.ui import WebDriverWait

from pages.main_page import MainPage, RegForm
from tests.test_class import Test
from tests.open_reg_form import open_reg_form

class HaveAccountClickTest(Test):
	def test(self):
		main_page = MainPage(self.driver)
		reg_form = main_page.reg_form
		open_reg_form(self, main_page, reg_form)

		reg_form.click_on(reg_form.ACCOUNT_ALREADY)

		login_form = main_page.login_form
		login_form.check_for_self(self)
