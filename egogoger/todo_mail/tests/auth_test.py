from egogoger.todo_mail.pages.main_page import MainPage
from egogoger.base_test import Test


class AuthTest(Test):
    def test(self):
        main_page = MainPage(self.driver)
        # auth_form = main_page.auth_form
