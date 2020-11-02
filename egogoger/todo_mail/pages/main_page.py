from egogoger.utils import wait_for_element_by_selector
from egogoger.default_page import DefaultPage, Component


class MainPage(DefaultPage):
    CONTAINER = '#root'
    OPEN_LINK = 'a.button[href="https://account.mail.ru/login?page=https://todo.mail.ru"]'
    TITLE = '.ListTitle_base__1l0yT h1'
    TITLE_NAME = 'Основной'

    def __init__(self, driver, path='https://todo.mail.ru/'):
        super().__init__(driver, path)

    def open_auth(self):
        wait_for_element_by_selector(self.driver, self.OPEN_LINK)
        self.driver.find_element_by_css_selector(self.OPEN_LINK).click()

    def check_for_self(self, test):
        wait_for_element_by_selector(self.driver, self.CONTAINER)
        wait_for_element_by_selector(self.driver, self.TITLE)
        test.assertEqual(
            self.TITLE_NAME,
            self.driver.find_element_by_css_selector(self.TITLE).text)
        test.assertEqual(
            self.PATH+'inbox',
            self.driver.current_url)
