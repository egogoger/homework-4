import os
import unittest

from selenium.webdriver import DesiredCapabilities, Remote
from selenium.webdriver.support.ui import WebDriverWait

from pages.main_page import MainPage, RegForm
from tests.test_class import Test
from tests.open_reg_form import open_reg_form

class InvalidNameTest(Test):
	CYRILLIC_NAME = 'Вася'
	SHORT_NAME = '1'
	LONG_NAME = 'a' * 257

	def test(self):
		main_page = MainPage(self.driver)
		form = main_page.reg_form
		open_reg_form(self, main_page, form)

		# Cyrillic name
		form.set_name(self.CYRILLIC_NAME)
		form.submit()
		form.check_error_msg_for(form.NAME_ERROR, self, None)

		# Short name
		form.set_name(self.SHORT_NAME)
		form.submit()
		form.check_error_msg_for(form.NAME_ERROR, self, None)

		# Long name
		form.set_name(self.LONG_NAME)
		form.submit()
		form.check_error_msg_for(form.NAME_ERROR, self, None)
