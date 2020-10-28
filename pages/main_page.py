from pages.default_page import DefaultPage, Component
from utils import wait_for_element_by_selector


class MainPage(DefaultPage):
    PATH = ''

    @property
    def reg_form(self):
        return RegForm(self.driver)

    @property
    def login_form(self):
        return LoginForm(self.driver)


class RegForm(Component):
    # containers
    CONTAINER = '.l-form.l-card'
    TITLE = f'{CONTAINER} h2'

    # inputs
    NAME = '#name'
    LOGIN = '#login'
    EMAIL = '#email'
    PASSWORD = '#password'
    PASSWORD2 = '#password-confirm'

    # links and buttons
    LINK = '#signup-link'
    SUBMIT = '#signup-submit'
    ACCOUNT_ALREADY = '.m-form-description a.m-tiny-ref[href="/login"]'

    # errors
    ERROR_MESSAGE = '.m-error-message-small.is-error-input-underline'
    NAME_ERROR = f'{NAME} + {ERROR_MESSAGE}'
    LOGIN_ERROR = f'{LOGIN} + {ERROR_MESSAGE}'
    EMAIL_ERROR = f'{EMAIL} + {ERROR_MESSAGE}'
    PASSWORD_ERROR = f'{PASSWORD} + {ERROR_MESSAGE}'

    # METHODS
    def open(self):
        self.driver.find_element_by_css_selector(self.LINK).click()
        wait_for_element_by_selector(self.driver, self.CONTAINER)
        
    def submit(self):
        wait_for_element_by_selector(self.driver, self.SUBMIT)
        self.driver.find_element_by_css_selector(self.SUBMIT).click()

    def set_input(self, selector, value):
        wait_for_element_by_selector(self.driver, selector)
        element = self.driver.find_element_by_css_selector(selector)
        element.clear()
        element.send_keys(value)

    def click_on(self, selector):
        wait_for_element_by_selector(self.driver, selector)
        self.driver.find_element_by_css_selector(selector).click()


    # CHECKERS
    def check_error_msg_for(self, selector, test, text):
        if text is None:
            visible = False
        else:
            visible = True
        wait_for_element_by_selector(self.driver, selector, visible)
        if visible:
            test.assertEqual(text, self.driver.find_element_by_css_selector(selector).text)


class LoginForm(Component):
    CONTAINER = '.l-form.l-card'
    TITLE = f'{CONTAINER} h2'

    TITLE_TEXT = 'LOG IN'

    def check_for_self(self, test):
        wait_for_element_by_selector(self.driver, self.CONTAINER)
        wait_for_element_by_selector(self.driver, self.TITLE)

        test.assertEqual(self.TITLE_TEXT, self.driver.find_element_by_css_selector(self.TITLE).text)
