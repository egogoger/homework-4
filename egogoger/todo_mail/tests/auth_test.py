import os

from egogoger.todo_mail.pages.main_page import MainPage
from egogoger.todo_mail.pages.auth_page import AuthPage
from egogoger.base_test import Test
from egogoger.utils import set_input


class AuthTest(Test):
    def test(self):
        main_page = MainPage(self.driver)
        main_page.open()

        # window_before = self.driver.window_handles[0]
        main_page.open_auth()
        window_after = self.driver.window_handles[1]
        self.driver.switch_to_window(window_after)

        auth_page = AuthPage(self.driver)
        auth_page.check_for_self(self)

        set_input(self.driver, auth_page.EMAIL_INPUT, os.environ.get('LOGIN'))
        auth_page.next()
        set_input(self.driver, auth_page.PASSWORD_INPUT, os.environ.get('PASSWORD'))
        auth_page.submit()

        main_page.check_for_self(self)
