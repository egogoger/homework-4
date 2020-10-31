import os
import unittest

from selenium.webdriver import DesiredCapabilities, Remote
from selenium.webdriver.support.ui import WebDriverWait

from pages.main_page import MainPage, RegForm
from tests.test_class import Test
from tests.open_reg_form import open_reg_form
from utils import get_datetime

class InvalidLoginTest(Test):
	# Correct messages
	LOGIN_ERROR = 'Login must contain at least 3 letters or numbers'
	BACKEND_ERROR = 'Bad request'

	CYRILLIC_NAME = 'Вася'
	CYRILLIC_WITH_NUMBERS_NAME = CYRILLIC_NAME+'1'
	SHORT_NAME = 'ke'
	LONG_NAME = 'a' * 257
	NUMERIC_NAME = '123'


	@property
	def correct_values(self):
		timestamp = get_datetime()
		return ['Name_'+timestamp, 'Login_'+timestamp, 'email_'+timestamp+'@mail.ru', 'password', 'password']
	

	def set_correct_values(self, form: RegForm):
		for iii in range(len(form.INPUTS)):
			form.set_input(form.INPUTS[iii], self.correct_values[iii])


	def test(self):
		main_page = MainPage(self.driver)
		form = main_page.reg_form
		open_reg_form(self, main_page, form)
		form.clear_inputs()

		# Cyrillic name
		form.set_input(form.LOGIN, self.CYRILLIC_NAME)
		form.submit()
		form.check_error_msg_for(form.LOGIN_ERROR, self, self.LOGIN_ERROR)
		form.clear_inputs()

		# Cyrillic with numbers name
		form.set_input(form.LOGIN, self.CYRILLIC_WITH_NUMBERS_NAME)
		form.submit()
		form.check_error_msg_for(form.LOGIN_ERROR, self, self.LOGIN_ERROR)
		form.clear_inputs()

		# Short name
		form.set_input(form.LOGIN, self.SHORT_NAME)
		form.submit()
		form.check_error_msg_for(form.LOGIN_ERROR, self, self.LOGIN_ERROR)
		form.clear_inputs()

		# Numeric name
		form.set_input(form.LOGIN, self.NUMERIC_NAME)
		form.submit()
		form.check_error_msg_for(form.LOGIN_ERROR, self, None)
		form.clear_inputs()

		# Long name (BACKEND check)
		self.set_correct_values(form)
		form.set_input(form.LOGIN, self.LONG_NAME)
		form.submit()
		form.check_error_msg_for(form.BACKEND_ERROR, self, self.BACKEND_ERROR)
		form.clear_inputs()
