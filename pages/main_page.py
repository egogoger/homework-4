from pages.default_page import DefaultPage, Component
from utils import wait_for_element_by_selector


class MainPage(DefaultPage):
    PATH = ''

    @property
    def form(self):
        return AuthForm(self.driver)

    @property
    def logo(self):
        return Logo(self.driver)


class AuthForm(Component):
    LOGIN = 'input[name="Login"]'
    PASSWORD = 'input[name="Password"]'
    NEXT = '[data-test-id="next-button"]'
    SUBMIT = '[data-test-id="submit-button"]'

    def set_login(self, login):
        wait_for_element_by_selector(self.driver, self.LOGIN)
        self.driver.find_element_by_css_selector(self.LOGIN).send_keys(login)

    def set_password(self, pwd):
        wait_for_element_by_selector(self.driver, self.PASSWORD)
        self.driver.find_element_by_css_selector(self.PASSWORD).send_keys(pwd)

    def next(self):
        wait_for_element_by_selector(self.driver, self.NEXT)
        self.driver.find_element_by_css_selector(self.NEXT).click()
        
    def submit(self):
        wait_for_element_by_selector(self.driver, self.SUBMIT)
        self.driver.find_element_by_css_selector(self.SUBMIT).click()


class Logo(Component):
    LOGO = 'a.l-logo'

    def check_logo(self):
        wait_for_element_by_selector(self.driver, self.LOGO)
