from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from conftest import driver
from helpers import Helpers
from locators import *
from url_adresses import login_page


class TestConstructorIn:

    def test_enter_the_constructor_by_link_open_constructor(self, driver):
        driver.get(login_page)
        Helpers.login(driver)

        driver.find_element(By.XPATH, HEADER_LINK_TO_ACCOUNT).click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((By.XPATH, ACCOUNT_LINK_TO_PROFILE)))

        driver.find_element(By.XPATH, HEADER_LINK_TO_CONSTRUCTOR).click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((By.CLASS_NAME, MAIN_HEADER)))

        assert driver.find_element(By.CLASS_NAME, MAIN_HEADER).text == 'Соберите бургер'

    def test_enter_the_constructor_by_logo_open_constructor(self, driver):
        driver.get(login_page)
        Helpers.login(driver)

        driver.find_element(By.XPATH, HEADER_LINK_TO_ACCOUNT).click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((By.XPATH, ACCOUNT_LINK_TO_PROFILE)))

        driver.find_element(By.XPATH, HEADER_LOGO_LINK).click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((By.CLASS_NAME, MAIN_HEADER)))

        assert driver.find_element(By.CLASS_NAME, MAIN_HEADER).text == 'Соберите бургер'
