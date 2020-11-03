import time
from selenium.webdriver.common.keys import Keys

from egogoger.utils import wait_for_element_by_selector
from egogoger.default_page import DefaultPage, Component
from selenium.webdriver.common.action_chains import ActionChains


class MainPage(DefaultPage):
    FINAL_PATH = 'https://todo.mail.ru/inbox'
    # Selectors
    CONTAINER = '#root'
    TITLE = '.ListTitle_base__1l0yT h1'
    OPTION_LIST = '.ContextMenu_base__2Dkdw'
    TODO_POPUP_ITEM = OPTION_LIST+' p.c019.c019.c0130'
    PRIORITY_LIST = '.Popup_base__2plk2'
    PRIORITY_LIST_ITEM = PRIORITY_LIST + ' .MenuButton_text__1DWJd'
    TODO = CONTAINER + ' li[data-task-id]'
    NEW_TODO_INPUT = "input.c0147[placeholder=\"Создать задачу\"]"
    # OPEN_LINK = 'a.button[href="https://account.mail.ru/login?page=https://todo.mail.ru"]'

    TITLE_NAME = 'Основной'
    CHANGE_PRIORITY_TEXT = 'Изменить приоритет'
    TODO_DELETE_TEXT = 'Удалить'
    HIGH_PRIORITY = 'Высокий'
    MID_PRIORITY = 'Средний'
    LOW_PRIORITY = 'Низкий'
    NO_PRIORITY = 'Нет приоритета'

    PRIORITY_NAMES = [HIGH_PRIORITY, MID_PRIORITY, LOW_PRIORITY, NO_PRIORITY]

    def __init__(self, driver, path='https://account.mail.ru/login?page=https://todo.mail.ru'):
        super().__init__(driver, path)

    def get_todos(self):
        return self.driver.find_elements_by_css_selector(self.TODO)

    def create_todo(self, name: str):
        self.driver.find_element_by_css_selector(self.NEW_TODO_INPUT).send_keys(name, Keys.RETURN)
        wait_for_element_by_selector(self.driver, self.TODO)

    def delete_todos(self):
        # print('deleting todos')
        if self.driver.find_element_by_css_selector(self.PRIORITY_LIST) is not None:
            # print('found priority list')
            self.driver.find_element_by_css_selector(self.PRIORITY_LIST_ITEM).click()
        # Delete all todos
        while len(self.get_todos()) != 0:
            todo = self.get_todos()[0]
            # print('got todo')
            ActionChains(self.driver).context_click(todo).perform()
            # print('right clicked')
            wait_for_element_by_selector(self.driver, self.OPTION_LIST)
            for li in self.driver.find_elements_by_css_selector(self.TODO_POPUP_ITEM):
                if li.text == self.TODO_DELETE_TEXT:
                    print(li.text)
                    li.click()
                    break

    def open_todo_options(self, index, test):
        # print('open todo options')
        try:
            ActionChains(self.driver).context_click(self.get_todos()[index]).perform()
        except IndexError:
            print(self.get_todos())
            test.fail('No todo was found')

    def open_priority_list(self):
        # print('open priority list')
        wait_for_element_by_selector(self.driver, self.OPTION_LIST)
        for option in self.driver.find_elements_by_css_selector(self.TODO_POPUP_ITEM):
            if option.text == self.CHANGE_PRIORITY_TEXT:
                option.click()
                break

    def check_priority_list_open(self, test):
        print('check_priority_list_open')
        wait_for_element_by_selector(self.driver, self.PRIORITY_LIST)
        priority_list_items = self.driver.find_elements_by_css_selector(self.PRIORITY_LIST_ITEM)
        test.assertEqual(len(self.PRIORITY_NAMES), len(priority_list_items))
            

    def check_for_self(self, test):
        wait_for_element_by_selector(self.driver, self.CONTAINER)
        wait_for_element_by_selector(self.driver, self.TITLE)
        title_name = self.driver.find_element_by_css_selector(self.TITLE).text
        test.assertEqual(self.TITLE_NAME, title_name)

        current_url = self.driver.current_url
        test.assertEqual(self.FINAL_PATH, current_url)
