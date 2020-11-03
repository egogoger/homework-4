import os

from egogoger.todo_mail.pages.main_page import MainPage
from egogoger.todo_mail.pages.auth_page import AuthPage
from egogoger.base_test import Test
from egogoger.utils import set_input
from .auth_test import auth_test


class PriorityTest(Test):
    TODO_NAMES = ["First", "Second", "Third"]

    def setUp(self):
        print('setUp')
        auth_test(self)
        # Create 3 new tasks
        main_page = MainPage(self.driver)
        for name in self.TODO_NAMES:
            main_page.create_todo(name)

    def tearDown(self):
        # Delete 3 tasks
        print('tearDown')
        MainPage(self.driver).delete_todos()

    def test_priority_click(self):
        main_page = MainPage(self.driver)
        main_page.open_todo_options(0, self)
        main_page.open_priority_list()
        main_page.check_priority_list_open(self)
