import os
import unittest

from selenium.webdriver import DesiredCapabilities, Remote
from selenium.webdriver.support.ui import WebDriverWait

from pages.main_page import MainPage, RegForm
from tests.test_class import Test
from tests.open_reg_form import open_reg_form
from utils import get_datetime


class ValidRegTest(Test):
	time = get_datetime()
	# Correct fields
	NAME = 'Вася Васильев'
	LOGIN = f'egogoger_{time}'
	EMAIL = f'egogoger_{time}@kek.kek'
	PASSWORD = 'password'

	def test(self):
		main_page = MainPage(self.driver)
		form = main_page.reg_form
		open_reg_form(self, main_page, form)

		inputs = [
			[form.NAME, self.NAME],
			[form.LOGIN, self.LOGIN],
			[form.EMAIL, self.EMAIL],
			[form.PASSWORD, self.PASSWORD],
			[form.PASSWORD2, self.PASSWORD],
		]

		for i in inputs:
			form.set_input(i[0], i[1])

		form.submit()
		form.check_if_dissappeared()

		main_page.check_for_self(self)
		main_page.check_for_login(self, self.LOGIN)
