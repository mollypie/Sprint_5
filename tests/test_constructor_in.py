from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from conftest import *


class TestConstructorIn:

    def test_enter_the_constructor_by_link_open_constructor(self, user):
        user.find_element(By.XPATH, HEADER_LINK_TO_ACCOUNT).click()
        WebDriverWait(user, 3).until(expected_conditions.visibility_of_element_located((By.XPATH, ACCOUNT_LINK_TO_PROFILE)))

        user.find_element(By.XPATH, HEADER_LINK_TO_CONSTRUCTOR).click()
        WebDriverWait(user, 3).until(expected_conditions.visibility_of_element_located((By.CLASS_NAME, MAIN_HEADER)))

        assert user.find_element(By.CLASS_NAME, MAIN_HEADER).text == 'Соберите бургер'

    def test_enter_the_constructor_by_logo_open_constructor(self, user):
        user.find_element(By.XPATH, HEADER_LINK_TO_ACCOUNT).click()
        WebDriverWait(user, 3).until(expected_conditions.visibility_of_element_located((By.XPATH, ACCOUNT_LINK_TO_PROFILE)))

        user.find_element(By.XPATH, HEADER_LOGO_LINK).click()
        WebDriverWait(user, 3).until(expected_conditions.visibility_of_element_located((By.CLASS_NAME, MAIN_HEADER)))

        assert user.find_element(By.CLASS_NAME, MAIN_HEADER).text == 'Соберите бургер'
