from egogoger.virusmusic.pages.main_page import MainPage
from .test_class import Test
from .open_reg_form import open_reg_form


class InvalidPassword2Test(Test):
	# Correct messages
	PASSWORD_ERROR = 'Passwords must match'

	CORRECT_PASS = 'kek'
	INCORRECT_PASS = 'l'

	def test(self):
		main_page = MainPage(self.driver)
		form = main_page.reg_form
		open_reg_form(self, main_page, form)

		form.set_input(form.PASSWORD, self.CORRECT_PASS)
		form.set_input(form.PASSWORD2, self.INCORRECT_PASS)
		form.submit()
		form.check_error_msg_for(form.PASSWORD_ERROR, self, self.PASSWORD_ERROR)
