import os
import unittest

from selenium.webdriver import DesiredCapabilities, Remote
from selenium.webdriver.support.ui import WebDriverWait

from pages.main_page import MainPage, RegForm
from tests.test_class import Test
from tests.open_reg_form import open_reg_form


class EmptyFieldsTest(Test):
	# Correct messages
	EMPTY_NAME_ERROR = 'Enter your name'
	EMPTY_LOGIN_ERROR = 'Enter login'
	EMPTY_EMAIL_ERROR = 'Enter email'
	EMPTY_PASSWORD_ERROR = 'Enter password'
	EMPTY_PASSWORD2_ERROR = 'Repeat the password'

	# tmp messages
	TMP_PASSWORD = 'kek8971364'

	def test(self):
		main_page = MainPage(self.driver)
		form = main_page.reg_form
		open_reg_form(self, main_page, form)

        # All fields empty
		form.submit()
		self.check_name_error_msg(form, self.EMPTY_NAME_ERROR)
		self.check_login_error_msg(form, self.EMPTY_LOGIN_ERROR)
		self.check_email_error_msg(form, self.EMPTY_EMAIL_ERROR)
		self.check_password_error_msg(form, self.EMPTY_PASSWORD_ERROR)

		# Second password empty
		form.set_password(self.TMP_PASSWORD)
		form.submit()
		self.check_password_error_msg(form, self.EMPTY_PASSWORD2_ERROR)

	def check_name_error_msg(self, form: RegForm, text):
		self.assertEqual(text, form.get_name_error().text)

	def check_login_error_msg(self, form: RegForm, text):
		self.assertEqual(text, form.login_error.text)

	def check_email_error_msg(self, form: RegForm, text):
		self.assertEqual(text, form.email_error.text)

	def check_password_error_msg(self, form: RegForm, text):
		self.assertEqual(text, form.password_error.text)
