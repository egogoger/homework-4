import datetime
import re

from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait


def wait_for_element_by_selector(driver, selector, visible=True):
    if visible:
        return WebDriverWait(driver, 10, 0.1).until(
            expected_conditions.visibility_of_element_located((By.CSS_SELECTOR, selector)))
    else:
        return WebDriverWait(driver, 10, 0.1).until(
            expected_conditions.invisibility_of_element_located((By.CSS_SELECTOR, selector)))

def get_datetime() -> str:
	return re.sub(r'[\.\-\s:]', '_', str(datetime.datetime.now()))
