import os
import unittest

from selenium.webdriver import DesiredCapabilities, Remote
from selenium.webdriver.support.ui import WebDriverWait

from pages.main_page import MainPage, RegForm
from tests.test_class import Test
from tests.open_reg_form import open_reg_form

class InvalidLoginTest(Test):
	# Correct messages
	LOGIN_ERROR = 'Login must contain at least 3 letters or numbers'

	CYRILLIC_NAME = 'Вася'
	CYRILLIC_WITH_NUMBERS_NAME = CYRILLIC_NAME+'1'
	SHORT_NAME = 'ke'
	LONG_NAME = 'a' * 257
	NUMERIC_NAME = '123'

	def test(self):
		main_page = MainPage(self.driver)
		form = main_page.reg_form
		open_reg_form(self, main_page, form)

		# Cyrillic name
		form.set_input(form.LOGIN, self.CYRILLIC_NAME)
		form.submit()
		form.check_error_msg_for(form.LOGIN_ERROR, self, self.LOGIN_ERROR)

		# Cyrillic with numbers name
		form.set_input(form.LOGIN, self.CYRILLIC_WITH_NUMBERS_NAME)
		form.submit()
		form.check_error_msg_for(form.LOGIN_ERROR, self, self.LOGIN_ERROR)

		# Short name
		form.set_input(form.LOGIN, self.SHORT_NAME)
		form.submit()
		form.check_error_msg_for(form.LOGIN_ERROR, self, self.LOGIN_ERROR)

		# Long name
		form.set_input(form.LOGIN, self.LONG_NAME)
		form.submit()
		form.check_error_msg_for(form.LOGIN_ERROR, self, None)

		# Numeric name
		form.set_input(form.LOGIN, self.NUMERIC_NAME)
		form.submit()
		form.check_error_msg_for(form.LOGIN_ERROR, self, None)
