from pages.default_page import DefaultPage, Component
from utils import wait_for_element_by_selector


class MainPage(DefaultPage):
    PATH = ''

    @property
    def reg_form(self):
        return RegForm(self.driver)


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

    def set_name(self, name):
        wait_for_element_by_selector(self.driver, self.NAME)
        self.driver.find_element_by_css_selector(self.NAME).send_keys(name)

    def set_password(self, password):
        wait_for_element_by_selector(self.driver, self.PASSWORD)
        self.driver.find_element_by_css_selector(self.PASSWORD).send_keys(password)


    # GETTERS
    @property
    def title_text(self):
        return self.driver.find_element_by_css_selector(self.TITLE).text

    # rewrite for all 
    def get_name_error(self, visible=True):
        wait_for_element_by_selector(self.driver, self.NAME_ERROR, visible)
        if visible:
            return self.driver.find_element_by_css_selector(self.NAME_ERROR)
        else:
            return None

    @property
    def login_error(self):
        wait_for_element_by_selector(self.driver, self.LOGIN_ERROR)
        return self.driver.find_element_by_css_selector(self.LOGIN_ERROR)

    @property
    def email_error(self):
        wait_for_element_by_selector(self.driver, self.EMAIL_ERROR)
        return self.driver.find_element_by_css_selector(self.EMAIL_ERROR)

    @property
    def password_error(self):
        wait_for_element_by_selector(self.driver, self.PASSWORD_ERROR)
        return self.driver.find_element_by_css_selector(self.PASSWORD_ERROR)
